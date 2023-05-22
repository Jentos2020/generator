import json
import pyotp
from rest_framework.views import APIView
from .serializers import DocdataSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .tasks import makeImg
from .models import Document
from django.db.models import Max



class DocgenAPI(APIView):
    def post(self, request, format=None):
        serializer = DocdataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            photo = makeImg.apply_async(args=[request.data])
            return Response(photo.get(), status=status.HTTP_201_CREATED)
        return Response('Ошибка отправки данных', status=status.HTTP_400_BAD_REQUEST)

def docPage(request):
    if request.method == 'GET':
        imgCount = Document.objects.all()
        return JsonResponse(
            data={
                'imgCount': imgCount.aggregate(Max('pk'))['pk__max'],
            },
        )
    else:
        return HttpResponse("Only GET allowed")


@csrf_exempt
def codeGen(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data['key'])
        code2fa = pyotp.TOTP(data['key'])
        return JsonResponse(
            data={
                'code': code2fa.now(),
            },
        )
    else:
        return HttpResponse("Only POST allowed")

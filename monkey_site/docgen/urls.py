from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', docPage),
    path('create/', DocgenAPI.as_view()),
    path('codegen/', codeGen),
]  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
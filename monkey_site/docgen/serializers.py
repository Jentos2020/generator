from rest_framework import serializers
from .models import Document

class DocdataSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ('__all__')
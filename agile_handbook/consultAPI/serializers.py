from .models import Consult, Anamnese
from rest_framework import fields, serializers

class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'

class AnamneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnese
        fields = '__all__'
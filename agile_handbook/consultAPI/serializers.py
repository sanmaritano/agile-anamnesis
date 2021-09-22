from .models import Consult
from rest_framework import fields, serializers

class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'
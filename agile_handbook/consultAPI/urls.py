from django.urls import path, include
from django.views.generic import base
from .views import ConsultDetails, consult_list, ConsultAPIView
from rest_framework import routers, viewsets, permissions
from consultAPI import models, serializers

class ConsultViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConsultSerializer
    queryset = models.Consult.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class AnamneseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AnamneseSerializer
    queryset = models.Anamnese.objects.all()
    permission_classes = [permissions.IsAuthenticated]

route = routers.DefaultRouter()
route.register(r'paciente', ConsultViewSet, basename="Paciente")
route.register(r'anamnese', AnamneseViewSet, basename="Anamnese")

urlpatterns = [
    path('consult/', consult_list),
    #path('detail/<int:pk>', article_detail),
    path('consult/', ConsultAPIView.as_view()),
    path('consult/<int:id>', ConsultDetails.as_view()),
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
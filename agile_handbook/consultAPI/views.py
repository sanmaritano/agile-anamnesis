from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from .models import Consult
from .serializers import ConsultSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics, mixins


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializers_class = ConsultSerializer
    queryset = Consult.objects.all()


class ConsultAPIView(APIView):

    def get(self, request):
        consult = Consult.objects.all()
        serializer = ConsultSerializer(consult, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConsultSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsultDetails(APIView):

    def get_object(self, id):
        try:
            return Consult.objects.get(pk=id)

        except Consult.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        consult = self.get_object(id)
        serializer = ConsultSerializer(consult)
        return Response(serializer.data)

    def put(self, request, id):
        consult = self.get_object(id)
        serializer = ConsultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    
@api_view(['GET', 'POST'])
def consult_list(request):

    if request.method == 'GET':
        consult = Consult.objects.all()
        serializer = ConsultSerializer(consult, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConsultSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


#a request originate from my website
@api_view(['GET', 'PUT', 'DELETE'])
def consult_detail(request, pk):
    try:
        consult = Consult.objects.get(pk=pk)

    except Consult.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConsultSerializer(consult)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConsultSerializer(consult, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        consult.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
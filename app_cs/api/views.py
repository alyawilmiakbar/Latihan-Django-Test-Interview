# import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated  # <-- Here


# import local data
from .serializers import CustomerServiceSerializer
from app_cs.models import CustomerService
from django.http import JsonResponse

# create a viewset
class CSView(APIView):
	# define queryset
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        data_csservice = CustomerService.objects.all()
        serializer = CustomerServiceSerializer(data_csservice, many = True) 
        return Response(serializer.data, status = 200)

    def post(self, request, *args, **kwargs):
        serializer = CustomerServiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
    
        
        return Response(serializer.errors, status = 400)

class CSDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_by_id(self, id):
        try : 
            return CustomerService.objects.get(id = id)
        except CustomerService.DoesNotExist:
            raise exceptions.ParseError(detail = 'data tidak ditemukan')
            #return Response({'message': 'data tidak ditemukan'}, status = 404)

    def get(self, request, id, *args, **kwargs):
        data_csservice = self.get_by_id(id = id)
        serializer = CustomerServiceSerializer(data_csservice)
        return Response(serializer.data, status = 201)

    def put(self,request, id, *args, **kwargs):
        data_csservice = self.get_by_id(id = id)
        serializer = CustomerServiceSerializer(instance = data_csservice, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        
        return Response(serializer.errors, status = 400)

    def delete(self, request, id):
        data_cs = self.get_by_id(id)
        data_cs.delete()
        return Response({'message': 'terhapus'}, status = 200)
        

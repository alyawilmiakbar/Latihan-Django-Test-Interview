# import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated  # <-- Here


# import local data
from .serializers import AccountSerializer
from app_account.models import Account
from django.http import JsonResponse

# create a viewset
class AccountView(APIView):
    permission_classes = (IsAuthenticated,)
	# define queryset
    def get(self, request, *args, **kwargs):
        data_accounts = Account.objects.all()
        serializer = AccountSerializer(data_accounts, many = True) 
        return Response(serializer.data, status = 200)

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        
        return Response(serializer.errors, status = 400)

class AccountDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_by_id(self, id):
        try : 
            return Account.objects.get(id = id)
        except Account.DoesNotExist:
            raise exceptions.ParseError(detail = 'data tidak ditemukan')
            #return Response({'message': 'data tidak ditemukan'}, status = 404)

    def get(self, request, id, *args, **kwargs):
        data_account = self.get_by_id(id = id)
        serializer = AccountSerializer(data_account)
        return Response(serializer.data, status = 201)

    def put(self,request, id, *args, **kwargs):
        data_account = self.get_by_id(id = id)
        serializer = AccountSerializer(instance = data_account, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        
        return Response(serializer.errors, status = 400)

    def delete(self, request, id):
        data_account = self.get_by_id(id)
        data_account.delete()
        return Response({'message': 'terhapus'}, status = 200)


from rest_framework import serializers
from app_cs.models import CustomerService

class CustomerServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerService
		fields = '__all__'
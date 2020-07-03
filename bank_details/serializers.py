from rest_framework.serializers import (ModelSerializer, SerializerMethodField, Serializer)
from rest_framework import serializers
from .models import Branches

class BranchDetailsSerializer(ModelSerializer):
	bank_name = SerializerMethodField()
	class Meta:
		model = Branches
		fields = ['branch','bank_name','address', 'city', 'district', 'state']
	
	def get_bank_name(self, obj):
		return str(obj.bank.name)

		
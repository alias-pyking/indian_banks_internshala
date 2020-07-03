from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import  BranchDetailsSerializer
from .models import Branches, Banks
class BranchDetailsView(generics.GenericAPIView):
	serializer_class = BranchDetailsSerializer
	def get(self, request):
		ifsc = request.GET.get('ifsc')
		try:
			branch = Branches.objects.get(ifsc=ifsc)
		except Branches.DoesNotExist:
			return Response({'message': 'Branch with this ifsc code does not exists'}, status=status.HTTP_404_NOT_FOUND)
		serializer = BranchDetailsSerializer(branch)
		return Response(serializer.data)
	
class ListBranchDetailsView(generics.ListAPIView):
	serializer_class = BranchDetailsSerializer
	def get_queryset(self):
		try:
			name = self.request.GET.get('name')
		except:
			name = None
		try:
			city = self.request.GET.get('city')
		except:
			city = None
		if not name or not city:
			return []
		try:
			bank = Banks.objects.get(name = name)
		except Banks.DoesNotExist:
			return []
		branches = bank.branches_set.filter(city=city)
		return branches
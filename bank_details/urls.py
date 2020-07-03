from django.contrib import admin
from django.urls import path,include
from .views import BranchDetailsView, ListBranchDetailsView
urlpatterns = [
    path('branch_details/', BranchDetailsView.as_view(), name='branch_details'),
	path('branches_list/', ListBranchDetailsView.as_view(), name='branch_details_list'),
]

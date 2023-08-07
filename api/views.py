# from django.shortcuts import render
'views'
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializer


# Create your views here.
'''
https://www.youtube.com/watch?v=DNFTUtZf1Zc&t=2236s
46:00'''

class CompanyViewSet(viewsets.ModelViewSet):
    'class based api view'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
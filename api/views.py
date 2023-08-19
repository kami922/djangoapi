# from django.shortcuts import render
'views'
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
'''
https://www.youtube.com/watch?v=DNFTUtZf1Zc&t=2236s
46:00
'''

class CompanyViewSet(viewsets.ModelViewSet):
    'class based api view'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employess(self,request,pk=None)
        try:
            company = Company.objects.all(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializers = EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializers.data)
        except Exception as e:
            return Response({
                'message':'Company might not exit!! '
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    'class based api view for employee'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    
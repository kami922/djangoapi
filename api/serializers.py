'defined serializers '
from rest_framework import serializers
from .models import Company
from .models import Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    'serializer for company model'
    company_id = serializers.ReadOnlyField() #to show id on json
    class Meta:
        'defined model and field'
        model = Company
        fields = "__all__"
        
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    'serializer for employee model'
    class Meta:
        'define model and fields'
        model = Employee
        fields = "__all__"
        
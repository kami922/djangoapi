'defined serializers '
from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    'serializer for company model'
    company_id = serializers.ReadOnlyField() #to show id on json
    class Meta:
        'defined model and field'
        model = Company
        fields = "__all__"
        
'database model'
from django.db import models

# Create your models here.

class Company(models.Model):
    'class db'
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(("IT","IT"),
                                                    ("Non IT","Non IT"),
                                                    ("Mobile Phones","Mobile phones")
                                                    )),
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
                            
from django.db import models
from Guest.models import *

# Create your models here.
class tbl_usercomplaint(models.Model):
    comp_subject=models.CharField(max_length=30)
    comp_details=models.CharField(max_length=50)
    comp_date=models.DateField(auto_now_add=True)
    comp_reply=models.CharField(max_length=50)
    comp_status=models.IntegerField(default=0)
    client_id=models.ForeignKey(tbl_client,on_delete=models.CASCADE)
    
from django.db import models

class user_info(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    tel=models.CharField(max_length=32)
class department_info(models.Model):
    did=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=32)
    creat_date=models.DateField(auto_now_add=True)
class doctor_info(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    sex=models.CharField(max_length=16)
    seniority=models.CharField(max_length=32)#资历
    r_id=models.ForeignKey('department_info','did')
class ap_success(models.Model):
    ad_time=models.DateField(auto_now_add=True)
    num=models.CharField(max_length=32)
    user_id=models.ForeignKey('doctor_info','id')

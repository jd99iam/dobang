from django.db import models

# Create your models here.

class Member(models.Model):
    member_name = models.CharField(max_length=30)
    member_info = models.CharField(max_length=30)


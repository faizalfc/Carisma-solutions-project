from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

# Create your models here.

class EmpDetails(models.Model):
    Employee_id = models.IntegerField(primary_key=True)
    Employee_name = models.CharField(max_length=20,blank=False,null=False)
    Employee_mobile = models.CharField(max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10), RegexValidator(r'^\d{10}$', message='Mobile number must be exactly 10 digits')])
    Employee_email=models.EmailField(max_length=50)
    Employee_dob=models.DateField()

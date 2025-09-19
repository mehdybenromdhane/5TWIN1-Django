from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
# Create your models here.


def valide_cin(value):
    
    if len(value) !=8:
        
        raise ValidationError("Cin must has 8 characters")



def valide_email(value):
    
    if str(value).endswith('@esprit.tn') ==False:
        
        raise ValidationError("Your email must end with @esprit.tn")
    
    
class Person(AbstractUser):
    cin =models.CharField(max_length=8 , primary_key=True , validators=[valide_cin])
    
    email = models.EmailField(max_length=30 , validators=[valide_email])
    username = models.CharField(max_length=20 , unique=True)
    
    USERNAME_FIELD="username"
    
    
    class Meta:
        verbose_name="Person"
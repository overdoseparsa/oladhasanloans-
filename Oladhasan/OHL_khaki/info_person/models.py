from django.db import models
from django.utils import timezone
# Create your models here.
# this is the first models 
class Person(models.Model): # this is create here 
    tasfiye = "getter"
    bedehkar = "setter"

    list_type_off_person = {
        tasfiye: "تسویه",
        bedehkar: "بدهکار",
    }
    (name,family,phone,ncode,score ,descripion,totals)  = (models.CharField(max_length=350) for i in range(7)) 
    profiles = models.ImageField()
    (date_add_totals  , date_add_score ,) = (models.DateField(default=timezone.now) for i in range(2))
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True) 
    all_totals = models.CharField(max_length=350)
    all_totals = models.CharField(max_length=350)
    Type_person = models.CharField(
        max_length=10,
        choices=list_type_off_person,
        default=tasfiye,
    )
    # felan tamom bashe # we will add 
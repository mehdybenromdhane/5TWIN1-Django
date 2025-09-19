from django.db import models

# Create your models here.

from datetime import datetime

from Person.models import Person

category_list= (("Musique", "Musique"),
                ('Cinema','Cinema'),
                ('Sport','Sport')
                )

class Event(models.Model):
    
    title = models.CharField(max_length=30)
    description = models.TextField()
    
    image=models.ImageField(upload_to='images' , null=True)
    category = models.CharField(max_length=20 , choices=category_list)
    state = models.BooleanField(default=True)
    nbr_participants = models.IntegerField(default=0)
    evt_date= models.DateTimeField()
    creation_date= models.DateField(auto_now_add=True)
    updated_date= models.DateField(auto_now=True)
    
    
    organisateur = models.ForeignKey(Person , on_delete=models.SET_NULL , null=True )
    
    
    participant= models.ManyToManyField(Person , through="Participants" , related_name="participant")
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(evt_date__gt=datetime.now()) , name="Please check event date")
        ]
    
    
    def __str__(self):
        
        return self.title

    
    
class Participants(models.Model):
    
    person = models.ForeignKey(Person , on_delete=models.CASCADE)
    
    event = models.ForeignKey(Event , on_delete=models.CASCADE)
    
    
    participation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together=['person', 'event']
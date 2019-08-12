from django.db import models

# Create your models here.
class Candidate(models.Model):
    name=models.CharField(max_length=100)
    intoduction =models.CharField(max_length=100)
    Area=models.CharField(max_length=10)
    party_number=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

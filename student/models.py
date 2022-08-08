from statistics import mode
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    maths=models.CharField(max_length=50)
    english=models.CharField(max_length=50)
    biology=models.CharField(max_length=50)
    chemistry=models.CharField(max_length=50)
    history=models.CharField(max_length=50)
    physics=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    

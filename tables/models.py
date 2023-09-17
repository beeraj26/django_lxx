from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    storage = models.IntegerField()
    colour = models.CharField(max_length=20)
    descprition = models.TextField()
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

types = [
    ("О", "Однокомнатная"),
    ("Д", "Двухкомнатная")
]

class Apartment(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    type = models.CharField(max_length=1, choices=types)
    max_person = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    photo_main = models.FileField(upload_to="apartments", max_length=100)
    photo_main_little = models.FileField(upload_to="apartments", max_length=100)
    photo_1 = models.FileField(upload_to="apartments", max_length=100)
    photo_2 = models.FileField(upload_to="apartments", max_length=100)
    photo_3 = models.FileField(upload_to="apartments", max_length=100)
    photo_4 = models.FileField(upload_to="apartments", max_length=100)
    photo_5 = models.FileField(upload_to="apartments", max_length=100)
    photo_6 = models.FileField(upload_to="apartments", max_length=100)
    googlemap_addres = models.CharField(max_length=10000)
from django.db import models

# Create your models here.

types = [
    ("О", "Однокомнатная"),
    ("Д", "Двухкомнатная")
]

statuses = [
    ("С", "Свободный"),
    ("З", "Занят")
]

class Apartment(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    type = models.CharField(max_length=1, choices=types)
    max_person = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=1, choices=statuses, default="C")
    photo_main = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_main_little = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_1 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_2 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_3 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_4 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_5 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_6 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_7 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_8 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_9 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_10 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_11 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    photo_12 = models.FileField(upload_to="apartments", max_length=100, null=True, blank=True)
    googlemap_addres = models.CharField(max_length=10000)
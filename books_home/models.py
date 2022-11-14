from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


cc = (('programming','programming'),
      ('social','social'),
      ('politics','politics'),
      ('fitness','fitness'),
      ('maths','maths'))

class Books(models.Model):

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    photo1 = models.ImageField(upload_to = "photos/%Y/%m/%d/",blank=True)
    photo2 = models.ImageField(upload_to = "photos/%Y/%m/%d/",blank=True)
    photo3 = models.ImageField(upload_to = "photos/%Y/%m/%d/",blank=True)
    photo4 = models.ImageField(upload_to = "photos/%Y/%m/%d/",blank=True)
    photo5 = models.ImageField(upload_to = "photos/%Y/%m/%d/",blank=True)
    photo6 = models.ImageField(upload_to = "photos/%Y/%m/%d/",blank=True)
    is_published = models.BooleanField(default=True)
    pdf = models.FileField(upload_to = "pdfs/%Y/%m/%d/",blank=True)
    category= models.CharField(choices=cc,null=True,max_length=100)
    book_date = models.DateTimeField(default=datetime.now(),blank=True) 

    def __str__(self):
        return self.title
    

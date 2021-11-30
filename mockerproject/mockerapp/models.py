from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Career(models.Model):
    Jobtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    salary = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    contact = models.IntegerField(default="")

    def __str__(self):
        return self.Jobtitle

class Contact(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    email = models.EmailField()
    phone = models.IntegerField(default=91)

    def __str__(self):
        return self.name

class Membership(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to="uploads/memberships")
    price = models.IntegerField(default=2000)
    is_available = models.BooleanField(default=True)
    discount = models.PositiveIntegerField(default=0)
    tutors = models.CharField(max_length=3000,default="")
    tutorimage1 = models.ImageField(upload_to="uploads/tutorimages",default="")
    tutorimage2 = models.ImageField(upload_to="uploads/tutorimages",null=True,blank=True)
    tutorimage3 = models.ImageField(upload_to="uploads/tutorimages",null=True,blank=True)

    def __str__(self):
        return self.name    

class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    phone = models.PositiveIntegerField(default=0)
    address = models.TextField(max_length=3000)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.user.first_name

class Team(models.Model):
    image = models.ImageField(upload_to="uploads/teamimages")
    name = models.CharField(max_length=200)
    jobtitle = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    linkedinprofile = models.CharField(max_length=400,null=True,blank=True)
    Instagramprofile = models.CharField(max_length=400,null=True,blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    subject = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/ads",null=True,blank=True)
    videoad = models.FileField(upload_to="uploads/advideos",null=True,blank=True)

    def __str__(self):
        return self.subject
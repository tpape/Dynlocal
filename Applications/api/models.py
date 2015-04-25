from django.db import models
from django.contrib.auth.models import User
from django_base64field.fields import Base64Field
# Create your models here.
class UserProfile(models.Model):
    #links UserProfile to User model (User is automatically generated by Django)
    user = models.OneToOneField(User)
    #NOT generated automatically fields
    registration_history = models.TextField(null=True, blank=True)

class ProfileContributer(models.Model):
    id_user = models.OneToOneField(UserProfile)
    label = models.CharField(db_index=True, max_length=30)
    latitude = models.DecimalField(db_index=True, max_digits=10,decimal_places=7)
    longitude = models.DecimalField(db_index=True,max_digits=10,decimal_places=7)
    img = Base64Field()
    postal_address = models.CharField(max_length= 100)
    description = models.TextField()
    availibility = models.TextField()
    contact = models.TextField()
    visible = models.BooleanField()

class ProfileVisitor(models.Model):
    id_user = models.OneToOneField(UserProfile)
    labels_interested_in = models.TextField()
    img = Base64Field()
    id_bid = models.PositiveIntegerField()
    favorite = models.ManyToManyField(ProfileContributer)

class Tag(models.Model):
    label = models.CharField(db_index=True, max_length=50)
    tagged = models.ManyToManyField(ProfileContributer)

class Bid(models.Model):
    #the user that was given the bid
    id_user = models.OneToOneField(UserProfile, null=True, blank=True)
    #the contributer that gives the bid to the user
    id_Contributer = models.OneToOneField(ProfileContributer, null=True, blank=True)
    duration = models.CharField(max_length=10)
    expiration_date = models.DateField()

def __unicode__(self):
        return self.title

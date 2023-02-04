from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=200, null=True)
    User_Name = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Phone = models.PositiveBigIntegerField()
    Passport_Number	= models.PositiveBigIntegerField()
    def __str__(self):
        return self.user.username
    def __str__(self):
        return self.Full_Name


class player (models.Model):

    Name =models.CharField(max_length=200, null=True)
    Added_Date =models.DateTimeField(auto_now_add=True, null=True)
    Passport_Number	=models.PositiveBigIntegerField()
    
class username (models.Model):

    Full_Name = models.CharField(max_length=200, null=True)
    User_Name = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Phone = models.PositiveBigIntegerField()
    Passport_Number	= models.PositiveBigIntegerField()
    def __str__(self):
        return self.user.username
    def __str__(self):
        return self.Full_Name
    
    def __unicode__(self):
        return self.name
            
class contact (models.Model):

    Name =models.CharField(max_length=200, null=False)
    E_mail =models.EmailField(max_length=200, null=True)
    Area_code =models.CharField(max_length=200, null=True)
    Phone_Number =models.CharField(max_length=200, null=True)
    Country =models.CharField(max_length=200, null= False)
    City =models.CharField(max_length=200, null= False)
    State =models.CharField(max_length=200, null= False)
    Zip_Code =models.CharField(max_length=200, null= False)
    Address =models.CharField(max_length=200, null= False)
    FIG_License_Number =models.CharField(max_length=200, null= False)
    Passport_Number	=models.CharField(max_length=200, null= False)
    ##UserProfile = models.ForeignKey(UserProfile, null = True, on_delete = models.CASCADE)
    UserProfile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
    def __unicode__(self):
        return self.name
    
class passport (models.Model):

    Surname =models.CharField(max_length=200, null=True)
    First_Name =models.CharField(max_length=200, null=True)
    Passport_Number =models.PositiveBigIntegerField()
    E_mail =models.EmailField(max_length=200, null=True)
    ##Gender =models.CharField(max_length=1, choices=gender) 
    Passport_Expiry_Date=models.DateTimeField(auto_now_add=False, null=True)
    Passport_Photo =models.CharField(max_length=200, null=True)


class music (models.Model):

    Composer =models.CharField(max_length=200, null=True)
    Title =models.CharField(max_length=200, null=True)
    Artist =models.CharField(max_length=200, null=True)
    Music_name =models.CharField(max_length=200, null=True)


class travel (models.Model):

    Type =models.CharField(max_length=200, null=True)
    Flight_Number =models.PositiveBigIntegerField()
    Date =models.DateTimeField(auto_now_add=False, null=True)
    Country =models.CharField(max_length=200, null=True)
    Airport =models.CharField(max_length=200)
    

# Create your models here.

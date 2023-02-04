from django import forms

from django.forms import ModelForm

from .models import *


##class add_homeform(ModelForm):
##    class Meta:
##        model = UserProfile
##        fields = ["Phone"]
##
##class update_homeform(ModelForm):
##    class Meta:
##        model = UserProfile
##        fields = ["Phone"]


class add_playerform(ModelForm):
    class Meta:
        model = contact
        fields = ["Name", "E_mail", "Area_code", "Phone_Number","Country","City","State","Zip_Code","Address","FIG_License_Number","Passport_Number"]
    
class update_playerform(ModelForm):
    class Meta:
        model = contact
        fields = ["Name", "E_mail", "Area_code", "Phone_Number","Country","City","State","Zip_Code","Address","FIG_License_Number","Passport_Number"]
        
        

    
class add_musicform(ModelForm):
    class Meta:
        model = music
        fields = '__all__'
      
class add_passform(ModelForm):
    class Meta:
        model = passport
        fields = '__all__'
        
class add_travelform(ModelForm):
    class Meta:
        model = travel
        fields = '__all__'


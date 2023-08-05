from tkinter import Widget
from django import forms
from soupsieve import select
from .models import *
from prison.models import * 
#from datetimepicker.widgets import DateTimePicker
from django.forms.widgets import NumberInput
  

GENDER=(('Female','Female'),('Male','Male'))
BLOODTYPES=(('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'), ('O+','O+'),('O-','O-'))

class DateInput(forms.DateInput):
    input_type = 'date'

cat_choice=(
    ('Criteria1','Criteria1'),
    ('Criteria2','Criteria2')
)

class PrisonForm(forms.ModelForm):
    class Meta:
        model = Prison
        fields = '__all__'
       
# class CrimeForm(forms.ModelForm):
#     class Meta:
#         model = Crime
#         fields = '__all__'
#         exclude = ('createdby',)
         
class CriminalForm(forms.ModelForm): 
    ReleasedDate=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    EntranceDate=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    Gender=forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER) 
    Category=forms.ChoiceField(widget=forms.RadioSelect, choices=cat_choice)
    Bloodtype= forms.ChoiceField(choices=BLOODTYPES) 
   
    class Meta:
        model=Criminal
        fields='__all__'
        exclude = ('createdby','prison','Status',)
        
class VisitorForm(forms.ModelForm):
    class Meta:
            model=Visitor 
            exclude = ('createdby','VisitDate',)
    Gender=forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER) 

class ImageForm(forms.ModelForm):
   
    class Meta:
        model=Image
        fields=['cname','image']     

   
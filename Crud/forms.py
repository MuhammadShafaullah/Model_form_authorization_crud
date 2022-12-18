from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from unicodedata import name
from django import forms
from .models import User

class Student(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password','rpassword']
        
        
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'rpassword':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
        
    #password cheking
    def clean(self):
     cleaned_data=super().clean()
     valpwd=self.cleaned_data['password']
     valrpwd=self.cleaned_data['rpassword']
       
     if valpwd !=valrpwd:
        raise forms.ValidationError('Password not mached!')
        
    
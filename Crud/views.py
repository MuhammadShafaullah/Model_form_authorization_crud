
from urllib import request
from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import Student
from django.contrib import messages

# Create your views here.

# This function Add new item and show all ite m
def home(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            rpassword = fm.cleaned_data['rpassword']
            reg=User(name=name,email=email,password=password,rpassword=rpassword)
            reg.save()
            messages.add_message(request,messages.SUCCESS,'Your account has been created!!')
            fm = Student()
    else:
        fm = Student()
    stud=User.objects.all()
    return render(request, 'Crud/home.html', {'form': fm,'stu':stud})

#Delete function
def delete_data(request,id):
    if request.method== 'POST':
        pi =User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm =Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         
        pi = User.objects.get(pk=id)
        fm =Student(instance=pi)       
    return render(request, 'Crud/update.html',{'form':fm})
        


#  if fm.is_valid():
#             name=fm.cleaned_data['name']
#             email=fm.cleaned_data['email']
#             password=fm.cleaned_data['password']
#             rpassword=fm.cleaned_data['rpassword']
            # reg=User(name=name,email=email,password=password,rpassword=rpassword)
            # reg.save()
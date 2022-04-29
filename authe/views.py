from contextlib import redirect_stderr
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from authe.models import registermodel
from authe.forms import registerform,loginform
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def registerview(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data['email']
            user=form.cleaned_data['username']
            subject='welcome to spiders matrimony '
            message=f'Hi Mr/Mrs.. {user.title()}\n select your companion'
            email_from= settings.EMAIL_HOST_USER
            rep=[email,]
            send_mail(message=message, subject=subject, from_email=email_from, recipient_list=rep)
            messages.success(request,'registration is success')
            return redirect('/authe/login/')
        else:
            messages.error(request,'registration is failed')
            
    return render(request,'register.html',{'form':form})

def loginview(request):
    form=loginform()
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'login is success')
                return redirect('/authe/home/')
            else:
                messages.error(request,'login is failed')
    return render(request,'login.html',{'form':form})

@login_required(login_url='/authe/login/')
def logoutview(request):
    logout(request)
    messages.success(request,'logout is success')
    return redirect('/authe/login/')

@login_required(login_url='/authe/login/')
def homeview(request):
    return render(request,'home.html')
'''
class registerview(CreateView):
    template_name='register.html'
    model=registermodel
    context_object_name='form'
    fields=['username','first_name','last_name','email','phone','age','gender','dob','password']
    form_class=registerform
    success_url='/admin/'

'''
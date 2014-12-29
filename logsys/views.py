from django.shortcuts import render,render_to_response,redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from Car.forms import Registration
# Create your views here.
#-*- encoding: utf-8 -*-
def login(reguest):
    args = {}
    args.update(csrf(reguest))
    if reguest.POST:
        username = reguest.POST.get('username', '')
        password = reguest.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(reguest, user)
            return redirect('/')
        else:
            args['login_error']= "Error"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(reguest):
    auth.logout(reguest)
    return redirect("/")

def register(reguest):
    args = {}
    args.update(csrf(reguest))
    args['form'] = UserCreationForm()
    if reguest.POST:
        new_user_form = UserCreationForm(reguest.POST)
        new_user_form.save()
        new_user = auth.authenticate(username= new_user_form.cleaned_data['username'],
                                      password= new_user_form.cleaned_data['password2'],
                                      email=new_user_form.cleaned_data['email'],
                                      first_name=new_user_form.cleaned_data['first_name'],
                                      last_name=new_user_form.cleaned_data['last_name']
                                        )
        auth.login(reguest, new_user)
        args['word']= "Thank you for registering"
        args['form']= new_user_form
    return render_to_response('register.html', args)


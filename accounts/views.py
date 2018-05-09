# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms

def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('activities:activity_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        val = form.is_valid()
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('activities:activity_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    print("logout")
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

@login_required(login_url='/accounts/login/')
def create_drink(request):
    if request.method =='POST':
        form = forms.CreateDrink(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('activities:activity_list')
    else:
        form = forms.CreateDrink()
    return render(request, 'accounts/create_drink.html' ,  {'form':form})

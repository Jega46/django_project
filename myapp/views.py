# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm  # Import LoginForm from forms.py

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page or home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')


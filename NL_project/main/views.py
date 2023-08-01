from django.shortcuts import render
from django.http import HttpResponse

def index(reqwest):
    return render (reqwest, 'main/index.html')

def about(reqwest):
    return render (reqwest, 'main/about.html')

def contacts(reqwest):
    return render (reqwest, 'main/contacts.html')

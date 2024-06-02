from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#------------------------------- student homepage --------------------------
def home_page(request):
    context=loader.get_template('index.html')
    return HttpResponse(context.render())

#--------------------------------about page---------------------------------

def about_page(request):
    context=loader.get_template('front_about.html')
    return HttpResponse(context.render())

def contact_page(request):
    context=loader.get_template('front_contact.html')
    return HttpResponse(context.render())



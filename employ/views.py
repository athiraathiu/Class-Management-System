from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def edit_emp(request):
    context=loader.get_template('edit_emp.html')
    return HttpResponse(context.render())

def emp_reg(request):
    context=loader.get_template('emp_reg.html')
    return HttpResponse(context.render())

def emp_list(request):
    context=loader.get_template('emplist.html')
    return HttpResponse(context.render())



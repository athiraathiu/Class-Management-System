from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User,auth

# Create your views here.
#------------------------------- master designation(add,edit,view) --------------------------
def admin_signin(request):
    context=loader.get_template('admin_signin.html')
    return HttpResponse(context.render())

def admin_chng_pass(request):
    context=loader.get_template('admin_chngpass.html')
    return HttpResponse(context.render())

def user_create(request):
    if request.POST:
        fst_name=request.POST['fst']
        lst_name=request.POST['lst']
        email=request.POST['eml']
        usr_name=request.POST['usrnm']
        pasword=request.POST['pass']
        cpassword=request.POST['cpass']
        v=User.objects.create_user(last_name=lst_name,first_name=fst_name,password=pasword,username=usr_name,email=email)
        v.save()
    return render(request,'create_user.html')

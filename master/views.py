from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from master.models import *
from django.contrib import messages
from django.db. models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

#------------------------------- MASTER DESIGNATION ------------------------------------------
#--------------------------------(add designation)--------------------------------------------
def add_des(request):
    message=''
    if request.POST:
        a=request.POST['txt1']
        b=request.POST['txt2']
        if Designation.objects.filter(Q(desg_name=a) | Q(desg_code=b)).exists():
            message='Already Added'
        else:
            v=Designation(desg_name=a, desg_code=b)
            v.save()
            message='Successfully Added'
    return render(request,'add_designation.html',{'messages':message})

#------------------------------------ edit designation -----------------------------------------------

def edit_des(request, eds):
    if request.method == 'POST':
        edt1 = request.POST['ed1']
        edt2 = request.POST['ed2']

        # Check if a designation with the same name and code already exists
        nw = Designation.objects.filter (Q(desg_name=edt1)| Q(desg_code=edt2) ).exclude(id=eds)
        if nw.exists():
            messages.error(request, 'Designation with this  already exists.')
            return redirect('view_des')

        # Update the existing designation
        rw = Designation.objects.get(id=eds)
        rw.desg_name = edt1
        rw.desg_code = edt2
        rw.save()

        messages.success(request, 'Successfully Updated')
        return redirect('view_des')

    # If it's a GET request, retrieve the designation for editing
    s = Designation.objects.get(id=eds)
    return render(request, 'edit_designation.html', {'data': s})
#---------------------------------------view designation------------------------------------------------

def view_des(request):
    rc=Designation.objects.all()
    return render(request,'view_designation.html',{'records':rc})

#-------------------------------------delete designation------------------------------------------------
def del_des(request,d_id):
    r=Designation.objects.get(id=d_id)
    r.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('view_des')
  

#----------------------------MASTER QUALIFICATION------------------------------------------------
#---------------------------(add qualification)---------------------------------------------------
@login_required
def add_qual(request):
    message=''
    if request.POST:
        # print(a)
        a=request.POST['qual'] # textbox value given to 'a'
        if qualification.objects.filter(qual_name=a).exists():
            message='already added'
        
        else:
            v=qualification(qual_name=a)
            v.save()
            message='sucessfully added'
    return render(request,'add_qualification.html',{'messages':message})

#-----------------------------------------Edit qualification------------------------------------------------


def edit_qual(request, e_id):
    if request.POST:
        b = request.POST['nm']
        # Check if a qualification with the same name already exists
        n = qualification.objects.filter(qual_name=b).exclude(id=e_id)
        if n.exists():
            messages.error(request, 'Qualification with this name already exists.')
            return redirect('view_qual')
        # Update the existing qualification
        r = qualification.objects.get(id=e_id)
        r.qual_name = b
        r.save()
        messages.success(request, 'Successfully Updated')
        return redirect('view_qual')
    # If it's a GET request, retrieve the qualification for editing
    r = qualification.objects.get(id=e_id)
    return render(request, 'edit_qualification.html', {'data': r})

#--------------------------------view qualification------------------------------------------------------

def view_qual(request):
    record=qualification.objects.all()
    return render(request,'view_qualification.html',{'records':record})

#--------------------------------delete qualification------------------------------------------------------

def del_qual(request,q_id):
    c=qualification.objects.get(id=q_id)
    c.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('view_qual')


#---------------------------- master class (add)(view)--------------------------------------------------

def add_cls(request):
    message=''
    if request.POST:
        # print(a)
        a=request.POST['cls'] # textbox value given to 'a'
        if Addcls.objects.filter(cls=a).exists():
            message='already added'
        else:
            v=Addcls(cls=a)
            v.save()
            message='sucessfully added'
    rc=Addcls.objects.all()       
    return render(request,'addclass.html',{'messages':message,'sample':rc})

#----------------------------------delete class----------------------------------------------------------

def dlt_cls(request,cl_id):
    cl=Addcls.objects.get(id=cl_id)
    cl.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('add_cls')

#----------------------------- master division(add)-----------------------------------------------

def add_div(request):
    message=''
    if request.POST:
        # print(a)
        a=request.POST['divv'] # textbox value given to 'a'
        if Add_div.objects.filter(div=a).exists():
            message='already added'
        else:
            v=Add_div(div=a)
            v.save()
            message='sucessfully added'
    rc=Add_div.objects.all()       
    return render(request,'add_div.html',{'messages':message,'data':rc})
#--------------------------------DLT DIVISION--------------------------------------------

def dlt_div(request,div_id):
    cl=Addcls.objects.get(id=div_id)
    cl.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('add_cls')

#----------------------------- change password-----------------------------------------------

def chnge_pass(request):
    context=loader.get_template('chnge_pass.html')
    return HttpResponse(context.render())



def add_cat(request):
    if request.POST:
        x=request.POST['c_name']
        obj=Category(cat_name=x)
        obj.save()
        for i in range(1,6):
             y=request.POST[f'item{i}']
             n=Product(itm=y,c_id=obj)
             n.save()    
    d=loader.get_template('catgry.html')
    return HttpResponse(d.render())

def cat_lst(request):
    x=Category.objects.all()
    return render(request,'cat_lst.html',{'data':x})















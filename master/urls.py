"""
URL configuration for cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('ad/', views.add_des,name='add_des'),
    path('ed/<int:eds>', views.edit_des,name='edit_des'),
    path('vd/', views.view_des,name='view_des'),
    path('dlqs/<int:d_id>', views.del_des,name='del_des'),
    
    path('aq/', views.add_qual,name='add_qual'),
    path('eq/<int:e_id>', views.edit_qual,name='edit_qual'),
    path('vq/', views.view_qual,name='view_qual'),
    path('dlq/<int:q_id>', views.del_qual,name='del_qual'),
    
    path('acls/', views.add_cls,name='add_cls'),
    path('delcl/<int:cl_id>', views.dlt_cls,name='dlt_cls'),
    path('adiv/', views.add_div,name='add_div'),
    path('deldiv/<int:div_id>', views.dlt_div,name='dlt_div'),
    path('cpass/', views.chnge_pass,name='chnge_pass'),
    
    path('add_cat/',views.add_cat,name='add_cat'),
    path('cat_lst/', views.cat_lst,name='cat_lst'),
  
    
    
    
]

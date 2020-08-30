"""employee_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from employee_register import views as employee_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , employee_view.home , name = 'home_page') ,
    path('employee/' , employee_view.employee_form , name = 'employee_insert') , 
    path('employee/<int:id>/' , employee_view.employee_form , name = 'employee_update') ,
    path('employee/list/' , employee_view.employee_list , name = 'employee_list') , 
    path('employee/delete/<int:id>/' , employee_view.employee_delete , name = 'employee_delete' ) ,
]

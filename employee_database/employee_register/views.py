from django.shortcuts import render , redirect 
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def employee_list(request ) :
    context = {"employee_list" : Employee.objects.all() }
    return render (request , 'employee_register/employee_list.html' , context )

# when id is 0 ,operation will be insert ,when id is not 0 , operation will be update 
def employee_form(request , id = 0 ) :
    if id != 0 :
        emp = Employee.objects.get(pk = id ) 
        if request.method == "POST" :
            form = EmployeeForm(request.POST , instance = emp )
            if form.is_valid() :
                form.save() 
                return redirect('employee_list')
        else :
            form  = EmployeeForm(instance = emp)
        return render(request , 'employee_register/employee_form.html' , {'form' : form })
    else :
        if request.method == "POST" : 
            form = EmployeeForm(request.POST) 
            if form.is_valid() :
                form.save() 
                return redirect('employee_list')
        else : 
            form = EmployeeForm()
        return render(request , 'employee_register/employee_form.html' , {"form" : form }) 


def employee_delete(request ,id = 0 ) :
    emp = Employee.objects.get(pk = id )
    emp.delete() 
    return redirect("employee_list") 

def home (request ) :
    return render(request , 'employee_register/home.html' ) 
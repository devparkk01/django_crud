from django import forms
from .models import Employee 

class EmployeeForm (forms.ModelForm) :

    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
            'fullname' : "Full Name " ,
            'contact'  : "Contact " ,
            'emp_code' : "EMP Code " ,
            'position' : "Position " ,
        }

    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['position'].empty_label = "Select"

        
    # write clean method on field contact 

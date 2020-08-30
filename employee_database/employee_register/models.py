from django.db import models

# Create your models here.

class Position (models.Model ) :
    title = models.CharField(max_length = 20)


    def __str__ (self) :
        return self.title 


class Employee (models.Model ) :
    fullname        = models.CharField(max_length = 40)
    contact         = models.CharField(max_length = 10)
    emp_code        = models.CharField(max_length = 3 )
    position        = models.ForeignKey(to = Position , on_delete= models.CASCADE ) 

    # def __str__(self) :
    #     return self.fullname 
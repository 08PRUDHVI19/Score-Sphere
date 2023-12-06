from django.db import models

from django.utils.translation import gettext as _

class Student(models.Model):
    reg_no=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.reg_no
    
class Semester(models.Model):
    semester=models.IntegerField(null=True)
    start_year=models.DateField()
    end_year=models.DateField()

    def __str__(self):
        return f"{self.semester}"
    
class Course(models.Model):
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    code=models.BigIntegerField()
    name=models.CharField(max_length=100)
    credits=models.IntegerField()

    def __str__(self):
        return self.name

    


class Result(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    grade=models.CharField(max_length=4,null=True)

    def __str__(self):
         return f'{self.student} - {self.course}'
    

class SemResult(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    SGPA=models.FloatField()

    def __str__(self):
        return f"{self.student}"
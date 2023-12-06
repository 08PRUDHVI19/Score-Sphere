from django.core.management.base import BaseCommand
from core.models import *
import pandas as pd

class Command(BaseCommand):
    help="Importing Sem 2 results into a database"

    def add_arguments(self,parser):
        parser.add_argument('results1.csv',type=str,help="The path of a File")

    def handle(self,*args,**kwargs):
        file_path=kwargs['results1.csv']
        df=pd.read_csv(file_path)
        
        for index,row in df.iterrows():
            reg_no=row['reg_no']
            try:
                student=Student.objects.get(reg_no=reg_no)
            except Student.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"😟the student with id {reg_no} doesnot Exists in this Database"))
                continue


            sem1=1
            try:
                semester=Semester.objects.get(semester=sem1)
            except Semester.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"😟the semester {sem1} doesnot Exists in this Database"))
                continue

            SGPA=row['SGPA']

            SemResult.objects.get_or_create(student=student,semester=semester,defaults={'SGPA':SGPA})

            subjects=['1000221102','1000221103','1000221109','1005221100','1000221114','1000221170','1005221110','1003221102','1000221120']
            for subject in subjects:

                try:
                    course=Course.objects.get(code=subject)
                except Course.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"😟the course  with id {subject} doesnot Exists in this Database"))
                    continue
                
                grade=row[subject]

                Result.objects.get_or_create(student=student,course=course,defaults={'grade':grade})


               


        self.stdout.write('Successfully imported CSV File into  database..........🎉🎊')



            
        
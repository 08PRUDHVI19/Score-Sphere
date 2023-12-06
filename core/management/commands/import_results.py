from typing import Any
from django.core.management.base import BaseCommand, CommandParser

from core.models import *

import pandas as pd

class Command(BaseCommand):
    help="Importing the sem 2  results csv  file data into a daatabase"
    def add_arguments(self, parser):
        parser.add_argument('results.csv',type=str,help="Path to the CSV File")

    def handle(self, *args, **kwargs):
        file_path = kwargs['results.csv']
        df = pd.read_csv(file_path)

        for index,row in df.iterrows():
            reg_id=row['reg_no']

            try:
                student=Student.objects.get(reg_no=reg_id)
            except Student.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Student {reg_id} is not found...Skipping entry................"))
                continue

            sem=2
            try:
                semester=Semester.objects.get(semester=sem)
            except Semester.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Semester {sem} does not Exists "))
                continue

            SGPA=row['SGPA']

            SemResult.objects.get_or_create(student=student,semester=semester,defaults={'SGPA':SGPA})
            
            subjects=['1000221202','1054221200','1005221202','1005221203','1000221107','1054221210','1000221112','1005221212','1000221210','1000221210']
            
            for subject in subjects:
                try:
                    course=Course.objects.get(code=subject)
                except Course.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Course with course code {subject} doesnot exists......skipping............"))
                    continue

                grade=row[subject]
                Result.objects.get_or_create(student=student,course=course,defaults={'grade':grade})





        self.stdout.write('Successfully imported CSV File into  database..........🎉🎊')
        
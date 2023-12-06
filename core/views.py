from django.shortcuts import render,redirect

from django.http import HttpResponse
from .forms import getResults
from .models import *


from django.views import View
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


def index(request):
    form=getResults()
    # if request.method=='GET':
    if 'id' in request.GET:
        form=getResults(request.GET)
        if form.is_valid():
            id=form.cleaned_data.get('id')
            id=id.upper()
            try:
                student=Student.objects.get(reg_no=id)
                sems=Semester.objects.all()
                sem=Semester.objects.get(semester=1)
                results=Result.objects.filter(student=student)
                CGPA=0.0
                points=SemResult.objects.filter(student=student)
                for k in points:
                    CGPA+=k.SGPA
                context={'form':form,'student':student,'results':results,'points':points,'sem':sem,'CGPA':CGPA/points.count(),'sems':sems}
                return render(request,'core/main.html',context)
            except Student.DoesNotExist:
                return render(request,'core/notfound.html',{'Errorid':id,})

    context={'form':form}
    return render(request,'core/main.html',context)



def render_to_pdf(temp_src,context_dict={}):
    template=get_template(temp_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None


class ViewPDF(View):
    def get(self,request,id,*args,**kwargs):
        id=id.upper()
        student=Student.objects.get(reg_no=id)
        sems=Semester.objects.all()
        sem=Semester.objects.get(semester=1)
        results=Result.objects.filter(student=student)
        CGPA=0.0
        points=SemResult.objects.filter(student=student)
        for k in points:
            CGPA+=k.SGPA
        context={'student':student,'results':results,'points':points,'sem':sem,'CGPA':CGPA/points.count(),'sems':sems}

        
        pdf=render_to_pdf('core/resultspdf.html',context)
        return HttpResponse(pdf,content_type='application/pdf')




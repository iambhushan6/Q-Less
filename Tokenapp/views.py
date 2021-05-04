from django.shortcuts import render,HttpResponse
from Tokenapp.models import Student
from datetime import datetime

# Create your views here.

def studentview(request):
    context={
        'success': False
    }
    if request.method == "POST":    
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        gr_no = request.POST.get('gr_no')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        query = request.POST.get('query')    

        student_detail = Student(
        name = name,
        email = email,
        gr_no = gr_no,
        branch = branch,
        year = year,
        query = query,
        date = datetime.datetime.now()
        )

        student_detail.save()

        context={
            'success':True
        }

    return render(request,"studentview.html",context)
    # return HttpResponse("Hello Bhushan")

def adminview(request):
    registrations = Student.objects.all()
    context={
        'entries': registrations
    }
    return render(request,'adminview.html',context)

def thanku(request):
    return render(request,'thanku.html')
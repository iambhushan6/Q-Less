from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from Tokenapp.models import AlumniCurrentToken, CurrentToken, Student, Alumni
from datetime import datetime

# Create your views here.

def studentview(request):
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
        query = query
        )

        student_detail.save()
        return redirect('token')

    return render(request,"studentview.html")

def adminview(request):
    registrations = Student.objects.all()
    context={
        'entries': registrations
    }
    return render(request,'adminview.html',context)

def token(request):
    tokennum = Student.objects.last()
    context = {
        'tokenno': tokennum
    }
    return render(request,'token.html', context)

def markasresolved(request, pk):
    registrations = Student.objects.get(pk=pk)
    lastdeleted = CurrentToken.objects.all()
    lastdeleted.update(token = pk+1) 
    # lastdeleted.save()
    if request.method == 'POST':
        registrations.delete()
        return redirect('adminview')
    context={
        'entries': registrations
    }
    return render(request,'adminview.html',context)

def currenttoken(request):
    current = CurrentToken.objects.last()
    context = {
        'currenttokennum' : current,
    }
    return render(request, 'currenttoken.html',context)

def alumniregistration(request):
    if request.method == "POST":    
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        gr_no = request.POST.get('gr_no')
        branch = request.POST.get('branch')
        passout = request.POST.get('passout')
        query = request.POST.get('query')    

        student_detail = Student(
        name = name,
        email = email,
        gr_no = gr_no,
        branch = branch,
        passout = passout,
        query = query
        )

        student_detail.save()
        return redirect('alumnitoken')
    return render(request, 'alumniregister.html')

def alumniadminview(request):
    registrations = Alumni.objects.all()
    context={
        'entries': registrations
    }
    return render(request,'alumniadminview.html',context)

def alumnitoken(request):
    tokennum = Alumni.objects.last()
    context = {
        'tokenno': tokennum
    }
    return render(request,'alumnitoken.html', context)

def alumnimarkasresolved(request, pk):
    registrations = Alumni.objects.get(pk=pk)
    lastdeleted = AlumniCurrentToken.objects.all()
    lastdeleted.update(token = pk+1) 
    # lastdeleted.save()
    if request.method == 'POST':
        registrations.delete()
        return redirect('alumniadminview')
    context={
        'entries': registrations
    }
    return render(request,'alumniadminview.html',context)

def alumnicurrenttoken(request):
    current = AlumniCurrentToken.objects.last()
    context = {
        'currenttokennum' : current,
    }
    return render(request, 'alumnicurrenttoken.html',context)



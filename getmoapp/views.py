from django.shortcuts import render, redirect
from getmoapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def starterpage(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def doctors(request):
    return render(request,'doctors.html')

def departments(request):
    return render(request,'departments.html')

def Appoint(request):
    if request.method == 'POST':
        my_appointments = appointment1(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
        my_appointments.save()
        return redirect('/show')

    else:
        return render(request,'appointments.html')


def contact(request):
    if request.method == 'POST':
        mycontact = contactform(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        mycontact.save()
        return redirect('/contact')

    else:
        return render(request,'contact.html')


def show(request):
    all = appointment1.objects.all()
    return render(request,'show.html',{'all':all})


def del(request,id):
    deleteappointments = appointment1.objects.get(id=id)
    deleteappointments.delete()
    return redirect('/show')

from django.shortcuts import render
from . models import *
from . forms import *
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def package(request):
    return render(request,'package.html')

def blog(request):
    return render(request,'blog.html')

def branches(request):
    return render(request,'branches.html')

def gallery(request):
    return render(request,'gallery.html')


def executive_package(request):
    return render(request,'executive-package.html')


def ayush_diabetic(request):
    return render(request,'ayush-diabetic.html')


def ayush_gold(request):
    return render(request,'ayush-gold.html')

    
def ayush_silver(request):
    return render(request,'ayush-sliver-plan.html')

    
def ayush_general(request):
    return render(request,'ayush-general.html')

    
def cardiac(request):
    return render(request,'cardiac.html')

    
def executive_package(request):
    return render(request,'executive-package.html')

def gmrl_chambakkara(request):
    return render(request,'gmrl-chambakkara.html')


def gmrl_kolenchery(request):
    return render(request,'gmrl-kolencherry.html')

    
def gmrl_thrippunithura(request):
    return render(request,'gmrl-thrippunithura.html')

    
def gmrl_vadakkekotta(request):
    return render(request,'gmrl-vadakan.html')

  
def moleculor_biology(request):
    return render(request,'molecular.html')

def radiology(request):
    return render(request,'radiology.html')

def test(request):
    return render(request,'test.html')


def department(request):
    return render(request,'department.html')

def index(request):
    context={}
    form=Enquiry_form()

    if request.method=="POST":
        if'save' in request.POST:
            form=Enquiry_form(request.POST)
            form.save()
            messages.success(request,'Enquiry form submitted')


    enquiry=Enquiry.objects.all()
    context['enquiry']=enquiry
    context['form']=form

    return render(request,'index.html')





def contact(request):
    context={}
    form=Contact_form()

    if request.method=="POST":
        if'save' in request.POST:
            form=Contact_form(request.POST)
            form.save()
            messages.success(request,'Message send successfully')
     
    

    contact=Contact.objects.all()
    context['contact']=contact
    context['form']=form
    return render(request,'contact.html',context)

def appointment(request):
    context={}
    form=Appointment_form()

    if request.method=="POST":
        if'save' in request.POST:
         form=Appointment_form(request.POST)
         form.save()
         messages.success(request,'booked  sucessfully')
 





    appointment=Appointment.objects.all()
    context['appointment']=appointment
    context['form']=form
    return render(request,'appointment.html',context)
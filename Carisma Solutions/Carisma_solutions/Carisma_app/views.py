from django.shortcuts import render
from .models import *

# Create your views here.


def loademp(request):
    return render(request,"addemp.html")

def upemp(request):
    return render(request,"updateemp.html")

def delemp(request):
    return render(request,"deleteemp.html")

def seremp(request):
    return render(request,"searchemp.html")

def getemp(request):
    if request.method == "POST":
        try:
            empid = int(request.POST['i'])
            ename = request.POST['n']
            emobile = request.POST['m']
            eemail = request.POST['e']
            edob = request.POST.get('d')  # Corrected line
            
            ed = EmpDetails(Employee_id=empid, Employee_name=ename, Employee_mobile=emobile, Employee_email=eemail, Employee_dob=edob)
            ed.save()
            result = "Data Saved..."
            return render(request, "addemp.html", {'r': result})
        except:
            result = "Data Not Saved..."
            return render(request, "addemp.html", {'r': result})


def updateemp(request):
   if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            emobile = request.POST['m']
            ed = EmpDetails.objects.get(Employee_id=empid)
            ed.Employee_mobile = emobile
            ed.save()
            result="Data updated..."
            return render(request,"updateemp.html",{'r':result})
        except:
            result = "Invalid Id"
            return render(request,"updateemp.html",{'r':result})
        

def deleteemp(request):
    if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            ed = EmpDetails.objects.get(Employee_id=empid)
            ed.delete()
            
            result="Data Deleted..."
            return render(request,"deleteemp.html",{'r':result})
        except:
            result = "Invalid Id"
            return render(request,"deleteemp.html",{'r':result})


def  searchemp(request):
    if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            ed = EmpDetails.objects.get(Employee_id=empid)  
            return render(request,"home.html",{'ei':ed. Employee_id,'en':ed. Employee_name,'em':ed. Employee_mobile,'eemail':ed.Employee_email,'edob':ed.Employee_dob})
        except:
            result = "Invalid Id"
            return render(request,"searchemp.html",{'r':result})

           
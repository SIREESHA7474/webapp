from django.shortcuts import render,redirect
from django .http  import HttpResponse
from .models import Employee
# Create your views here.


def dbprocessing(request):
    return HttpResponse("db app has request")


def insertemployee(request):
    if request.method == 'GET':
        return render(request,'dbapp.html/insert.html')  
    
    if request.method =="POST":
         eno = request.POST.get("eno",0)
         ename = request.POST.get('ename','VCUBE')
         esal = request.POST.get("esal",0)

         #insert into employee values(eno,ename,esal)
         #empobj=Employee(empno=eno,empname=ename,salary=esal)
         #empobj.save()
    try:
         Employee.objects.create(empno=eno,empname=ename,salary=esal)
    except Exception:
         return render(request,"dbapp.html/insert.html",{"msg":"data is failed"})
    return redirect("empselecturl")


def selectemployee(request):
     if request.method == "GET":
          emps=Employee.objects.all() #select * from Employee
          
          return render(request,"dbapp.html/select.html",{'employee':emps})
     


def updateemployee(request,eno):
    if request.method == 'GET':
        emp = Employee.objects.get(empno=eno)
        return render(request,'dbapp.html/update.html',{"employee":emp})
    if request.method == 'POST':
         ename = request.POST['ename']
         esal =  int(request.POST['esal'])
         eobj = Employee(empno=eno,empname=ename,salary=esal)
         eobj.save()
         return redirect('empselecturl')
    

def deleteemployee(request,eno):
     if request.method == "GET":
          emp=Employee.objects.get(empno=eno)
          return render(request,'dbapp.html/delete.html',{'employee':emp})    

     if request.method == "POST":
          emp=Employee.objects.get(empno=eno)
          emp.delete()
          return redirect("empselecturl")



         

     
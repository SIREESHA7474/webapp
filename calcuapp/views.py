from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def addition(request):
    if request.method == "GET":
        return render(request,"calcuapp/addition.html")
    if request.method == "POST":
        v1 = int(request.POST["t1"])
        v2 = int(request.POST["t2"])
        if "add" in request.POST:
            res=v1+v2
            action="addition"
        elif "sub" in request.POST:
            res=v2-v1
            action="sub"
        elif "multi" in request.POST:
            res=v1*v2
            action="multiplication"
        else: 
            res=v2/v1
            action="division"
        return render(request, "calcuapp/addition.html",{"result":res,"action":action})
    
    
    
def mathtable(request):
        if request.method == "GET":
            return render(request,"calcuapp/mtable.html")
        if request.method == "POST":
            num = int(request.POST["t1"])
            output = []
            for i in range(1,11):
                output.append(str(i)+' * '+str(num)+" = "+str(i*num))
            return render(request,"calcuapp/mtable.html",{"table":output})  



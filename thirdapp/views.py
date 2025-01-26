from django.shortcuts import render

# Create your views here.
def sendtemplate(request):
    return render(request,"third.html")
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
def firstview(request):
    res=isinstance(request,HttpRequest)
    print(res)
    print(request.method)
    return HttpResponse("Hello world")
def secondview(request):
    return HttpResponse("HI SIRI")
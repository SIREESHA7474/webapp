from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dbprocessing(request):
    return HttpResponse('DB app has recevied request')

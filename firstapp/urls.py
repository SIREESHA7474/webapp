
from django.urls import path
from . import views 
urlpatterns=[
    path('',views.firstview),
    path("h",views.firstview),
    path("siri/",views.secondview)
]
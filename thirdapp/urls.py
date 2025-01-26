from django.urls import path
from .import views


urlpatterns=[
    path('third',views.sendtemplate ,name="sendtemplate")
]
from django.urls import path
from . import views


urlpatterns= [
    path('',views.dbprocessing),
    path('insert/',views.insertemployee,name="empinserturl"),
    path('select/',views.selectemployee,name='empselecturl'),
    path('modify/<int:eno>/',views.updateemployee,name="empupdateurl"),
    path('delete/<int:eno>/',views.deleteemployee,name="empdeleteurl"),

]

#empselecturl=http:127.0.0.1:8000/db/select/
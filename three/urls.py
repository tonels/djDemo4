from django.conf.urls import url

from three import views

urlpatterns = [
    url('index/',views.index),
    url('getGrade/',views.get_grade),
    url('getStus/',views.get_stus),
]
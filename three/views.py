from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from three.models import Student, Grade


def index(request):
    three_index = loader.get_template("three_index.html")
    result = three_index.render()
    print(result)
    return HttpResponse(result)


def get_grade(request):
    student = Student.objects.get(pk=1)
    grade = student.s_grade
    return HttpResponse("Grade %s" % grade.g_name)


def get_stus(request):
    grade = Grade.objects.get(pk=1)
    students = grade.student_set.all()
    for i in students:
        print(i)

    context={
        "students":students
    }
    return render(request,'three_stu_list.html',context)
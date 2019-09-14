from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import Student


def index(request):
    return HttpResponse("Two  index....")

# 新增
def save(request):
    student = Student()
    student.s_name = 'Jerry'
    student.a_age = 12
    student.save()
    return HttpResponse("添加成功")

# 查询
def getStudents(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    # return HttpResponse("Student list")
    context = {
        "hobby":"play basketball",
        "students":students
    }
    return render(request,"stu_list.html",context)


def update(request):
    student = Student.objects.get(pk=2)
    student.s_name = "Jack"
    student.save()
    return HttpResponse("Update success ... ")


def delete(request):
    student = Student.objects.get(pk=3)
    student.delete()
    return HttpResponse("delete Success..")
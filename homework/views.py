from django.shortcuts import render
from .models import ToMeet

def project (request):
    return render(request, 'homework.html')


def dom (request):
    return render(request, 'dom.html')

def meeting (request):
    todo_list = ToMeet.objects.all()
    return render (request, 'meeting.html', {"todo_list": todo_list})



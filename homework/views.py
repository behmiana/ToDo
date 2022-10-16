from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse

from .models import ToMeet, Habits

def project (request):
    return render(request, 'homework.html')


def dom (request):
    return render(request, 'dom.html')

def meeting (request):
    todo_list = ToMeet.objects.all()
    return render (request, 'meeting1.html', {"todo_list": todo_list})

def add_todos(request):
    f=request.POST
    text=f["tomeet_text"]
    number = f["tomeet_number"]
    comment = f["tomeet_comment"]
    tomeet=ToMeet(
        persone=text,
        phone_number = number,
        comment = comment

    )
    tomeet.save()
    return redirect(meeting)

def habits(request):
    todo_list = Habits.objects.all()
    return render(request,'habits.html', {"todo_list": todo_list})

def add_habits(request):
    f=request.POST
    name=f["habits_text"]
    done = f["habits_done"]
    important = f["habits_important"]
    comment = f["habits_comment"]
    hbs=Habits(
        name=name,
        done_for_today = done,
        important = important,
        comment = comment

    )
    hbs.save()
    return redirect(habits)

def mark_tomeet(request, id):
    tomeet=ToMeet.objects.get(id=id)
    tomeet.is_favorite = not tomeet.is_favorite
    tomeet.save()
    return redirect(meeting)


def delete_tomeet(request, id):
    tomeet=ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(meeting)



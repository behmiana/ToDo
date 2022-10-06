from django.shortcuts import render, HttpResponse,redirect
from .models import todo

def homepage (request):
    todo_list = todo.objects.all()
    return render(request, "index.html", {"todo_list": todo_list})

def test(request):
    return render(request, "test.html")

def check(request):
    return HttpResponse("Control and check")


def add_todo(request):
    f = request.POST
    text= f["todo_text"]
    td=todo(
        text=text
    )
    td.save()
    return redirect(homepage)

def delete_todo(request, id):
    td=todo.objects.get(id=id)
    td.delete()
    return redirect(homepage)

def mark_todo(request, id):
    td=todo.objects.get(id=id)
    td.is_favorite = True
    td.save()
    return redirect(homepage)

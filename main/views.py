from django.shortcuts import render, HttpResponse
from .models import todo

def homepage (request):
    todo_list = todo.objects.all()
    return render(request, "index.html", {"todo_list": todo_list})

def test(request):
    return render(request, "test.html")

def check(request):
    return HttpResponse("Control and check")
# Create your views here.

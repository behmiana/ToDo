from django.shortcuts import render

def project (request):
    return render(request, 'homework.html')


def dom (request):
    return render(request, 'dom.html')



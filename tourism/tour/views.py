from django.shortcuts import render
from django.http import HttpResponse


def tourism(request):
    return render(request,'tourism.html')

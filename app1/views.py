from django.shortcuts import render


def fun(request):
    return render(request,'front/home.html')

# Create your views here.

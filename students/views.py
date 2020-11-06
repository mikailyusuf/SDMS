from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'students/login.html')


def signup(request):
    return render(request, 'students/register.html')

def home(request):
    return render(request, 'students/home.html')
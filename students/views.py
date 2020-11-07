from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from students.forms import CreateUserForm
from students.models import Teachers


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(request.POST['password1'])
            print(request.POST['email'])
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            Teachers.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            print(user)
            print(username + "User Registered")
    context = {'form': form}
    return render(request, 'students/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'students/login.html')


def signout(request):
    logout(request)
    return HttpResponseRedirect('login')


def home(request):
    return render(request, 'students/home.html')


def createUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = createUser(request)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            group = Group.objects.get(name='teachers')
            user.groups.add(group)
        # Teachers.objects.create(
        # user = user,first_name = )

from django.contrib.auth.models import Group
from django.shortcuts import render


# Create your views here.
from students.forms import CreateUserForm
from students.models import Teachers


def login(request):
    return render(request, 'students/login.html')


def signup(request):
    return render(request, 'students/register.html')

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
        Teachers.objects.create(
        user = user,first_name =
        )
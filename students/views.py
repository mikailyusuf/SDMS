from django.contrib.auth.models import Group
from django.shortcuts import render


# Create your views here.
from students.forms import CreateUserForm
from students.models import Teachers


def login(request):
    return render(request, 'students/login.html')


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

    # print(request)
    # print(request.email)
    # print(request.idnumber)
    # print(request.password)
    # print(request.contact)
    context = {'form': form}
    return render(request, 'students/register.html',context)

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
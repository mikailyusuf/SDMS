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


def studentRecord(request):
    if request.method == 'POST':
        maths_test = request.POST['maths_test']
        maths_exam = request.POST['maths_exam']
        session = request.POST['session']
        term = request.POST['term']
        eng_test = request.POST['eng_test']
        eng_exam = request.POST['eng_exam']
        bio_test = request.POST['bio_test']
        bio_exam = request.POST['bio_exam']
        chem_test = request.POST['chem_test']
        chem_exam = request.POST['chem_exam']
        civic_test = request.POST['civic_test']
        civic_exam = request.POST['civic_exam']
        agric_test = request.POST['agric_test']
        agric_exam = request.POST['agric_exam']
        phy_test = request.POST['phy_test']
        phy_exam = request.POST['phy_exam']
        comment = request.POST['comment']

        print(" Session :" + session)
        print("Term :" + term)
        print( "Maths :" + maths_test +":" + maths_exam)
        print( "English :" + eng_test +":" + eng_exam)
        print( "Physics :" + phy_test +":" + phy_exam)
        print( "Biology :" + bio_test +":" + bio_exam)
        print( "Chemistry :" + chem_test +":" + chem_exam)
        print( "Civic Education :" + civic_test +":" + civic_exam)
        print( "Agric :" + agric_test +":" + agric_exam)
        print( "Comment :" + comment )


    return render(request, 'students/StudentRecord.html')

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


def calculateTotal(test,exam):
    total = test+exam
    return total

def grade(total):
    if total >= 70:
        grade = 'A'
    elif total >= 60:
        grade = 'B'
    elif total >= 50:
        grade = 'C'
    elif total >= 45:
        grade = 'D'
    else:
        grade = 'F'
    return grade

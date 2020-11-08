from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from students.filters import StudentsFilter
from students.forms import CreateUserForm, CreateResult
from students.models import Teachers, Results, Students


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
    form = CreateResult
    if request.method == 'POST':
        maths_test = request.POST['maths_test']
        maths_exam = request.POST['maths_exam']
        maths_total = calculateTotal(maths_test, maths_exam)
        maths_grade = grade(maths_total)
        exam_session = request.POST['session']
        exam_term = request.POST['term']
        eng_test = request.POST['eng_test']
        eng_exam = request.POST['eng_exam']
        eng_total = calculateTotal(eng_test, eng_exam)
        eng_grade = grade(eng_total)
        bio_test = request.POST['bio_test']
        bio_exam = request.POST['bio_exam']
        bio_total = calculateTotal(bio_test, bio_exam)
        bio_grade = grade(bio_total)
        chem_test = request.POST['chem_test']
        chem_exam = request.POST['chem_exam']
        chem_total = calculateTotal(chem_test, chem_exam)
        chem_grade = grade(chem_total)
        civic_test = request.POST['civic_test']
        civic_exam = request.POST['civic_exam']
        civic_total = calculateTotal(civic_test, civic_exam)
        civic_grade = grade(civic_total)
        agric_test = request.POST['agric_test']
        agric_exam = request.POST['agric_exam']
        agric_total = calculateTotal(agric_test, agric_exam)
        agric_grade = grade(agric_total)
        phy_test = request.POST['phy_test']
        phy_exam = request.POST['phy_exam']
        phy_total = calculateTotal(phy_test, phy_exam)
        phy_grade = grade(phy_total)
        comment = request.POST['comment']

        Results.objects.create(
            session=exam_session, term=exam_term,
            math_exam=maths_exam, math_test=maths_test, math_total=maths_total, math_grade=maths_grade,
            eng_exam=eng_exam, eng_test=eng_test, eng_total=eng_total, eng_grade=eng_grade,
            bio_test=bio_test, bio_grade=bio_grade, bio_exam=bio_exam, bio_total=bio_total,
            chem_test=chem_test, chem_exam=chem_exam, chem_total=chem_total, chem_grade=chem_grade,
            physics_test=phy_test, physics_exam=phy_exam, physics_total=phy_total, physics_grade=phy_grade,
            civic_test=civic_test, civic_exam=civic_exam, civic_total=civic_total, civic_grade=civic_grade,
            comment=comment,
            agric_test=agric_test, agric_exam=agric_exam, agric_total=agric_total, agric_grade=agric_grade,

        )

        # print(" Session :" + session)
        # print("Term :" + term)
        # print( "Maths :" + maths_test +":" + maths_exam)
        # print( "English :" + eng_test +":" + eng_exam)
        # print( "Physics :" + phy_test +":" + phy_exam)
        # print( "Biology :" + bio_test +":" + bio_exam)
        # print( "Chemistry :" + chem_test +":" + chem_exam)
        # print( "Civic Education :" + civic_test +":" + civic_exam)
        # print( "Agric :" + agric_test +":" + agric_exam)
        # print( "Comment :" + comment )

    context = {'form': form}

    return render(request, 'students/StudentRecord.html', context)


def filterStudents(request):
    f = StudentsFilter(request.GET, queryset=Students.objects.all())
    return render(request, 'students/students.html', {'filter': f})


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


def calculateTotal(test, exam):
    total = int(test) + int(exam)
    return total


def grade(t):
    total = int(t)
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

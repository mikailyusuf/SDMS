from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginPage,name='login'),
    path('', views.loginPage,name='login'),
    path('signup/', views.signup,name = 'signup'),
    path('home/', views.home,name = 'home'),
    path('signout', views.signout,name = 'signout'),
    path('record', views.studentRecord,name = 'record'),
    path('search', views.StudentsFilter,name = 'search'),

]

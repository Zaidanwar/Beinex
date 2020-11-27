
from django.urls import path,include
from myapp.views import *

urlpatterns = [

    path('',Home.as_view(),name="home"),
path('login/',Login.as_view(),name="login"),
path('register/',Register.as_view(),name="register"),
path('mainhome/',Mainhome.as_view(),name="mainhome"),
path('addemployees/',AddEmployee.as_view(),name="addemployees"),
path('viewemployees/',ViewEmployee.as_view(),name="viewemployees"),
]
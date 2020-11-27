# from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from myapp.models import *

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'homepage.html')


class Register(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self, request):
        data = request.POST
        username = data['username']
        password = data['pass']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('/login/')
class Login(View):
    def get(self,request):
        return render(request,'login.html')


    def post(self,request):

        data=request.POST
        user1=data['username']
        passwrd=data['pass']


        ruser = authenticate(request, username=user1, password=passwrd)
        if ruser is not None:
            login(request, ruser)
            return redirect('/mainhome/')

        else:
            messages.warning(request, 'User does not exist/ Password incorrect.')
            return HttpResponseRedirect(reverse('login'))


class Mainhome(View):
    def get(self,request):
        return render(request,'mainhome.html')

class AddEmployee(View):
    def get(self,request):
        return render(request,'addemployee.html')
    def post(self,request):
        data=request.POST
        name = data["name"]
        image= request.FILES["image"]
        phone = data["phone"]
        address=data["address"]

        emp=Employee(Employee_Name=name,Image=image,phone_no=phone,address=address)
        emp.save()
        return redirect('/mainhome')

class ViewEmployee(View):
    def get(self,request):

        emp = Employee.objects.all()


        return render(request, 'viewemployees.html', {'emp': emp})
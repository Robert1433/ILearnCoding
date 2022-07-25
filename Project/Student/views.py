from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .models import *
from Teacher import models as modelsteach
from .forms import  *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login/")
def studenthome(request):
	return render(request,"Student/homestudent.html")


def authfstudent(request):
		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password1',None)
		user = authenticate(request, username = username, password = password, email = email)
		if user is not None:
			login(request,user)
			return redirect('settings')	
		else:
				form = RegisterStudent(request.POST)
				if form.is_valid():
					user = form.save()			
					login(request,user)
					usermodel = User.objects.get(username=username)
					newprofile = Student.objects.create(user= usermodel,user_id = usermodel.id)
					newprofile.save()
					return redirect('settings')
				else:
					form = RegisterStudent()
					return render(request,'register/loginasstudent.html',{"form":form})					

	
def Logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url="/login/")
def displaycourseasstudent(request):
	lessons =modelsteach.Courses.objects.all()
	return render(request,"Student/displaycourseasstudent.html",{'lessons':lessons})


@login_required(login_url="/login/")
def settings(request):
	UserProfile = Student.objects.get(user=request.user)
	if request.method == 'POST':	
		email = request.POST['email']
		preferences = request.POST['preferences']
		bio = request.POST['bio']
		tip = request.POST['tip']
		UserProfile.email = email
		UserProfile.preference = preferences
		UserProfile.biograpghy = bio
		UserProfile.utype = tip
		UserProfile.save()
		if UserProfile.utype == 'Student':
			return redirect('studenthome')
	return render(request,'register/settingsstudent.html',{'user_profile':UserProfile})


@login_required(login_url="/login/")	
def ctutorial2(request):
	return render(request, 'tutoriale/c2++.html')


@login_required(login_url="/login/")	
def python2(request):
	return render(request,'tutoriale/python2.html')


@login_required(login_url="/login/")		
def java2(request):
	return render(request,'tutoriale/java2.html')	


@login_required(login_url="/login/")
def library(request):
	return render(request,'tutoriale/biblioteca.html')


@login_required(login_url="/login/")
def editor(request):
	return render(request,'tutoriale/compiler.html')

	
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .models import *
from Teacher import models as modelsteach
from .forms import  *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def authfteacher(request):
		username = request.POST.get('username',None)
		email = request.POST.get('email',None)
		password = request.POST.get('password1',None)
		user = authenticate(request, username = username, password = password, email = email)
		if user is not None:
			login(request,user)
			return redirect('settingsasteacher')	
		else:
				form = RegisterTeacher(request.POST)
				if form.is_valid():
					user = form.save()			
					login(request,user)
					usermodel = User.objects.get(username=username)
					newprofile = Teacher.objects.create(user= usermodel,user_id = usermodel.id)
					newprofile.save()
					return redirect('settingsasteacher')
				else:
					form = RegisterTeacher()
					return render(request,'register/loginasteacher.html',{"form":form})					
	
def Logout(request):
    logout(request)
    return redirect('home')
@login_required(login_url="/login/")
def hometeacher(request):
    return render(request,'Teacher/hometeach.html')

@login_required(login_url="/login/")
def settingsasteacher(request):
	UserProfile = Teacher.objects.get(user=request.user)
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
		if UserProfile.utype == 'Teacher':
			return redirect('hometeacher')
	return render(request,'register/settingsteacher.html',{'user_profile':UserProfile})

@login_required(login_url="/login/")
def addcoursesasteacher(request):
	if request.method == 'POST':
		user = request.user.username 
		imag = request.FILES.get('imag')
		text  = request.POST['text']
		video = request.FILES.get('video')
		document = request.FILES.get('document')
		newcourse = Courses.objects.create(prof_user = user, imag = imag, text = text,video = video,document = document)
		newcourse.save()
		return redirect('displaycourseasteacher')
	return render(request,"Teacher/addlesson.html")
@login_required(login_url="/login/")
def displaycourseasteacher(request):
	lessons = modelsteach.Courses.objects.all()
	return render(request,"Teacher/displaycourseasteacher.html",{'lessons':lessons})

@login_required(login_url="/login/")	
def ctutorial(request):
	return render(request, 'tutoriale/c++.html')
@login_required(login_url="/login/")	
def python(request):
	return render(request,'tutoriale/python.html')
@login_required(login_url="/login/")		
def java(request):
	return render(request,'tutoriale/java.html')	
@login_required(login_url="/login/")
def library(request):
	return render(request,'tutoriale/biblioteca.html')
@login_required(login_url="/login/")
def editor(request):
	return render(request,'tutoriale/compiler.html')

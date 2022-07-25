from django.urls import path

from . import views as vw

urlpatterns = [
	path('studenthome/',vw.studenthome,name='studenthome'),
	path('authfstudent/',vw.authfstudent,name='authfstudent'),
	path('settings/',vw.settings,name='settings'),
	path('displaycourseasstudent/',vw.displaycourseasstudent,name='displaycourseasstudent'),
	
	path('c++/',vw.ctutorial2,name='ctutorial2'),
	path('python/',vw.python2,name='python2'),
	path('java/',vw.java2,name='java2'),
	path('library/',vw.library,name='library'),
	path('editor/',vw.editor,name='editor'),

]
 
from django.urls import path

from . import views as vw

urlpatterns = [
	path('teacherhome/',vw.hometeacher,name='hometeacher'),
	path('authfteacher/',vw.authfteacher,name='authfteacher'),
	path('Logout/',vw.Logout,name = "Logout"),
	path('settingsasteacher/',vw.settingsasteacher,name="settingsasteacher"),
	path('displaycourseasteacher/',vw.displaycourseasteacher,name="displaycourseasteacher"),
	path('addcoursesasteacher/',vw.addcoursesasteacher,name="addcoursesasteacher"),
	path('c++/',vw.ctutorial,name='ctutorial'),
	path('python/',vw.python,name='python'),
	path('java/',vw.java,name='java'),
	path('library/',vw.library,name='library'),
	path('editor/',vw.editor,name='editor'),

]
 
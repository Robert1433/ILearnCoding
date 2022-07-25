from django.urls import path

from . import views as vw

urlpatterns = [
	path('',vw.home,name='home'),
	path('chat/',vw.chathome,name = "chathome"),
	path('<str:room>/', vw.room, name='room'),
    path('checkview', vw.checkview, name='checkview'),
    path('send', vw.send, name='send'),
    path('getMessages/<str:room>/', vw.getMessages, name='getMessages'),
]

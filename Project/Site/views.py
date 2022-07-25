from django.shortcuts import render,redirect
from django.http import Http404
from .models import *
from .forms import  *
from django.contrib.auth.models import User
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.http import  JsonResponse,HttpResponse




def home(request):
	return render(request,"home.html",{})
 

@login_required(login_url="/login/")
def chathome(request):
	return render(request,"rooms/rhome.html")


@login_required(login_url="/login/")
def room(request, room):
    username = request.GET.get('username')
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        raise Http404    
    return render(request, 'rooms/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

@login_required(login_url="/login/")
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

@login_required(login_url="/login/")
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

@login_required(login_url="/login/")
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
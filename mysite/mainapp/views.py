from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
#from json


def index(request):
    return render(request, "mainapp/index.html")

def create_room(request):
        if request.method == 'POST':
            if request.POST.get('name'):
                room=Room()
                #generate id=name
                room.name= request.POST.get('name')

                #add intialuser
                users = [request.POST.get('name')]
                users = str(users).replace("'",'') #porsiaca lo vi en un tuto xd
                room.users = json.loads(users)
                room.save()
                
                return render(request, 'mainapp/lobby.html')  

        else:
                return render(request,'posts/error.html')

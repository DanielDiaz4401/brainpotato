from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Room
import json
import random
@csrf_exempt


def index(request):
    return render(request, "mainapp/index.html")

def create_room(request):
        if request.method == 'POST':
            if request.POST.get('name'):
                room=Room()

                #initialize all variables with json
                room.users ={"users":[]}
                room.users = str(room.users).replace("'",'"') #just in case

                room.points ={"points":[]}
                room.points = str(room.points).replace("'",'"') #just in case

                room.inpu_words ={"inpu_words":[]}
                room.inpu_words = str(room.inpu_words).replace("'",'"') #just in case

                room.word_bag ={"word_bag":[]}
                room.word_bag = str(room.word_bag).replace("'",'"') #just in case

                room.game_words ={"game_words":[]}
                room.game_words = str(room.game_words).replace("'",'"') #just in case

                room.chains ={"chains":[]}
                room.chains = str(room.chains).replace("'",'"') #just in case

                #generate id=name
                result=""
                for i in range(0,4):
                    generated=random.randint(0,34)
                    if generated<=25:
                        generated=chr(generated+65)
                    else:
                        generated=chr(generated-25+48)
                    result=result+generated
                room.name = result

                #add first player
                users ={"users":[request.POST.get('name')]}
                users = eval(str(users).replace("'",'"')) #molt necessari omaigad
                room.users = str(users)
                room.save()
                
                request.session['roomName'] = room.name
                return redirect(lobby) 

        else:
            return render(request,'posts/error.html')

def lobby(request):
    rumi = Room.objects.get(name = request.session['roomName'])
    context= eval(rumi.users)
    print(context)
    return render(request, 'mainapp/lobby.html',context) 

def join_room(request):
    if request.method == 'POST':
        print(request.POST.getlist("user"))
        if request.POST.getlist('gameid'):
            rumi = Room.objects.get(name = request.POST.get('gameid'))
            #users = json.loads(rumi.users)
            print(request.POST.getlist('username[]'))
        return redirect(lobby) 
            
    else:
        return render(request,'mas/error.html')

@csrf_exempt
def wordinput(request):
    print(request.body)
    return render(request,'mainapp/wordinput.html')

@csrf_exempt
def game(request):
    return render(request, 'mainapp/game.html')
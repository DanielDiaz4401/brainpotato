from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200) #simple id string
    users = models.TextField(default="") #list of user  names
    phase = models.CharField(max_length=200) #creation, wordinput,playing,user_eval,nextRound?,finished
    
    #rondadata 
    idn = models.CharField#1,2,3,4,5... should be an int but meh need to go faaast it crashed with integer
    points = models.TextField(default="") #list of points of each user
    inpu_words = models.TextField(default="")  #list of lists of inputted words
    word_bag = models.TextField(default="")  #list of all words
    game_words = models.TextField(default="")  #list of 2nlist with start and finish words
    chains = models.TextField(default="") #list of user created chain

        


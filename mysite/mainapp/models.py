from django.db import models
from jsonfield import JSONField
from django.shortcuts import redirect

class Round(models.Model):
    idd = models.IntegerField()#1,2,3,4,5...
    status = models.CharField(max_length=200) #pregame, ingame, finished
    points = JSONField() #list of points of each user
    inpu_words = JSONField() #list of lists of inputted words
    word_bag = JSONField() #list of all words
    game_words = JSONField() #list of 2nlist with start and finish words
    chains = JSONField() #list of user created chain

class Room(models.Model):
    name = models.CharField(max_length=200) #simple id string
    users = JSONField() #list of user  names
    inpu_words = JSONField() #list of lists of words
    phase = models.CharField(max_length=200) #creation, wordinput,playing,user_eval,nextRound?,finished
    #rounds = Round() #array of rounds


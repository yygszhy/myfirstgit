from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from random import shuffle
import math
from math import factorial as fact
import numpy as np
from scipy import stats
# This Python file uses the following encoding: utf-8
import os, sys
from array import *
from decimal import *
# from tkinter import *
import csv
import ast


author = 'Feibai'

doc = """
Confidence Study1b sweepstakes
"""


class Constants(BaseConstants):
    name_in_url = 'Confidence_study1b_ss'
    players_per_group = None
    showupfee = 10
    num_rounds = 1
    num_problemsets = 10
    mmacolor = 'lightblue'
    mmbcolor = 'orange'

    # yoking - corresponding column number in csvfile， Study 1A - realized sampling data for all subjects; 1-to-1 matching
    # get the variables' names
    code = 'participant.code' # study1a, participant code
    samplea1 = 'player.realsamplea1' # study1a, player.realsamplea1 - Column 27 in csv - this is a python list
    sampleb1 = 'player.realsampleb1' # study1a, player.realsampleb1 - Column 28 in csv
    proba1 = 'player.realproba1'  # study1a, player.realproba1 - Column 29 in csv
    probb1 = 'player.realprobb1' # study1a, player.realprobb1 - Column 30 in csv
    amounta1 = 'player.realamounta1' # study1a, player.realamounta1 - Column 31 in csv
    amountb1 = 'player.realamountb1' # study1a, player.realamountb1
    bo1 = 'player.bo1' # study1a, player.bo1

    samplea2 = 'player.realsamplea2'
    sampleb2 = 'player.realsampleb2'
    proba2 = 'player.realproba2'
    probb2 = 'player.realprobb2'
    amounta2 = 'player.realamounta2'
    amountb2 = 'player.realamountb2'
    bo2 = 'player.bo2'

    samplea3 = 'player.realsamplea3'
    sampleb3 = 'player.realsampleb3'
    proba3 = 'player.realproba3'
    probb3 = 'player.realprobb3'
    amounta3 = 'player.realamounta3'
    amountb3 = 'player.realamountb3'
    bo3 = 'player.bo3'

    samplea4 = 'player.realsamplea4'
    sampleb4 = 'player.realsampleb4'
    proba4 = 'player.realproba4'
    probb4 = 'player.realprobb4'
    amounta4 = 'player.realamounta4'
    amountb4 = 'player.realamountb4'
    bo4 = 'player.bo4'

    samplea5 = 'player.realsamplea5'
    sampleb5 = 'player.realsampleb5'
    proba5 = 'player.realproba5'
    probb5 = 'player.realprobb5'
    amounta5 = 'player.realamounta5'
    amountb5 = 'player.realamountb5'
    bo5 = 'player.bo5'

    samplea6 = 'player.realsamplea6'
    sampleb6 = 'player.realsampleb6'
    proba6 = 'player.realproba6'
    probb6 = 'player.realprobb6'
    amounta6 = 'player.realamounta6'
    amountb6 = 'player.realamountb6'
    bo6 = 'player.bo6'

    samplea7 = 'player.realsamplea7'
    sampleb7 = 'player.realsampleb7'
    proba7 = 'player.realproba7'
    probb7 = 'player.realprobb7'
    amounta7 = 'player.realamounta7'
    amountb7 = 'player.realamountb7'
    bo7 = 'player.bo7'

    samplea8 = 'player.realsamplea8'
    sampleb8 = 'player.realsampleb8'
    proba8 = 'player.realproba8'
    probb8 = 'player.realprobb8'
    amounta8 = 'player.realamounta8'
    amountb8 = 'player.realamountb8'
    bo8 = 'player.bo8'

    samplea9 = 'player.realsamplea9'
    sampleb9 = 'player.realsampleb9'
    proba9 = 'player.realproba9'
    probb9 = 'player.realprobb9'
    amounta9 = 'player.realamounta9'
    amountb9 = 'player.realamountb9'
    bo9 = 'player.bo9'

    samplea10 = 'player.realsamplea10'
    sampleb10 = 'player.realsampleb10'
    proba10 = 'player.realproba10'
    probb10 = 'player.realprobb10'
    amounta10 = 'player.realamounta10'
    amountb10 = 'player.realamountb10'
    bo10 = 'player.bo10'


class Subsession(BaseSubsession):
    def creating_session(self):
        with open('yoking/yoking.csv', 'r') as csvfile:
        # 'r' only read the file
        # create reader object
            storereader = csv.reader(csvfile, delimiter=',')
        # get the first row of variable names from csv file
            headers = next(storereader)
        # read row
            addrow = []
            for row in storereader:
            # create list x list object
                addrow.append(row)
            j = 0
            for p in self.get_players():
                # set participant.vars "yokinglist" for each player
                # each player get one row by looping
                # number of players have to be smaller or equal to number of players in study1a and yoking conditions
                # yokinglist is a dictionary which includes the first row in csv file (the variable names)
                # and the other row in csv file (the corresponding data for that variable)
                p.participant.vars['yokinglist'] = dict(zip(headers, addrow[j]))
                j = j + 1




class Group(BaseGroup):

    #num_players = models.IntegerField(doc="number of players")

    #def get_num_players(self):
     #   self.num_players = self.session.config['num_players']

    # winner = models.IntegerField(
    #     doc="one player is chosen by sweepstakes")
    # # self.get_players() = [<Player 1>, <Player 2>, <Player 3>, <Player 4>, <Player 5>, <Player 6>, <Player 7>, <Player 8>, <Player 9>, <Player 10>]
    # # all payoffs have to be positive. can't have negative payoff.
    # def sweepstakes(self):
    #     if self.session.config['sweepstakes'] == 1:
    #         stake0 = []
    #         # add up all points earned by all players
    #         group = sum(float(p.payoff) for p in self.get_players())
    #         # get number of the players
    #         num_players = len(self.get_players())
    #         # num_players = self.session.config['num_players']
    #         # get total points of all players (i.e. all points earned + base pay)
    #         groupsum = group + Constants.showupfee * num_players
    #         # for each player, his stake = his points (earned + base pay) / total points of all players
    #         stake0.append(((float(p.payoff) + Constants.showupfee)/groupsum) for p in self.get_players())
    #         # put all individual stakes as a list of probabilities of being drawn. e.g. (0.1, 0.2, 0.3, 0.2, 0.2)
    #         stake = [list(float(y) for y in x) for x in stake0][0]
    #         # draw one number from 1 to number of players (python list starts from 0, that's why +1), based on the list of probabilities
    #         # list of probabilities corresponds to the stake of each individual
    #         self.winner = np.random.choice(np.arange(1, num_players+1), p=stake)
    #     else:
    #         self.winner = 999
    pass


class Player(BasePlayer):


    # randomly assign one problem set for payoff

    def random():
        return random.randint(1, 10)

    randompayoff = models.IntegerField(default = random)

    # yoking
    yoking = models.CharField (doc = "yoked participant code in Study_1a")

    # get which participant in Study_1a is yoked in Study_1b,1c and 1d
    def getyoked(self):
        yokinglist = self.participant.vars['yokinglist']
        # get the column participant code from csv file.
        self.yoking = yokinglist.get(Constants.code)

    amounta1 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a1")
    amountb1 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b1")
    proba1 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a1")
    probb1 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b1")
    proboptiona1u = models.CharField(doc="choice-set specific, mma1 probabilities for upper line in text")
    proboptiona1d = models.CharField(doc="choice-set specific, mma1 probabilities for lower line in text")
    proboptionb1u = models.CharField(doc="choice-set specific, mmb1 probabilities for upper line in text")
    proboptionb1d = models.CharField(doc="choice-set specific, mmb1 probabilities for lower line in text")
    bo1 = models.FloatField(doc = "bad outcome in pair 1")
    mm1 = models.BooleanField(doc = "which money machine button in pair 1 was clicked: 1=machine A; 0=machine B")

    amounta2 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a2")
    amountb2 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b2")
    proba2 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a2")
    probb2 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b2")
    proboptiona2u = models.CharField(doc="choice-set specific, mma2 probabilities for upper line in text")
    proboptiona2d = models.CharField(doc="choice-set specific, mma2 probabilities for lower line in text")
    proboptionb2u = models.CharField(doc="choice-set specific, mmb2 probabilities for upper line in text")
    proboptionb2d = models.CharField(doc="choice-set specific, mmb2 probabilities for lower line in text")
    bo2 = models.FloatField(doc = "bad outcome in pair 2")
    mm2 = models.BooleanField(doc = "which money machine button in pair 2 was clicked: 1=machine A; 0=machine B")


    amounta3 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a3")
    amountb3 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b3")
    proba3 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a3")
    probb3 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b3")
    proboptiona3u = models.CharField(doc="choice-set specific, mma3 probabilities for upper line in text")
    proboptiona3d = models.CharField(doc="choice-set specific, mma3 probabilities for lower line in text")
    proboptionb3u = models.CharField(doc="choice-set specific, mmb3 probabilities for upper line in text")
    proboptionb3d = models.CharField(doc="choice-set specific, mmb3 probabilities for lower line in text")
    bo3 = models.FloatField(doc = "bad outcome in pair 3")
    mm3 = models.BooleanField(doc = "which money machine button in pair 3 was clicked: 1=machine A; 0=machine B")


    amounta4 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a4")
    amountb4 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b4")
    proba4 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a4")
    probb4 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b4")
    proboptiona4u = models.CharField(doc="choice-set specific, mma4 probabilities for upper line in text")
    proboptiona4d = models.CharField(doc="choice-set specific, mma4 probabilities for lower line in text")
    proboptionb4u = models.CharField(doc="choice-set specific, mmb4 probabilities for upper line in text")
    proboptionb4d = models.CharField(doc="choice-set specific, mmb4 probabilities for lower line in text")
    bo4 = models.FloatField(doc = "bad outcome in pair 4")
    mm4 = models.BooleanField(doc = "which money machine button in pair 4 was clicked: 1=machine A; 0=machine B")

    amounta5 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a5")
    amountb5 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b5")
    proba5 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a5")
    probb5 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b5")
    proboptiona5u = models.CharField(doc="choice-set specific, mma5 probabilities for upper line in text")
    proboptiona5d = models.CharField(doc="choice-set specific, mma5 probabilities for lower line in text")
    proboptionb5u = models.CharField(doc="choice-set specific, mmb5 probabilities for upper line in text")
    proboptionb5d = models.CharField(doc="choice-set specific, mmb5 probabilities for lower line in text")
    bo5 = models.FloatField(doc = "bad outcome in pair 5")
    mm5 = models.BooleanField(doc = "which money machine button in pair 5 was clicked: 1=machine A; 0=machine B")

    amounta6 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a6")
    amountb6 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b6")
    proba6 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a6")
    probb6 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b6")
    proboptiona6u = models.CharField(doc="choice-set specific, mma6 probabilities for upper line in text")
    proboptiona6d = models.CharField(doc="choice-set specific, mma6 probabilities for lower line in text")
    proboptionb6u = models.CharField(doc="choice-set specific, mmb6 probabilities for upper line in text")
    proboptionb6d = models.CharField(doc="choice-set specific, mmb6 probabilities for lower line in text")
    bo6 = models.FloatField(doc = "bad outcome in pair 6")
    mm6 = models.BooleanField(doc = "which money machine button in pair 6 was clicked: 1=machine A; 0=machine B")

    amounta7 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a7")
    amountb7 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b7")
    proba7 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a7")
    probb7 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b7")
    proboptiona7u = models.CharField(doc="choice-set specific, mma7 probabilities for upper line in text")
    proboptiona7d = models.CharField(doc="choice-set specific, mma7 probabilities for lower line in text")
    proboptionb7u = models.CharField(doc="choice-set specific, mmb7 probabilities for upper line in text")
    proboptionb7d = models.CharField(doc="choice-set specific, mmb7 probabilities for lower line in text")
    bo7 = models.FloatField(doc = "bad outcome in pair 7")
    mm7 = models.BooleanField(doc = "which money machine button in pair 7 was clicked: 1=machine A; 0=machine B")

    amounta8 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a8")
    amountb8 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b8")
    proba8 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a8")
    probb8 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b8")
    proboptiona8u = models.CharField(doc="choice-set specific, mma8 probabilities for upper line in text")
    proboptiona8d = models.CharField(doc="choice-set specific, mma8 probabilities for lower line in text")
    proboptionb8u = models.CharField(doc="choice-set specific, mmb8 probabilities for upper line in text")
    proboptionb8d = models.CharField(doc="choice-set specific, mmb8 probabilities for lower line in text")
    bo8 = models.FloatField(doc = "bad outcome in pair 8")
    mm8 = models.BooleanField(doc = "which money machine button in pair 8 was clicked: 1=machine A; 0=machine B")

    amounta9 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a9")
    amountb9 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b9")
    proba9 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a9")
    probb9 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b9")
    proboptiona9u = models.CharField(doc="choice-set specific, mma9 probabilities for upper line in text")
    proboptiona9d = models.CharField(doc="choice-set specific, mma9 probabilities for lower line in text")
    proboptionb9u = models.CharField(doc="choice-set specific, mmb9 probabilities for upper line in text")
    proboptionb9d = models.CharField(doc="choice-set specific, mmb9 probabilities for lower line in text")
    bo9 = models.FloatField(doc = "bad outcome in pair 9")
    mm9 = models.BooleanField(doc = "which money machine button in pair 9 was clicked: 1=machine A; 0=machine B")

    amounta10 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a10")
    amountb10 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b10")
    proba10 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a10")
    probb10 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b10")
    proboptiona10u = models.CharField(doc="choice-set specific, mma10 probabilities for upper line in text")
    proboptiona10d = models.CharField(doc="choice-set specific, mma10 probabilities for lower line in text")
    proboptionb10u = models.CharField(doc="choice-set specific, mmb10 probabilities for upper line in text")
    proboptionb10d = models.CharField(doc="choice-set specific, mmb10 probabilities for lower line in text")
    bo10 = models.FloatField(doc = "bad outcome in pair 10")
    mm10 = models.BooleanField(doc = "which money machine button in pair 10 was clicked: 1=machine A; 0=machine B")


    # get bad outcome for each pair of money machines

    def getbo(self):
        # get yokinglist from participant.vars
        yokinglist = self.participant.vars['yokinglist']

        # Plan B, without directly yoking bad outcome variable, we can get bad outcome by the smallest value in the combination of samples
        # ast.literal_eval: Safely evaluate an expression node or a string containing a Python literal or container display.

        # combine list samplea1 and sampleb1 into one list
        # sample1 = ast.literal_eval(yokinglist[Constants.samplea1]) + ast.literal_eval(yokinglist[Constants.sampleb1])

        # find the smallest value in the list of samplea1 and sampleb1 - the bad outcome
        # self.bo1 = min(int(i) for i in sample1)

        # problem: if bad outcome was not in the realized samples

        # Now directly get bad outcomes from study 1a csv file
        self.bo1 = ast.literal_eval(yokinglist.get(Constants.bo1))
        self.bo2 = ast.literal_eval(yokinglist.get(Constants.bo2))
        self.bo3 = ast.literal_eval(yokinglist.get(Constants.bo3))
        self.bo4 = ast.literal_eval(yokinglist.get(Constants.bo4))
        self.bo5 = ast.literal_eval(yokinglist.get(Constants.bo5))
        self.bo6 = ast.literal_eval(yokinglist.get(Constants.bo6))
        self.bo7 = ast.literal_eval(yokinglist.get(Constants.bo7))
        self.bo8 = ast.literal_eval(yokinglist.get(Constants.bo8))
        self.bo9 = ast.literal_eval(yokinglist.get(Constants.bo9))
        self.bo10 = ast.literal_eval(yokinglist.get(Constants.bo10))

    # Attributes of money machine pairs based on yoking study 1a

    def getmoneymachine1(self):
        yokinglist = self.participant.vars['yokinglist']
        # from the yokinglist, get the element of amounta1, element number defined in Constants
        self.amounta1 = yokinglist.get(Constants.amounta1)
        self.amountb1 = yokinglist.get(Constants.amountb1)
        # from yokinglist, get original probability, define Machine A or B is certain/uncertain
        probb1 = ast.literal_eval(yokinglist.get(Constants.probb1))
        # ast.literal_eval: Safely evaluate an expression node or a string containing a Python literal or container display.
        samplea1 = ast.literal_eval(yokinglist.get(Constants.samplea1))
        sampleb1 = ast.literal_eval(yokinglist.get(Constants.sampleb1))
        if probb1 == 1.0: # define which money machine has uncertain outcomes
            if self.bo1 < 0: # when €0 is not the bad outcome with probability p2
                # calculate the yoking probabality from realized sample draw in Study 1a
                p1 = round(samplea1.count(str(round(self.bo1))) / len(samplea1), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona1u = str(round(p1 * 100)) + '%'
                self.proboptiona1d = str(round(p2 * 100)) + '%'
                self.proboptionb1u = '100%'
                self.proboptionb1d = '0%'
                self.proba1 = p1
                self.probb1 = 1.0
            else: # when €0 is the bad outcome with probability p1
                p1 = round(samplea1.count(str(round(self.bo1))) / len(samplea1), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona1u = str(round(p2 * 100)) + '%'
                self.proboptiona1d = str(round(p1 * 100)) + '%'
                self.proboptionb1u = '100%'
                self.proboptionb1d = '0%'
                self.proba1 = p2
                self.probb1 = 1.0
        else:
            if self.bo1 < 0:
                p1 = round(sampleb1.count(str(round(self.bo1))) / len(sampleb1), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb1u = str(round(p1 * 100)) + '%'
                self.proboptionb1d = str(round(p2 * 100)) + '%'
                self.proboptiona1u = '100%'
                self.proboptiona1d = '0%'
                self.proba1 = 1.0
                self.probb1 = p1
            else:
                p1 = round(sampleb1.count(str(round(self.bo1))) / len(sampleb1), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb1u = str(round(p2 * 100)) + '%'
                self.proboptionb1d = str(round(p1 * 100)) + '%'
                self.proboptiona1u = '100%'
                self.proboptiona1d = '0%'
                self.proba1 = 1.0
                self.probb1 = p2


    def getmoneymachine2(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta2 = yokinglist.get(Constants.amounta2)
        self.amountb2 = yokinglist.get(Constants.amountb2)
        probb2 = ast.literal_eval(yokinglist.get(Constants.probb2))
        samplea2 = ast.literal_eval(yokinglist.get(Constants.samplea2))
        sampleb2 = ast.literal_eval(yokinglist.get(Constants.sampleb2))
        if probb2 == 1.0:# define which money machine has uncertain outcomes
            if self.bo2 < 0: # when €0 is not the bad outcome with probability p2
                p1 = round(samplea2.count(str(round(self.bo2))) / len(samplea2), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona2u = str(round(p1 * 100)) + '%'
                self.proboptiona2d = str(round(p2 * 100)) + '%'
                self.proboptionb2u = '100%'
                self.proboptionb2d = '0%'
                self.proba2 = p1
                self.probb2 = 1.0
            else: # when €0 is the bad outcome with probability p1
                p1 = round(samplea2.count(str(round(self.bo2))) / len(samplea2), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona2u = str(round(p2 * 100)) + '%'
                self.proboptiona2d = str(round(p1 * 100)) + '%'
                self.proboptionb2u = '100%'
                self.proboptionb2d = '0%'
                self.proba2 = p2
                self.probb2 = 1.0
        else:
            if self.bo2 < 0:
                p1 = round(sampleb2.count(str(round(self.bo2))) / len(sampleb2), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb2u = str(round(p1 * 100)) + '%'
                self.proboptionb2d = str(round(p2 * 100)) + '%'
                self.proboptiona2u = '100%'
                self.proboptiona2d = '0%'
                self.probb2 = p1
                self.proba2 = 1.0
            else:
                p1 = round(sampleb2.count(str(round(self.bo2))) / len(sampleb2), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb2u = str(round(p2 * 100)) + '%'
                self.proboptionb2d = str(round(p1 * 100)) + '%'
                self.proboptiona2u = '100%'
                self.proboptiona2d = '0%'
                self.probb2 = p2
                self.proba2 = 1.0


    def getmoneymachine3(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta3 = yokinglist.get(Constants.amounta3)
        self.amountb3 = yokinglist.get(Constants.amountb3)
        probb3 = ast.literal_eval(yokinglist.get(Constants.probb3))
        samplea3 = ast.literal_eval(yokinglist.get(Constants.samplea3))
        sampleb3 = ast.literal_eval(yokinglist.get(Constants.sampleb3))
        if probb3 == 1.0:# define which money machine has uncertain outcomes
            if self.bo3 < 0: # when €0 is not the bad outcome with probability p2
                p1 = round(samplea3.count(str(round(self.bo3))) / len(samplea3), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona3u = str(round(p1 * 100)) + '%'
                self.proboptiona3d = str(round(p2 * 100)) + '%'
                self.proboptionb3u = '100%'
                self.proboptionb3d = '0%'
                self.proba3 = p1
                self.probb3 = 1.0
            else: # when €0 is the bad outcome with probability p1
                p1 = round(samplea3.count(str(round(self.bo3))) / len(samplea3), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona3u = str(round(p2 * 100)) + '%'
                self.proboptiona3d = str(round(p1 * 100)) + '%'
                self.proboptionb3u = '100%'
                self.proboptionb3d = '0%'
                self.proba3 = p2
                self.probb3 = 1.0
        else:
            if self.bo3 < 0:
                p1 = round(sampleb3.count(str(round(self.bo3))) / len(sampleb3), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb3u = str(round(p1 * 100)) + '%'
                self.proboptionb3d = str(round(p2 * 100)) + '%'
                self.proboptiona3u = '100%'
                self.proboptiona3d = '0%'
                self.probb3 = p1
                self.proba3 = 1.0
            else:
                p1 = round(sampleb3.count(str(round(self.bo3))) / len(sampleb3), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb3u = str(round(p2 * 100)) + '%'
                self.proboptionb3d = str(round(p1 * 100)) + '%'
                self.proboptiona3u = '100%'
                self.proboptiona3d = '0%'
                self.probb3 = p2
                self.proba3 = 1.0

    def getmoneymachine4(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta4 = yokinglist.get(Constants.amounta4)
        self.amountb4 = yokinglist.get(Constants.amountb4)
        probb4 = ast.literal_eval(yokinglist.get(Constants.probb4))
        samplea4 = ast.literal_eval(yokinglist.get(Constants.samplea4))
        sampleb4 = ast.literal_eval(yokinglist.get(Constants.sampleb4))
        if probb4 == 1.0: # define which money machine has uncertain outcomes
            if self.bo4 < 0:  # when €0 is not the bad outcome with probability p2
                p1 = round(samplea4.count(str(round(self.bo4))) / len(samplea4), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona4u = str(round(p1 * 100)) + '%'
                self.proboptiona4d = str(round(p2 * 100)) + '%'
                self.proboptionb4u = '100%'
                self.proboptionb4d = '0%'
                self.proba4 = p1
                self.probb4 = 1.0
            else: # when €0 is the bad outcome with probability p1
                p1 = round(samplea4.count(str(round(self.bo1))) / len(samplea4), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona4u = str(round(p2 * 100)) + '%'
                self.proboptiona4d = str(round(p1 * 100)) + '%'
                self.proboptionb4u = '100%'
                self.proboptionb4d = '0%'
                self.probb4 = 1.0
                self.proba4 = p2
        else:
            if self.bo4 < 0:
                p1 = round(sampleb4.count(str(round(self.bo4))) / len(sampleb4), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb4u = str(round(p1 * 100)) + '%'
                self.proboptionb4d = str(round(p2 * 100)) + '%'
                self.proboptiona4u = '100%'
                self.proboptiona4d = '0%'
                self.probb4 = p1
                self.proba4 = 1.0
            else:
                p1 = round(sampleb4.count(str(round(self.bo4))) / len(sampleb4), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb4u = str(round(p2 * 100)) + '%'
                self.proboptionb4d = str(round(p1 * 100)) + '%'
                self.proboptiona4u = '100%'
                self.proboptiona4d = '0%'
                self.probb4 = p2
                self.proba4 = 1.0

    def getmoneymachine5(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta5 = yokinglist.get(Constants.amounta5)
        self.amountb5 = yokinglist.get(Constants.amountb5)
        probb5 = ast.literal_eval(yokinglist.get(Constants.probb5))
        samplea5 = ast.literal_eval(yokinglist.get(Constants.samplea5))
        sampleb5 = ast.literal_eval(yokinglist.get(Constants.sampleb5))
        if probb5 == 1.0: # define which money machine has uncertain outcomes
            if self.bo5 < 0:  # when €0 is not the bad outcome with probability p2
                p1 = round(samplea5.count(str(round(self.bo5))) / len(samplea5), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona5u = str(round(p1 * 100)) + '%'
                self.proboptiona5d = str(round(p2 * 100)) + '%'
                self.proboptionb5u = '100%'
                self.proboptionb5d = '0%'
                self.proba5 = p1
                self.probb5 = 1.0
            else: # when €0 is the bad outcome with probability p1
                p1 = round(samplea5.count(str(round(self.bo5))) / len(samplea5), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona5u = str(round(p2 * 100)) + '%'
                self.proboptiona5d = str(round(p1 * 100)) + '%'
                self.proboptionb5u = '100%'
                self.proboptionb5d = '0%'
                self.proba5 = p2
                self.probb5 = 1.0
        else:
            if self.bo5 < 0:
                p1 = round(sampleb5.count(str(round(self.bo5))) / len(sampleb5), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb5u = str(round(p1 * 100)) + '%'
                self.proboptionb5d = str(round(p2 * 100)) + '%'
                self.proboptiona5u = '100%'
                self.proboptiona5d = '0%'
                self.probb5 = p1
                self.proba5 = 1.0
            else:
                p1 = round(sampleb5.count(str(round(self.bo5))) / len(sampleb5), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb5u = str(round(p2 * 100)) + '%'
                self.proboptionb5d = str(round(p1 * 100)) + '%'
                self.proboptiona5u = '100%'
                self.proboptiona5d = '0%'
                self.probb5 = p2
                self.proba5 = 1.0

    def getmoneymachine6(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta6 = yokinglist.get(Constants.amounta6)
        self.amountb6 = yokinglist.get(Constants.amountb6)
        probb6 = ast.literal_eval(yokinglist.get(Constants.probb6))
        samplea6 = ast.literal_eval(yokinglist.get(Constants.samplea6))
        sampleb6 = ast.literal_eval(yokinglist.get(Constants.sampleb6))
        if probb6 == 1.0: # define which money machine has uncertain outcomes
            if self.bo6 < 0: # when €0 is not the bad outcome with probability p2
                p1 = round(samplea6.count(str(round(self.bo6))) / len(samplea6), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona6u = str(round(p1 * 100)) + '%'
                self.proboptiona6d = str(round(p2 * 100)) + '%'
                self.proboptionb6u = '100%'
                self.proboptionb6d = '0%'
                self.proba6 = p1
                self.probb6 = 1.0
            else: # when €0 is the bad outcome with probability p1
                p1 = round(samplea6.count(str(round(self.bo6))) / len(samplea6), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona6u = str(round(p2 * 100)) + '%'
                self.proboptiona6d = str(round(p1 * 100)) + '%'
                self.proboptionb6u = '100%'
                self.proboptionb6d = '0%'
                self.proba6 = p2
                self.probb6 = 1.0
        else:
            if self.bo6 < 0:
                p1 = round(sampleb6.count(str(round(self.bo6))) / len(sampleb6), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb6u = str(round(p1 * 100)) + '%'
                self.proboptionb6d = str(round(p2 * 100)) + '%'
                self.proboptiona6u = '100%'
                self.proboptiona6d = '0%'
                self.probb6 = p1
                self.proba6 = 1.0
            else:
                p1 = round(sampleb6.count(str(round(self.bo6))) / len(sampleb6), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb6u = str(round(p2 * 100)) + '%'
                self.proboptionb6d = str(round(p1 * 100)) + '%'
                self.proboptiona6u = '100%'
                self.proboptiona6d = '0%'
                self.proba6 = p2
                self.probb6 = 1.0

    def getmoneymachine7(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta7 = yokinglist.get(Constants.amounta7)
        self.amountb7 = yokinglist.get(Constants.amountb7)
        probb7 = ast.literal_eval(yokinglist.get(Constants.probb7))
        samplea7 = ast.literal_eval(yokinglist.get(Constants.samplea7))
        sampleb7 = ast.literal_eval(yokinglist.get(Constants.sampleb7))
        if probb7 == 1.0: # define which money machine has uncertain outcomes
            if self.bo7 < 0: # when €0 is not the bad outcome with probability p2
                p1 = round(samplea7.count(str(round(self.bo7))) / len(samplea7), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb7u = '100%'
                self.proboptionb7d = '0%'
                self.probb7 = 1.0
                self.proba7 = p1
                self.proboptiona7u = str(round(p1 * 100)) + '%'
                self.proboptiona7d = str(round(p2 * 100)) + '%'

            else:# when €0 is the bad outcome with probability p1
                p1 = round(samplea7.count(str(round(self.bo7))) / len(samplea7), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb7u = '100%'
                self.proboptionb7d = '0%'
                self.probb7 = 1.0
                self.proba7 = p2
                self.proboptiona7u = str(round(p2 * 100)) + '%'
                self.proboptiona7d = str(round(p1 * 100)) + '%'
        else:
            if self.bo7 < 0:
                p1 = round(sampleb7.count(str(round(self.bo7))) / len(sampleb7), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona7u = '100%'
                self.proboptiona7d = '0%'
                self.proba7 = 1.0
                self.probb7 = p1
                self.proboptionb7u = str(round(p1 * 100)) + '%'
                self.proboptionb7d = str(round(p2 * 100)) + '%'
            else:
                p1 = round(sampleb7.count(str(round(self.bo7))) / len(sampleb7), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona7u = '100%'
                self.proboptiona7d = '0%'
                self.proba7 = 1.0
                self.probb7 = p2
                self.proboptionb7u = str(round(p2 * 100)) + '%'
                self.proboptionb7d = str(round(p1 * 100)) + '%'


    def getmoneymachine8(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta8 = yokinglist.get(Constants.amounta8)
        self.amountb8 = yokinglist.get(Constants.amountb8)
        probb8 = ast.literal_eval(yokinglist.get(Constants.probb8))
        samplea8 = ast.literal_eval(yokinglist.get(Constants.samplea8))
        sampleb8 = ast.literal_eval(yokinglist.get(Constants.sampleb8))
        if probb8 == 1.0: # define which money machine has uncertain outcomes
            if self.bo8 < 0: # when €0 is not the bad outcome with probability p2
                p1 = round(samplea8.count(str(round(self.bo8))) / len(samplea8), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona8u = str(round(p1 * 100)) + '%'
                self.proboptiona8d = str(round(p2 * 100)) + '%'
                self.proboptionb8u = '100%'
                self.proboptionb8d = '0%'
                self.proba8 = p1
                self.probb8 = 1.0
            else:# when €0 is the bad outcome with probability p1
                p1 = round(samplea8.count(str(round(self.bo8))) / len(samplea8), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona8u = str(round(p2 * 100)) + '%'
                self.proboptiona8d = str(round(p1 * 100)) + '%'
                self.proboptionb8u = '100%'
                self.proboptionb8d = '0%'
                self.proba8 = p2
                self.probb8 = 1.0
        else:
            if self.bo8 < 0:
                p1 = round(sampleb8.count(str(round(self.bo8))) / len(sampleb8), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb8u = str(round(p1 * 100)) + '%'
                self.proboptionb8d = str(round(p2 * 100)) + '%'
                self.proboptiona8u = '100%'
                self.proboptiona8d = '0%'
                self.probb8 = p1
                self.proba8 = 1.0
            else:
                p1 = round(sampleb8.count(str(round(self.bo8))) / len(sampleb8), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb8u = str(round(p2 * 100)) + '%'
                self.proboptionb8d = str(round(p1 * 100)) + '%'
                self.proboptiona8u = '100%'
                self.proboptiona8d = '0%'
                self.probb8 = p2
                self.proba8 = 1.0

    def getmoneymachine9(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta9 = yokinglist.get(Constants.amounta9)
        self.amountb9 = yokinglist.get(Constants.amountb9)
        probb9 = ast.literal_eval(yokinglist.get(Constants.probb9))
        samplea9 = ast.literal_eval(yokinglist.get(Constants.samplea9))
        sampleb9 = ast.literal_eval(yokinglist.get(Constants.sampleb9))
        if probb9 == 1.0: # define which money machine has uncertain outcomes
            if self.bo9 < 0: # when €0 is not the bad outcome with probability p2
                p1 = round(samplea9.count(str(round(self.bo9))) / len(samplea9), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona9u = str(round(p1 * 100)) + '%'
                self.proboptiona9d = str(round(p2 * 100)) + '%'
                self.proboptionb9u = '100%'
                self.proboptionb9d = '0%'
                self.proba9 = p1
                self.probb9 = 1.0
            else:# when €0 is the bad outcome with probability p1
                p1 = round(samplea9.count(str(round(self.bo9))) / len(samplea9), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona9u = str(round(p2 * 100)) + '%'
                self.proboptiona9d = str(round(p1 * 100)) + '%'
                self.proboptionb9u = '100%'
                self.proboptionb9d = '0%'
                self.proba9 = p2
                self.probb9 = 1.0
        else:
            if self.bo9 < 0:
                p1 = round(sampleb9.count(str(round(self.bo9))) / len(sampleb9), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb9u = str(round(p1 * 100)) + '%'
                self.proboptionb9d = str(round(p2 * 100)) + '%'
                self.proboptiona9u = '100%'
                self.proboptiona9d = '0%'
                self.probb9 = p1
                self.proba9 = 1.0
            else:
                p1 = round(sampleb9.count(str(round(self.bo9))) / len(sampleb9), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb9u = str(round(p2 * 100)) + '%'
                self.proboptionb9d = str(round(p1 * 100)) + '%'
                self.proboptiona9u = '100%'
                self.proboptiona9d = '0%'
                self.probb9 = p2
                self.proba9 = 1.0


    def getmoneymachine10(self):
        yokinglist = self.participant.vars['yokinglist']
        self.amounta10 = yokinglist.get(Constants.amounta10)
        self.amountb10 = yokinglist.get(Constants.amountb10)
        probb10 = ast.literal_eval(yokinglist.get(Constants.probb10))
        samplea10 = ast.literal_eval(yokinglist.get(Constants.samplea10))
        sampleb10 = ast.literal_eval(yokinglist.get(Constants.sampleb10))
        if probb10 == 1.0: # define which money machine has uncertain outcomes
            if self.bo10 < 0: # when €0 is not the bad outcome with probability p2
                p1 = round(samplea10.count(str(round(self.bo10))) / len(samplea10), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona10u = str(round(p1 * 100)) + '%'
                self.proboptiona10d = str(round(p2 * 100)) + '%'
                self.proboptionb10u = '100%'
                self.proboptionb10d = '0%'
                self.proba10 = p1
                self.probb10 = 1.0
            else: # when €0 is the bad outcome with probability p1
                p1 = round(samplea10.count(str(round(self.bo10))) / len(samplea10), 2)
                p2 = round(1 - p1, 2)
                self.proboptiona10u = str(round(p2 * 100)) + '%'
                self.proboptiona10d = str(round(p1 * 100)) + '%'
                self.proboptionb10u = '100%'
                self.proboptionb10d = '0%'
                self.proba10 = p2
                self.probb10 = 1.0
        else:
            if self.bo10 < 0:
                p1 = round(sampleb10.count(str(round(self.bo10))) / len(sampleb10), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb10u = str(round(p1 * 100)) + '%'
                self.proboptionb10d = str(round(p2 * 100)) + '%'
                self.proboptiona10u = '100%'
                self.proboptiona10d = '0%'
                self.probb10 = p1
                self.proba10 = 1.0
            else:
                p1 = round(sampleb10.count(str(round(self.bo10))) / len(sampleb10), 2)
                p2 = round(1 - p1, 2)
                self.proboptionb10u = str(round(p2 * 100)) + '%'
                self.proboptionb10d = str(round(p1 * 100)) + '%'
                self.proboptiona10u = '100%'
                self.proboptiona10d = '0%'
                self.probb10 = p2
                self.proba10 = 1.0

   # Choices chosen for the confirm page for each problem set

    def choice1(self):
        if self.mm1 == 1:
            return 'A'
        else:
            return 'B'

    def choice2(self):
        if self.mm2 == 1:
            return 'A'
        else:
            return 'B'

    def choice3(self):
        if self.mm3 == 1:
            return 'A'
        else:
            return 'B'

    def choice4(self):
        if self.mm4 == 1:
            return 'A'
        else:
            return 'B'

    def choice5(self):
        if self.mm5 == 1:
            return 'A'
        else:
            return 'B'

    def choice6(self):
        if self.mm6 == 1:
            return 'A'
        else:
            return 'B'

    def choice7(self):
        if self.mm7 == 1:
            return 'A'
        else:
            return 'B'

    def choice8(self):
        if self.mm8 == 1:
            return 'A'
        else:
            return 'B'

    def choice9(self):
        if self.mm9 == 1:
            return 'A'
        else:
            return 'B'

    def choice10(self):
        if self.mm10 == 1:
            return 'A'
        else:
            return 'B'

    # problem set choice - which color, which probability, which outcome chosen
    # color

    def opacitya1(self):
        if self.mm1 == 1:
            return 1
        return 0.2

    def opacityb1(self):
        if self.mm1 == 1:
            return 0.2
        return 1

    def opacitya2(self):
        if self.mm2 == 1:
            return 1
        return 0.2

    def opacityb2(self):
        if self.mm2 == 1:
            return 0.2
        return 1

    def opacitya3(self):
        if self.mm3 == 1:
            return 1
        return 0.2

    def opacityb3(self):
        if self.mm3 == 1:
            return 0.2
        return 1

    def opacitya4(self):
        if self.mm4 == 1:
            return 1
        return 0.2

    def opacityb4(self):
        if self.mm4 == 1:
            return 0.2
        return 1

    def opacitya5(self):
        if self.mm5 == 1:
            return 1
        return 0.2

    def opacityb5(self):
        if self.mm5 == 1:
            return 0.2
        return 1

    def opacitya6(self):
        if self.mm6 == 1:
            return 1
        return 0.2

    def opacityb6(self):
        if self.mm6 == 1:
            return 0.2
        return 1

    def opacitya7(self):
        if self.mm7 == 1:
            return 1
        return 0.2

    def opacityb7(self):
        if self.mm7 == 1:
            return 0.2
        return 1

    def opacitya8(self):
        if self.mm8 == 1:
            return 1
        return 0.2

    def opacityb8(self):
        if self.mm8 == 1:
            return 0.2
        return 1

    def opacitya9(self):
        if self.mm9 == 1:
            return 1
        return 0.2

    def opacityb9(self):
        if self.mm9 == 1:
            return 0.2
        return 1

    def opacitya10(self):
        if self.mm10 == 1:
            return 1
        return 0.2

    def opacityb10(self):
        if self.mm10 == 1:
            return 0.2
        return 1



    # amount for sample draw
    def amount1(self):
        if self.mm1 == 1:
            return self.amounta1
        return self.amountb1

    def amount2(self):
        if self.mm2 == 1:
            return self.amounta2
        return self.amountb2

    def amount3(self):
        if self.mm3 == 1:
            return self.amounta3
        return self.amountb3

    def amount4(self):
        if self.mm4 == 1:
            return self.amounta4
        return self.amountb4

    def amount5(self):
        if self.mm5 == 1:
            return self.amounta5
        return self.amountb5

    def amount6(self):
        if self.mm6 == 1:
            return self.amounta6
        return self.amountb6

    def amount7(self):
        if self.mm7 == 1:
            return self.amounta7
        return self.amountb7

    def amount8(self):
        if self.mm8 == 1:
            return self.amounta8
        return self.amountb8

    def amount9(self):
        if self.mm9 == 1:
            return self.amounta9
        return self.amountb9

    def amount10(self):
        if self.mm10 == 1:
            return self.amounta10
        return self.amountb10

    # probabilities for sample draw
    def prob1(self):
        if self.mm1 == 1:
            return self.proba1
        return self.probb1

    def prob2(self):
        if self.mm2 == 1:
            return self.proba2
        return self.probb2

    def prob3(self):
        if self.mm3 == 1:
            return self.proba3
        return self.probb3

    def prob4(self):
        if self.mm4 == 1:
            return self.proba4
        return self.probb4

    def prob5(self):
        if self.mm5 == 1:
            return self.proba5
        return self.probb5

    def prob6(self):
        if self.mm6 == 1:
            return self.proba6
        return self.probb6

    def prob7(self):
        if self.mm7 == 1:
            return self.proba7
        return self.probb7

    def prob8(self):
        if self.mm8 == 1:
            return self.proba8
        return self.probb8

    def prob9(self):
        if self.mm9 == 1:
            return self.proba9
        return self.probb9

    def prob10(self):
        if self.mm10 == 1:
            return self.proba10
        return self.probb10

    # probabilities

    def choice11prob(self):
        if self.mm1 == 1:
            return self.proboptiona1
        return self.proboptionb1

    def choice12prob(self):
        if self.mm2 == 1:
            return self.proboptiona2
        return self.proboptionb2

    def choice13prob(self):
        if self.mm3 == 1:
            return self.proboptiona3
        return self.proboptionb3

    def choice14prob(self):
        if self.mm4 == 1:
            return self.proboptiona4
        return self.proboptionb4

    def choice15prob(self):
        if self.mm5 == 1:
            return self.proboptiona5
        return self.proboptionb5

    def choice16prob(self):
        if self.mm6 == 1:
            return self.proboptiona6
        return self.proboptionb6

    def choice17prob(self):
        if self.mm7 == 1:
            return self.proboptiona7
        return self.proboptionb7

    def choice18prob(self):
        if self.mm8 == 1:
            return self.proboptiona8
        return self.proboptionb8

    def choice19prob(self):
        if self.mm9 == 1:
            return self.proboptiona9
        return self.proboptionb9

    def choice110prob(self):
        if self.mm10 == 1:
            return self.proboptiona10
        return self.proboptionb10


    # which money machine for payoff
    def payoffpair(self):
        if self.randompayoff == 1:
            return "Pair 1"
        elif self.randompayoff == 2:
            return "Pair 2"
        elif self.randompayoff == 3:
            return "Pair 3"
        elif self.randompayoff == 4:
            return "Pair 4"
        elif self.randompayoff == 5:
            return "Pair 5"
        elif self.randompayoff == 6:
            return "Pair 6"
        elif self.randompayoff == 7:
            return "Pair 7"
        elif self.randompayoff == 8:
            return "Pair 8"
        elif self.randompayoff == 9:
            return "Pair 9"
        return "Pair 10"


    def payoffpairaorb(self):
        if self.randompayoff == 1:
            return self.choice1()
        elif self.randompayoff == 2:
            return self.choice2()
        elif self.randompayoff == 3:
            return self.choice3()
        elif self.randompayoff == 4:
            return self.choice4()
        elif self.randompayoff == 5:
            return self.choice5()
        elif self.randompayoff == 6:
            return self.choice6()
        elif self.randompayoff == 7:
            return self.choice7()
        elif self.randompayoff == 8:
            return self.choice8()
        elif self.randompayoff == 9:
            return self.choice9()
        return self.choice10()

    def payoffopacitya(self):
        if self.randompayoff == 1:
            return self.opacitya1()
        elif self.randompayoff == 2:
            return self.opacitya2()
        elif self.randompayoff == 3:
            return self.opacitya3()
        elif self.randompayoff == 4:
            return self.opacitya4()
        elif self.randompayoff == 5:
            return self.opacitya5()
        elif self.randompayoff == 6:
            return self.opacitya6()
        elif self.randompayoff == 7:
            return self.opacitya7()
        elif self.randompayoff == 8:
            return self.opacitya8()
        elif self.randompayoff == 9:
            return self.opacitya9()
        return self.opacitya10()

    def payoffopacityb(self):
        if self.randompayoff == 1:
            return self.opacityb1()
        elif self.randompayoff == 2:
            return self.opacityb2()
        elif self.randompayoff == 3:
            return self.opacityb3()
        elif self.randompayoff == 4:
            return self.opacityb4()
        elif self.randompayoff == 5:
            return self.opacityb5()
        elif self.randompayoff == 6:
            return self.opacityb6()
        elif self.randompayoff == 7:
            return self.opacityb7()
        elif self.randompayoff == 8:
            return self.opacityb8()
        elif self.randompayoff == 9:
            return self.opacityb9()
        return self.opacityb10()

    def payoffeuroa(self):
        if self.randompayoff == 1:
            return self.optiona1
        elif self.randompayoff == 2:
            return self.optiona2
        elif self.randompayoff == 3:
            return self.optiona3
        elif self.randompayoff == 4:
            return self.optiona4
        elif self.randompayoff == 5:
            return self.optiona5
        elif self.randompayoff == 6:
            return self.optiona6
        elif self.randompayoff == 7:
            return self.optiona7
        elif self.randompayoff == 8:
            return self.optiona8
        elif self.randompayoff == 9:
            return self.optiona9
        return self.optiona10

    def payoffeurob(self):
        if self.randompayoff == 1:
            return self.optionb1
        elif self.randompayoff == 2:
            return self.optionb2
        elif self.randompayoff == 3:
            return self.optionb3
        elif self.randompayoff == 4:
            return self.optionb4
        elif self.randompayoff == 5:
            return self.optionb5
        elif self.randompayoff == 6:
            return self.optionb6
        elif self.randompayoff == 7:
            return self.optionb7
        elif self.randompayoff == 8:
            return self.optionb8
        elif self.randompayoff == 9:
            return self.optionb9
        return self.optionb10

    def payoffproba(self):
        if self.randompayoff == 1:
            return self.proboptiona1
        elif self.randompayoff == 2:
            return self.proboptiona2
        elif self.randompayoff == 3:
            return self.proboptiona3
        elif self.randompayoff == 4:
            return self.proboptiona4
        elif self.randompayoff == 5:
            return self.proboptiona5
        elif self.randompayoff == 6:
            return self.proboptiona6
        elif self.randompayoff == 7:
            return self.proboptiona7
        elif self.randompayoff == 8:
            return self.proboptiona8
        elif self.randompayoff == 9:
            return self.proboptiona9
        return self.proboptiona10

    def payoffprobb(self):
        if self.randompayoff == 1:
            return self.proboptionb1
        elif self.randompayoff == 2:
            return self.proboptionb2
        elif self.randompayoff == 3:
            return self.proboptionb3
        elif self.randompayoff == 4:
            return self.proboptionb4
        elif self.randompayoff == 5:
            return self.proboptionb5
        elif self.randompayoff == 6:
            return self.proboptionb6
        elif self.randompayoff == 7:
            return self.proboptionb7
        elif self.randompayoff == 8:
            return self.proboptionb8
        elif self.randompayoff == 9:
            return self.proboptionb9
        return self.proboptionb10

    # def payoffeuro(self):
    #     if self.randompayoff == 1:
    #         return self.choice11euro()
    #     elif self.randompayoff == 2:
    #         return self.choice12euro()
    #     elif self.randompayoff == 3:
    #         return self.choice13euro()
    #     elif self.randompayoff == 4:
    #         return self.choice14euro()
    #     elif self.randompayoff == 5:
    #         return self.choice15euro()
    #     elif self.randompayoff == 6:
    #         return self.choice16euro()
    #     elif self.randompayoff == 7:
    #         return self.choice17euro()
    #     elif self.randompayoff == 8:
    #         return self.choice18euro()
    #     elif self.randompayoff == 9:
    #         return self.choice19euro()
    #     return self.choice110euro()

    def payoffprob(self):
        if self.randompayoff == 1:
            return self.choice11prob()
        elif self.randompayoff == 2:
            return self.choice12prob()
        elif self.randompayoff == 3:
            return self.choice13prob()
        elif self.randompayoff == 4:
            return self.choice14prob()
        elif self.randompayoff == 5:
            return self.choice15prob()
        elif self.randompayoff == 6:
            return self.choice16prob()
        elif self.randompayoff == 7:
            return self.choice17prob()
        elif self.randompayoff == 8:
            return self.choice18prob()
        elif self.randompayoff == 9:
            return self.choice19prob()
        return self.choice110prob()

    # find parameters of the distribution from payoff money machine to draw a sample
    def ps(self):
        if self.randompayoff == 1:
            return self.prob1()
        elif self.randompayoff == 2:
            return self.prob2()
        elif self.randompayoff == 3:
            return self.prob3()
        elif self.randompayoff == 4:
            return self.prob4()
        elif self.randompayoff == 5:
            return self.prob5()
        elif self.randompayoff == 6:
            return self.prob6()
        elif self.randompayoff == 7:
            return self.prob7()
        elif self.randompayoff == 8:
            return self.prob8()
        elif self.randompayoff == 9:
            return self.prob9()
        return self.prob10()

    def playmm(self):
        yokinglist = self.participant.vars['yokinglist']
        realproba1 = float(yokinglist.get(Constants.proba1))
        realproba2 = float(yokinglist.get(Constants.proba2))
        realproba3 = float(yokinglist.get(Constants.proba3))
        realproba4 = float(yokinglist.get(Constants.proba4))
        realproba5 = float(yokinglist.get(Constants.proba5))
        realproba6 = float(yokinglist.get(Constants.proba6))
        realproba7 = float(yokinglist.get(Constants.proba7))
        realproba8 = float(yokinglist.get(Constants.proba8))
        realproba9 = float(yokinglist.get(Constants.proba9))
        realproba10 = float(yokinglist.get(Constants.proba10))
        realprobb1 = float(yokinglist.get(Constants.probb1))
        realprobb2 = float(yokinglist.get(Constants.probb2))
        realprobb3 = float(yokinglist.get(Constants.probb3))
        realprobb4 = float(yokinglist.get(Constants.probb4))
        realprobb5 = float(yokinglist.get(Constants.probb5))
        realprobb6 = float(yokinglist.get(Constants.probb6))
        realprobb7 = float(yokinglist.get(Constants.probb7))
        realprobb8 = float(yokinglist.get(Constants.probb8))
        realprobb9 = float(yokinglist.get(Constants.probb9))
        realprobb10 = float(yokinglist.get(Constants.probb10))
        if self.randompayoff == 1:
            if self.mm1 == 1:
                playprob = realproba1
            else:
                playprob = realprobb1
        elif self.randompayoff == 2:
            if self.mm2 == 1:
                playprob = realproba2
            else:
                playprob = realprobb2
        elif self.randompayoff == 3:
            if self.mm3 == 1:
                playprob = realproba3
            else:
                playprob = realprobb3
        elif self.randompayoff == 4:
            if self.mm4 == 1:
                playprob = realproba4
            else:
                playprob = realprobb4
        elif self.randompayoff == 5:
            if self.mm5 == 1:
                playprob = realproba5
            else:
                playprob = realprobb5
        elif self.randompayoff == 6:
            if self.mm6 == 1:
                playprob = realproba6
            else:
                playprob = realprobb6
        elif self.randompayoff == 7:
            if self.mm7 == 1:
                playprob = realproba7
            else:
                playprob = realprobb7
        elif self.randompayoff == 8:
            if self.mm8 == 1:
                playprob = realproba8
            else:
                playprob = realprobb8
        elif self.randompayoff == 9:
            if self.mm9 == 1:
                playprob = realproba9
            else:
                playprob = realprobb9
        else:
            if self.mm10 == 1:
                playprob = realproba10
            else:
                playprob = realprobb10
        if playprob < 1:
            return 1
        return 0


    def amount(self):
        if self.randompayoff == 1:
            return self.amount1()
        elif self.randompayoff == 2:
            return self.amount2()
        elif self.randompayoff == 3:
            return self.amount3()
        elif self.randompayoff == 4:
            return self.amount4()
        elif self.randompayoff == 5:
            return self.amount5()
        elif self.randompayoff == 6:
            return self.amount6()
        elif self.randompayoff == 7:
            return self.amount7()
        elif self.randompayoff == 8:
            return self.amount8()
        elif self.randompayoff == 9:
            return self.amount9()
        return self.amount10()

    # randomly draw a sample from binary distribution defined by payoff parameters


    def set_payoffs(self):
        self.payoff = int(self.amount() * np.random.binomial(1, self.ps()))
        self.participant.vars['sweepstake'] = round(int(self.payoff + Constants.showupfee))



    # define information fields for subjects

    gender = models.CharField(
        choices=['Male', 'Female'],
        widget=widgets.RadioSelect()
    )
    age = models.PositiveIntegerField()


    def sswin(self):
        if self.id_in_group == self.group.winner:
            return 1
        else:
            return 0

    # to filter out the players who are not connected
    active = models.BooleanField(doc='real player=true', initial=False)

    def setactive(self):
        self.active = True

    def checkactive(self):
        if self.active == True:
            self.participant.vars['active'] = 1
        else:
            self.participant.vars['active'] = 0


    pass

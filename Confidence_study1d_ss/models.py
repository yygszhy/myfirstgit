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
from scipy.stats import beta
# import matplotlib.pyplot as plt
import simplejson as json
import csv
import ast

author = 'Feibai'

doc = """
Confidence Study1d Classroom
"""


class Constants(BaseConstants):
    name_in_url = 'Confidence_study1d_ss'
    players_per_group = None
    num_rounds = 1
    showupfee = 10
    num_problemsets = 10
    mmacolor = 'lightblue'
    mmbcolor = 'orange'
    text_a_uncertain = 'Here you see sample outcomes for Points Machine A.'
    text_a_certain = 'Points Machine A has one possible outcome only, always'
    text_b_uncertain = 'Here you see sample outcomes for Points Machine B.'
    text_b_certain = 'Points Machine B has one possible outcome only, always'


    # below numbers are yoked from Study 1A - realized sampling data for all subjects; 1-to-1 matching
    # yoking
    # mma_i = Confidence_study1a.1.player.realamounta_i
    # mmb_i = Confidence_study1a.1.player.realamountb_i
    # samplesizea_i = Confidence_study1a.1.player.clicksmma_i
    # samplesizeb_i = Confidence_study1a.1.player.clicksmmb_i
    # samplea_i = Confidence_study1a.1.player.realsamplea_i
    # sampleb_i = Confidence_study1a.1.player.realsampleb_i
    # proboptiona_i = Confidence_study1a.1.player.realproba1
    # proboptionb_i = Confidence_study1a.1.player.realprobb1


    # yoking - corresponding column number in csvfile
    code = 'participant.code' # study1a, participant code
    samplea1 = 'player.realsamplea1' # study1a, player.realsamplea1 - Column 27 in csv
    sampleb1 = 'player.realsampleb1' # study1a, player.realsampleb1 - Column 28 in csv
    proboptiona1 = 'player.realproba1'  # study1a, player.realproba1 - Column 29 in csv
    proboptionb1 = 'player.realprobb1' # study1a, player.realprobb1 - Column 30 in csv
    mma1 = 'player.realamounta1' # study1a, player.realamounta1 - Column 31 in csv
    mmb1 = 'player.realamountb1' # study1a, player.realamountb1
    bo1 = 'player.bo1' # study1a, player.bo1
    samplesizea1 = 'player.clicksmma1'
    samplesizeb1 = 'player.clicksmmb1'

    samplea2 = 'player.realsamplea2'
    sampleb2 = 'player.realsampleb2'
    proboptiona2 = 'player.realproba2'
    proboptionb2 = 'player.realprobb2'
    mma2 = 'player.realamounta2'
    mmb2 = 'player.realamountb2'
    bo2 = 'player.bo2'
    samplesizea2 = 'player.clicksmma2'
    samplesizeb2 = 'player.clicksmmb2'

    samplea3 = 'player.realsamplea3'
    sampleb3 = 'player.realsampleb3'
    proboptiona3 = 'player.realproba3'
    proboptionb3 = 'player.realprobb3'
    mma3 = 'player.realamounta3'
    mmb3 = 'player.realamountb3'
    bo3 = 'player.bo3'
    samplesizea3 = 'player.clicksmma3'
    samplesizeb3 = 'player.clicksmmb3'

    samplea4 = 'player.realsamplea4'
    sampleb4 = 'player.realsampleb4'
    proboptiona4 = 'player.realproba4'
    proboptionb4 = 'player.realprobb4'
    mma4 = 'player.realamounta4'
    mmb4 = 'player.realamountb4'
    bo4 = 'player.bo4'
    samplesizea4 = 'player.clicksmma4'
    samplesizeb4 = 'player.clicksmmb4'

    samplea5 = 'player.realsamplea5'
    sampleb5 = 'player.realsampleb5'
    proboptiona5 = 'player.realproba5'
    proboptionb5 = 'player.realprobb5'
    mma5 = 'player.realamounta5'
    mmb5 = 'player.realamountb5'
    bo5 = 'player.bo5'
    samplesizea5 = 'player.clicksmma5'
    samplesizeb5 = 'player.clicksmmb5'

    samplea6 = 'player.realsamplea6'
    sampleb6 = 'player.realsampleb6'
    proboptiona6 = 'player.realproba6'
    proboptionb6 = 'player.realprobb6'
    mma6 = 'player.realamounta6'
    mmb6 = 'player.realamountb6'
    bo6 = 'player.bo6'
    samplesizea6 = 'player.clicksmma6'
    samplesizeb6 = 'player.clicksmmb6'

    samplea7 = 'player.realsamplea7'
    sampleb7 = 'player.realsampleb7'
    proboptiona7 = 'player.realproba7'
    proboptionb7 = 'player.realprobb7'
    mma7 = 'player.realamounta7'
    mmb7 = 'player.realamountb7'
    bo7 = 'player.bo7'
    samplesizea7 = 'player.clicksmma7'
    samplesizeb7 = 'player.clicksmmb7'

    samplea8 = 'player.realsamplea8'
    sampleb8 = 'player.realsampleb8'
    proboptiona8 = 'player.realproba8'
    proboptionb8 = 'player.realprobb8'
    mma8 = 'player.realamounta8'
    mmb8 = 'player.realamountb8'
    bo8 = 'player.bo8'
    samplesizea8 = 'player.clicksmma8'
    samplesizeb8 = 'player.clicksmmb8'

    samplea9 = 'player.realsamplea9'
    sampleb9 = 'player.realsampleb9'
    proboptiona9 = 'player.realproba9'
    proboptionb9 = 'player.realprobb9'
    mma9 = 'player.realamounta9'
    mmb9 = 'player.realamountb9'
    bo9 = 'player.bo9'
    samplesizea9 = 'player.clicksmma9'
    samplesizeb9 = 'player.clicksmmb9'

    samplea10 = 'player.realsamplea10'
    sampleb10 = 'player.realsampleb10'
    proboptiona10 = 'player.realproba10'
    proboptionb10 = 'player.realprobb10'
    mma10 = 'player.realamounta10'
    mmb10 = 'player.realamountb10'
    bo10 = 'player.bo10'
    samplesizea10 = 'player.clicksmma10'
    samplesizeb10 = 'player.clicksmmb10'



    # data format is 100 * posterior probabilities. highchart puts % after the numbers.
    # below data is for statistical tool page. illustration of the data format
    # data = [
    #         ['0', 0.0000000],
    #         ['1', 0.0003119],
    #         ['2', 0.0047173],
    #         ['3', 0.0225621],
    #         ['4', 0.0673444],
    #         ['5', 0.155225],
    #         ['6', 0.3037809],
    #         ['7', 0.5309758],
    #         ['8', 0.8543252],
    #         ['9', 1.2902324],
    #         ['10', 1.853476],
    #         ['11', 2.556829],
    #         ['12', 3.410797],
    #         ['13', 4.423448],
    #         ['14', 5.600334],
    #         ['15', 6.944485],
    #         ['16', 8.456458],
    #         ['17', 10.13444],
    #         ['18', 11.974388],
    #         ['19', 13.970202],
    #         ['20', 16.11392],
    #         ['21', 18.39593],
    #         ['22', 20.805197],
    #         ['23', 23.329483],
    #         ['24', 25.955583],
    #         ['25', 28.669548],
    #         ['26', 31.456902],
    #         ['27', 34.302857],
    #         ['28', 37.192506],
    #         ['29', 40.111009],
    #         ['30', 43.043766],
    #         ['31', 45.976567],
    #         ['32', 48.895732],
    #         ['33', 51.788234],
    #         ['34', 54.641796],
    #         ['35', 57.444985],
    #         ['36', 60.187278],
    #         ['37', 62.859119],
    #         ['38', 65.451957],
    #         ['39', 67.958269],
    #         ['40', 70.371573],
    #         ['41', 72.686425],
    #         ['42', 74.898406],
    #         ['43', 77.004097],
    #         ['44', 79.001046],
    #         ['45', 80.887728],
    #         ['46', 82.663493],
    #         ['47', 84.328513],
    #         ['48', 85.883723],
    #         ['49', 87.330755],
    #         ['50', 88.671875],
    #         ['51', 89.90991],
    #         ['52', 91.048186],
    #         ['53', 92.090452],
    #         ['54', 93.040816],
    #         ['55', 93.903676],
    #         ['56', 94.683657],
    #         ['57', 95.385549],
    #         ['58', 96.014248],
    #         ['59', 96.5747],
    #         ['60', 97.071851],
    #         ['61', 97.510602],
    #         ['62', 97.895766],
    #         ['63', 98.232027],
    #         ['64', 98.523914],
    #         ['65', 98.775767],
    #         ['66', 98.99172],
    #         ['67', 99.175676],
    #         ['68', 99.331296],
    #         ['69', 99.46199],
    #         ['70', 99.57091],
    #         ['71', 99.660948],
    #         ['72', 99.734737],
    #         ['73', 99.794655],
    #         ['74', 99.842835],
    #         ['75', 99.881172],
    #         ['76', 99.911333],
    #         ['77', 99.934776],
    #         ['78', 99.952758],
    #         ['79', 99.966355],
    #         ['80', 99.976478],
    #         ['81', 99.983887],
    #         ['82', 99.989208],
    #         ['83', 99.99295],
    #         ['84', 99.995522],
    #         ['85', 99.997244],
    #         ['86', 99.998364],
    #         ['87', 99.999068],
    #         ['88', 99.999493],
    #         ['89', 99.99974],
    #         ['90', 99.999875],
    #         ['91', 99.999944],
    #         ['92', 99.999977],
    #         ['93', 99.999992],
    #         ['94', 99.999997],
    #         ['95', 99.999999],
    #         ['96', 99.999999],
    #         ['97', 99.999999],
    #         ['98', 100],
    #         ['99', 100],
    #         ['100', 100],
    # ]




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

    data = models.CharField(doc = "datasource for beta distribution in illustration tool page")

    def getdatafortool(self):
        # number of 0 is 3
        # number of 80 is 6
        rawdata = [[str(i), beta.cdf(i / 100, 4, 7) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data = json.dumps(datalist)

    pass

    # winner = models.IntegerField(
    #      doc="one player is chosen by sweepstakes")
    #  # self.get_players() = [<Player 1>, <Player 2>, <Player 3>, <Player 4>, <Player 5>, <Player 6>, <Player 7>, <Player 8>, <Player 9>, <Player 10>]
    #  # all payoffs have to be positive. can't have negative payoff.
    # def sweepstakes(self):
    #     if self.session.config['sweepstakes'] == 1:
    #         stake0 = []
    #         # add up all points earned by all players
    #         group = sum(float(p.payoff) for p in self.get_players())
    #         # get number of the players
    #         num_players = len(self.get_players())
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


class Player(BasePlayer):




    gender = models.CharField(
        choices=['Male', 'Female'],
        widget=widgets.RadioSelect()
    )

    age = models.PositiveIntegerField()

    # yoking
    yoking = models.CharField (doc = "yoked participant code in Study_1a")

    # get which participant in Study_1a is yoked in Study_1b,1c and 1d
    def getyoked(self):
        yokinglist = self.participant.vars['yokinglist']
        # get the column participant code from csv file.
        self.yoking = yokinglist.get(Constants.code)

    def random():
        return random.randint(1, 10)

    randompayoff = models.IntegerField(default = random)

    rr_tool = models.FloatField(
        doc="maximum proportion of bad outcome in 100 can be tolerated in illustration page; switch/adjust point for machine A and B")
    confidence_tool = models.FloatField(
        doc="posterior probability of proportion of bad outcome smaller or equal to riskthreshold in illustration page")

    data1 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 1")
    optiona1 = models.CharField(doc="choice-sets specific, mma1 text display")
    optionb1 = models.CharField(doc="choice-sets specific, mmb1 text display")
    mm1 = models.BooleanField(doc = "which money machine button in pair 1 was clicked: 1=machine A, 0=machine B")
    riskthreshold1 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 1; switch/adjust point for machine A and B")
    confidence1 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 1")
    bo1 = models.FloatField(doc = "bad outcome in pair 1")

    data2 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 2")
    optiona2 = models.CharField(doc="choice-sets specific, mma2 text display")
    optionb2 = models.CharField(doc="choice-sets specific, mmb2 text display")
    mm2 = models.BooleanField(doc = "which money machine button in pair 2 was clicked: 1=machine A, 0=machine B")
    riskthreshold2 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 2; switch/adjust point for machine A and B")
    confidence2 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 2")
    bo2 = models.FloatField(doc = "bad outcome in pair 2")

    data3 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 3")
    optiona3 = models.CharField(doc="choice-sets specific, mma3 text display")
    optionb3 = models.CharField(doc="choice-sets specific, mmb3 text display")
    mm3 = models.BooleanField(doc = "which money machine button in pair 3 was clicked: 1=machine A, 0=machine B")
    riskthreshold3 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 3; switch/adjust point for machine A and B")
    confidence3 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 3")
    bo3 = models.FloatField(doc = "bad outcome in pair 3")

    data4 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 4")
    optiona4 = models.CharField(doc="choice-sets specific, mma4 text display")
    optionb4 = models.CharField(doc="choice-sets specific, mmb4 text display")
    mm4 = models.BooleanField(doc = "which money machine button in pair 4 was clicked: 1=machine A, 0=machine B")
    riskthreshold4 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 4; switch/adjust point for machine A and B")
    confidence4 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 4")
    bo4 = models.FloatField(doc = "bad outcome in pair 4")

    data5 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 5")
    optiona5 = models.CharField(doc="choice-sets specific, mma5 text display")
    optionb5 = models.CharField(doc="choice-sets specific, mmb5 text display")
    mm5 = models.BooleanField(doc = "which money machine button in pair 5 was clicked: 1=machine A, 0=machine B")
    riskthreshold5 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 5; switch/adjust point for machine A and B")
    confidence5 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 5")
    bo5 = models.FloatField(doc = "bad outcome in pair 5")

    data6 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 6")
    optiona6 = models.CharField(doc="choice-sets specific, mma6 text display")
    optionb6 = models.CharField(doc="choice-sets specific, mmb6 text display")
    mm6 = models.BooleanField(doc = "which money machine button in pair 6 was clicked: 1=machine A, 0=machine B")
    riskthreshold6 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 6; switch/adjust point for machine A and B")
    confidence6 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 6")
    bo6 = models.FloatField(doc = "bad outcome in pair 6")

    data7 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 7")
    optiona7 = models.CharField(doc="choice-sets specific, mma7 text display")
    optionb7 = models.CharField(doc="choice-sets specific, mmb7 text display")
    mm7 = models.BooleanField(doc = "which money machine button in pair 7 was clicked: 1=machine A, 0=machine B")
    riskthreshold7 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 7; switch/adjust point for machine A and B")
    confidence7 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 7")
    bo7 = models.FloatField(doc = "bad outcome in pair 7")

    data8 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 8")
    optiona8 = models.CharField(doc="choice-sets specific, mma8 text display")
    optionb8 = models.CharField(doc="choice-sets specific, mmb8 text display")
    mm8 = models.BooleanField(doc = "which money machine button in pair 8 was clicked: 1=machine A, 0=machine B")
    riskthreshold8 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 8; switch/adjust point for machine A and B")
    confidence8 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 8")
    bo8 = models.FloatField(doc = "bad outcome in pair 8")

    data9 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 9")
    optiona9 = models.CharField(doc="choice-sets specific, mma9 text display")
    optionb9 = models.CharField(doc="choice-sets specific, mmb9 text display")
    mm9 = models.BooleanField(doc = "which money machine button in pair 9 was clicked: 1=machine A, 0=machine B")
    riskthreshold9 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 9; switch/adjust point for machine A and B")
    confidence9 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 9")
    bo9 = models.FloatField(doc = "bad outcome in pair 9")

    data10 = models.CharField(doc = "confidence input value for highchart, determined by yoked sample draws in Pair 10")
    optiona10 = models.CharField(doc="choice-sets specific, mma10 text display")
    optionb10 = models.CharField(doc="choice-sets specific, mmb10 text display")
    mm10 = models.BooleanField(doc = "which money machine button in pair 10 was clicked: 1=machine A, 0=machine B")
    riskthreshold10 = models.FloatField(doc = "maximum proportion of bad outcome in 100 can be tolerated in Pair 10; switch/adjust point for machine A and B")
    confidence10 = models.FloatField(doc = "posterior probability of proportion of bad outcome smaller or equal to riskthreshold in Pair 10")
    bo10 = models.FloatField(doc = "bad outcome in pair 10")

    def getparameters(self):
        yokinglist = self.participant.vars['yokinglist']
        self.optiona1 = round(ast.literal_eval(yokinglist.get(Constants.mma1)))
        self.optiona2 = round(ast.literal_eval(yokinglist.get(Constants.mma2)))
        self.optiona3 = round(ast.literal_eval(yokinglist.get(Constants.mma3)))
        self.optiona4 = round(ast.literal_eval(yokinglist.get(Constants.mma4)))
        self.optiona5 = round(ast.literal_eval(yokinglist.get(Constants.mma5)))
        self.optiona6 = round(ast.literal_eval(yokinglist.get(Constants.mma6)))
        self.optiona7 = round(ast.literal_eval(yokinglist.get(Constants.mma7)))
        self.optiona8 = round(ast.literal_eval(yokinglist.get(Constants.mma8)))
        self.optiona9 = round(ast.literal_eval(yokinglist.get(Constants.mma9)))
        self.optiona10 = round(ast.literal_eval(yokinglist.get(Constants.mma10)))
        self.optionb1 = round(ast.literal_eval(yokinglist.get(Constants.mmb1)))
        self.optionb2 = round(ast.literal_eval(yokinglist.get(Constants.mmb2)))
        self.optionb3 = round(ast.literal_eval(yokinglist.get(Constants.mmb3)))
        self.optionb4 = round(ast.literal_eval(yokinglist.get(Constants.mmb4)))
        self.optionb5 = round(ast.literal_eval(yokinglist.get(Constants.mmb5)))
        self.optionb6 = round(ast.literal_eval(yokinglist.get(Constants.mmb6)))
        self.optionb7 = round(ast.literal_eval(yokinglist.get(Constants.mmb7)))
        self.optionb8 = round(ast.literal_eval(yokinglist.get(Constants.mmb8)))
        self.optionb9 = round(ast.literal_eval(yokinglist.get(Constants.mmb9)))
        self.optionb10 = round(ast.literal_eval(yokinglist.get(Constants.mmb10)))
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

# find good outcomes for each pair for display a button on HTML page
    def go1(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea1 = ast.literal_eval(yokinglist.get(Constants.samplea1))
        sampleb1 = ast.literal_eval(yokinglist.get(Constants.sampleb1))
        return max(int(i) for i in samplea1 + sampleb1)

    def go2(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea2 = ast.literal_eval(yokinglist.get(Constants.samplea2))
        sampleb2 = ast.literal_eval(yokinglist.get(Constants.sampleb2))
        return max(int(i) for i in samplea2 + sampleb2)

    def go3(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea3 = ast.literal_eval(yokinglist.get(Constants.samplea3))
        sampleb3 = ast.literal_eval(yokinglist.get(Constants.sampleb3))
        return max(int(i) for i in samplea3 + sampleb3)

    def go4(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea4 = ast.literal_eval(yokinglist.get(Constants.samplea4))
        sampleb4 = ast.literal_eval(yokinglist.get(Constants.sampleb4))
        return max(int(i) for i in samplea4 + sampleb4)

    def go5(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea5 = ast.literal_eval(yokinglist.get(Constants.samplea5))
        sampleb5 = ast.literal_eval(yokinglist.get(Constants.sampleb5))
        return max(int(i) for i in samplea5 + sampleb5)

    def go6(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea6 = ast.literal_eval(yokinglist.get(Constants.samplea6))
        sampleb6 = ast.literal_eval(yokinglist.get(Constants.sampleb6))
        return max(int(i) for i in samplea6 + sampleb6)

    def go7(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea7 = ast.literal_eval(yokinglist.get(Constants.samplea7))
        sampleb7 = ast.literal_eval(yokinglist.get(Constants.sampleb7))
        return max(int(i) for i in samplea7 + sampleb7)

    def go8(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea8 = ast.literal_eval(yokinglist.get(Constants.samplea8))
        sampleb8 = ast.literal_eval(yokinglist.get(Constants.sampleb8))
        return max(int(i) for i in samplea8 + sampleb8)

    def go9(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea9 = ast.literal_eval(yokinglist.get(Constants.samplea9))
        sampleb9 = ast.literal_eval(yokinglist.get(Constants.sampleb9))
        return max(int(i) for i in samplea9 + sampleb9)

    def go10(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea10 = ast.literal_eval(yokinglist.get(Constants.samplea10))
        sampleb10 = ast.literal_eval(yokinglist.get(Constants.sampleb10))
        return max(int(i) for i in samplea10 + sampleb10)

    # calculate confidence level for default value when the page is loaded, slider initial value is 50.
    # calculate the initical confidence based on Bayesian beta distribution
    def getinitialc1(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea1))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb1))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb1))
        num_bo_1 = samplea.count(str(self.bo1)) if proboptionb == 1.0 else sampleb.count(str(self.bo1))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)

    def getinitialc2(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea2))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb2))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb2))
        num_bo_1 = samplea.count(str(self.bo2)) if proboptionb == 1.0 else sampleb.count(str(self.bo2))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)

    def getinitialc3(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea3))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb3))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb3))
        num_bo_1 = samplea.count(str(self.bo3)) if proboptionb == 1.0 else sampleb.count(str(self.bo3))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)

    def getinitialc4(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea4))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb4))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb4))
        num_bo_1 = samplea.count(str(self.bo4)) if proboptionb == 1.0 else sampleb.count(str(self.bo4))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)

    def getinitialc5(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea5))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb5))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb5))
        num_bo_1 = samplea.count(str(self.bo5)) if proboptionb == 1.0 else sampleb.count(str(self.bo5))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)

    def getinitialc6(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea6))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb6))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb6))
        num_bo_1 = samplea.count(str(self.bo6)) if proboptionb == 1.0 else sampleb.count(str(self.bo6))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)

    def getinitialc7(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea7))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb7))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb7))
        num_bo_1 = samplea.count(str(self.bo7)) if proboptionb == 1.0 else sampleb.count(str(self.bo7))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)

    def getinitialc8(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea8))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb8))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb8))
        num_bo_1 = samplea.count(str(self.bo8)) if proboptionb == 1.0 else sampleb.count(str(self.bo8))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)


    def getinitialc9(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea9))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb9))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb9))
        num_bo_1 = samplea.count(str(self.bo9)) if proboptionb == 1.0 else sampleb.count(str(self.bo9))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)


    def getinitialc10(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea = ast.literal_eval(yokinglist.get(Constants.samplea10))
        sampleb = ast.literal_eval(yokinglist.get(Constants.sampleb10))
        proboptionb = ast.literal_eval(yokinglist.get(Constants.proboptionb10))
        num_bo_1 = samplea.count(str(self.bo10)) if proboptionb == 1.0 else sampleb.count(str(self.bo10))
        a = num_bo_1 + 1
        num_go_1 = len(samplea) - num_bo_1 if proboptionb == 1.0 else len(sampleb) - num_bo_1
        b = num_go_1 + 1
        initial = beta.cdf(0.5, a, b) * 100
        return "%0.2f" % (initial)


    def getdata1(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea1 = ast.literal_eval(yokinglist.get(Constants.samplea1))
        sampleb1 = ast.literal_eval(yokinglist.get(Constants.sampleb1))
        proboptionb1 = ast.literal_eval(yokinglist.get(Constants.proboptionb1))
        num_bo_1 = samplea1.count(str(self.bo1)) if proboptionb1 == 1.0 else sampleb1.count(str(self.bo1))
        a = num_bo_1 + 1
        num_go_1 = len(samplea1) - num_bo_1 if proboptionb1 == 1.0 else len(sampleb1) - num_bo_1
        b = num_go_1 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data1 = json.dumps(datalist)

    def getdata2(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea2 = ast.literal_eval(yokinglist.get(Constants.samplea2))
        sampleb2 = ast.literal_eval(yokinglist.get(Constants.sampleb2))
        proboptionb2 = ast.literal_eval(yokinglist.get(Constants.proboptionb2))
        num_bo_2 = samplea2.count(str(self.bo2)) if proboptionb2 == 1.0 else sampleb2.count(str(self.bo2))
        a = num_bo_2 + 1
        num_go_2 = len(samplea2) - num_bo_2 if proboptionb2 == 1.0 else len(sampleb2) - num_bo_2
        b = num_go_2 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data2 = json.dumps(datalist)

    def getdata3(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea3 = ast.literal_eval(yokinglist.get(Constants.samplea3))
        sampleb3 = ast.literal_eval(yokinglist.get(Constants.sampleb3))
        proboptionb3 = ast.literal_eval(yokinglist.get(Constants.proboptionb3))
        num_bo_3 = samplea3.count(str(self.bo3)) if proboptionb3 == 1.0 else sampleb3.count(str(self.bo3))
        a = num_bo_3 + 1
        num_go_3 = len(samplea3) - num_bo_3 if proboptionb3 == 1.0 else len(sampleb3) - num_bo_3
        b = num_go_3 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data3 = json.dumps(datalist)

    def getdata4(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea4 = ast.literal_eval(yokinglist.get(Constants.samplea4))
        sampleb4 = ast.literal_eval(yokinglist.get(Constants.sampleb4))
        proboptionb4 = ast.literal_eval(yokinglist.get(Constants.proboptionb4))
        num_bo_4 = samplea4.count(str(self.bo4)) if proboptionb4 == 1.0 else sampleb4.count(str(self.bo4))
        a = num_bo_4 + 1
        num_go_4 = len(samplea4) - num_bo_4 if proboptionb4 == 1.0 else len(sampleb4) - num_bo_4
        b = num_go_4 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data4 = json.dumps(datalist)

    def getdata5(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea5 = ast.literal_eval(yokinglist.get(Constants.samplea5))
        sampleb5 = ast.literal_eval(yokinglist.get(Constants.sampleb5))
        proboptionb5 = ast.literal_eval(yokinglist.get(Constants.proboptionb5))
        num_bo_5 = samplea5.count(str(self.bo5)) if proboptionb5 == 1.0 else sampleb5.count(str(self.bo5))
        a = num_bo_5 + 1
        num_go_5 = len(samplea5) - num_bo_5 if proboptionb5 == 1.0 else len(sampleb5) - num_bo_5
        b = num_go_5 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data5 = json.dumps(datalist)

    def getdata6(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea6 = ast.literal_eval(yokinglist.get(Constants.samplea6))
        sampleb6 = ast.literal_eval(yokinglist.get(Constants.sampleb6))
        proboptionb6 = ast.literal_eval(yokinglist.get(Constants.proboptionb6))
        num_bo_6 = samplea6.count(str(self.bo6)) if proboptionb6 == 1.0 else sampleb6.count(str(self.bo6))
        a = num_bo_6 + 1
        num_go_6 = len(samplea6) - num_bo_6 if proboptionb6 == 1.0 else len(sampleb6) - num_bo_6
        b = num_go_6 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data6 = json.dumps(datalist)

    def getdata7(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea7 = ast.literal_eval(yokinglist.get(Constants.samplea7))
        sampleb7 = ast.literal_eval(yokinglist.get(Constants.sampleb7))
        proboptionb7 = ast.literal_eval(yokinglist.get(Constants.proboptionb7))
        num_bo_7 = samplea7.count(str(self.bo7)) if proboptionb7 == 1.0 else sampleb7.count(str(self.bo7))
        a = num_bo_7 + 1
        num_go_7 = len(samplea7) - num_bo_7 if proboptionb7 == 1.0 else len(sampleb7) - num_bo_7
        b = num_go_7 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data7 = json.dumps(datalist)

    def getdata8(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea8 = ast.literal_eval(yokinglist.get(Constants.samplea8))
        sampleb8 = ast.literal_eval(yokinglist.get(Constants.sampleb8))
        proboptionb8 = ast.literal_eval(yokinglist.get(Constants.proboptionb8))
        num_bo_8 = samplea8.count(str(self.bo8)) if proboptionb8 == 1.0 else sampleb8.count(str(self.bo8))
        a = num_bo_8 + 1
        num_go_8 = len(samplea8) - num_bo_8 if proboptionb8 == 1.0 else len(sampleb8) - num_bo_8
        b = num_go_8 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data8 = json.dumps(datalist)

    def getdata9(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea9 = ast.literal_eval(yokinglist.get(Constants.samplea9))
        sampleb9 = ast.literal_eval(yokinglist.get(Constants.sampleb9))
        proboptionb9 = ast.literal_eval(yokinglist.get(Constants.proboptionb9))
        num_bo_9 = samplea9.count(str(self.bo9)) if proboptionb9 == 1.0 else sampleb9.count(str(self.bo9))
        a = num_bo_9 + 1
        num_go_9 = len(samplea9) - num_bo_9 if proboptionb9 == 1.0 else len(sampleb9) - num_bo_9
        b = num_go_9 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data9 = json.dumps(datalist)

    def getdata10(self):
        yokinglist = self.participant.vars['yokinglist']
        samplea10 = ast.literal_eval(yokinglist.get(Constants.samplea10))
        sampleb10 = ast.literal_eval(yokinglist.get(Constants.sampleb10))
        proboptionb10 = ast.literal_eval(yokinglist.get(Constants.proboptionb10))
        num_bo_10 = samplea10.count(str(self.bo10)) if proboptionb10 == 1.0 else sampleb10.count(str(self.bo10))
        a = num_bo_10 + 1
        num_go_10 = len(samplea10) - num_bo_10 if proboptionb10 == 1.0 else len(sampleb10) - num_bo_10
        b = num_go_10 + 1
        rawdata = [[str(i), beta.cdf(i / 100, a, b) * 100] for i in range(0, 101)]
        datalist = []
        for i in rawdata:
            datalist.append(i)
        self.data10 = json.dumps(datalist)

# Choices chosen for the confirmation page for each problem set

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


  ########################################
    #  set up the style of buttons for result page

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


    # get the non-zero outcomes for each pair, both money machine A and B

    def amounta1(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma1))))

    def amountb1(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb1))))

    def amounta2(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma2))))

    def amountb2(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb2))))

    def amounta3(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma3))))

    def amountb3(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb3))))

    def amounta4(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma4))))

    def amountb4(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb4))))

    def amounta5(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma5))))

    def amountb5(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb5))))

    def amounta6(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma6))))

    def amountb6(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb6))))

    def amounta7(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma7))))

    def amountb7(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb7))))

    def amounta8(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma8))))

    def amountb8(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb8))))

    def amounta9(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma9))))

    def amountb9(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb9))))

    def amounta10(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mma10))))

    def amountb10(self):
        yokinglist = self.participant.vars['yokinglist']
        return round(ast.literal_eval((yokinglist.get(Constants.mmb10))))


# set up parameter for the random draw which determines the payoff
    def set_payoffs(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona1 = ast.literal_eval(yokinglist.get(Constants.proboptiona1))
        proboptionb1 = ast.literal_eval(yokinglist.get(Constants.proboptionb1))
        proboptiona2 = ast.literal_eval(yokinglist.get(Constants.proboptiona2))
        proboptionb2 = ast.literal_eval(yokinglist.get(Constants.proboptionb2))
        proboptiona3 = ast.literal_eval(yokinglist.get(Constants.proboptiona3))
        proboptionb3 = ast.literal_eval(yokinglist.get(Constants.proboptionb3))
        proboptiona4 = ast.literal_eval(yokinglist.get(Constants.proboptiona4))
        proboptionb4 = ast.literal_eval(yokinglist.get(Constants.proboptionb4))
        proboptiona5 = ast.literal_eval(yokinglist.get(Constants.proboptiona5))
        proboptionb5 = ast.literal_eval(yokinglist.get(Constants.proboptionb5))
        proboptiona6 = ast.literal_eval(yokinglist.get(Constants.proboptiona6))
        proboptionb6 = ast.literal_eval(yokinglist.get(Constants.proboptionb6))
        proboptiona7 = ast.literal_eval(yokinglist.get(Constants.proboptiona7))
        proboptionb7 = ast.literal_eval(yokinglist.get(Constants.proboptionb7))
        proboptiona8 = ast.literal_eval(yokinglist.get(Constants.proboptiona8))
        proboptionb8 = ast.literal_eval(yokinglist.get(Constants.proboptionb8))
        proboptiona9 = ast.literal_eval(yokinglist.get(Constants.proboptiona9))
        proboptionb9 = ast.literal_eval(yokinglist.get(Constants.proboptionb9))
        proboptiona10 = ast.literal_eval(yokinglist.get(Constants.proboptiona10))
        proboptionb10 = ast.literal_eval(yokinglist.get(Constants.proboptionb10))
        if self.randompayoff == 1:
            p = proboptiona1 if self.mm1 == 1 else proboptionb1
            scale = self.amounta1() if self.mm1 == 1 else self.amountb1()
        elif self.randompayoff == 2:
            p = proboptiona2 if self.mm2 == 1 else proboptionb2
            scale = self.amounta2() if self.mm2 == 1 else self.amountb2()
        elif self.randompayoff == 3:
            p = proboptiona3 if self.mm3 == 1 else proboptionb3
            scale = self.amounta3() if self.mm3 == 1 else self.amountb3()
        elif self.randompayoff == 4:
            p = proboptiona4 if self.mm4 == 1 else proboptionb4
            scale = self.amounta4() if self.mm4 == 1 else self.amountb4()
        elif self.randompayoff == 5:
            p = proboptiona5 if self.mm5 == 1 else proboptionb5
            scale = self.amounta5() if self.mm5 == 1 else self.amountb5()
        elif self.randompayoff == 6:
            p = proboptiona6 if self.mm6 == 1 else proboptionb6
            scale = self.amounta6() if self.mm6 == 1 else self.amountb6()
        elif self.randompayoff == 7:
            p = proboptiona7 if self.mm7 == 1 else proboptionb7
            scale = self.amounta7() if self.mm7 == 1 else self.amountb7()
        elif self.randompayoff == 8:
            p = proboptiona8 if self.mm8 == 1 else proboptionb8
            scale = self.amounta8() if self.mm8 == 1 else self.amountb8()
        elif self.randompayoff == 9:
            p = proboptiona9 if self.mm9 == 1 else proboptionb9
            scale = self.amounta9() if self.mm9 == 1 else self.amountb9()
        elif self.randompayoff == 10:
            p = proboptiona10 if self.mm10 == 1 else proboptionb10
            scale = self.amounta10() if self.mm10 == 1 else self.amountb10()
        self.payoff = int(scale * np.random.binomial(1, p))
        self.participant.vars['sweepstake'] = round(int(self.payoff + Constants.showupfee))


# determine which page to show as the result of payoff, certain outcome vs. uncertain outcome which leads to a random draw
    def prob1(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm1 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona1))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb1))

    def prob2(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm2 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona2))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb2))

    def prob3(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm3 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona3))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb3))

    def prob4(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm4 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona4))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb4))

    def prob5(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm5 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona5))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb5))

    def prob6(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm6 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona6))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb6))

    def prob7(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm7 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona7))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb7))

    def prob8(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm8 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona8))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb8))

    def prob9(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm9 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona9))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb9))

    def prob10(self):
        yokinglist = self.participant.vars['yokinglist']
        if self.mm10 == 1:
            return ast.literal_eval(yokinglist.get(Constants.proboptiona10))
        return ast.literal_eval(yokinglist.get(Constants.proboptionb10))


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
        if self.ps() < 1:
            return 1
        return 0

    # based on the option of money machine A and B,
    # to show different text "Here you see different outcomes for Money Machine X" or
    # "Here you see the only outcomes for Money Machine X"
    def texta1(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona1 = ast.literal_eval(yokinglist.get(Constants.proboptiona1))
        mma1 = ast.literal_eval(yokinglist.get(Constants.mma1))
        if proboptiona1 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma1)) + '.'
        return Constants.text_a_uncertain

    def textb1(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb1 = ast.literal_eval(yokinglist.get(Constants.proboptionb1))
        mmb1 = ast.literal_eval(yokinglist.get(Constants.mmb1))
        if proboptionb1 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb1)) + '.'
        return Constants.text_b_uncertain

    def texta2(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona2 = ast.literal_eval(yokinglist.get(Constants.proboptiona2))
        mma2 = ast.literal_eval(yokinglist.get(Constants.mma2))
        if proboptiona2 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma2)) + '.'
        return Constants.text_a_uncertain

    def textb2(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb2 = ast.literal_eval(yokinglist.get(Constants.proboptionb2))
        mmb2 = ast.literal_eval(yokinglist.get(Constants.mmb2))
        if proboptionb2 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb2)) + '.'
        return Constants.text_b_uncertain

    def texta3(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona3 = ast.literal_eval(yokinglist.get(Constants.proboptiona3))
        mma3 = ast.literal_eval(yokinglist.get(Constants.mma3))
        if proboptiona3 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma3)) + '.'
        return Constants.text_a_uncertain

    def textb3(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb3 = ast.literal_eval(yokinglist.get(Constants.proboptionb3))
        mmb3 = ast.literal_eval(yokinglist.get(Constants.mmb3))
        if proboptionb3 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb3)) + '.'
        return Constants.text_b_uncertain

    def texta4(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona4 = ast.literal_eval(yokinglist.get(Constants.proboptiona4))
        mma4 = ast.literal_eval(yokinglist.get(Constants.mma4))
        if proboptiona4 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma4)) + '.'
        return Constants.text_a_uncertain

    def textb4(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb4 = ast.literal_eval(yokinglist.get(Constants.proboptionb4))
        mmb4 = ast.literal_eval(yokinglist.get(Constants.mmb4))
        if proboptionb4 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb4)) + '.'
        return Constants.text_b_uncertain

    def texta5(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona5 = ast.literal_eval(yokinglist.get(Constants.proboptiona5))
        mma5 = ast.literal_eval(yokinglist.get(Constants.mma5))
        if proboptiona5 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma5)) + '.'
        return Constants.text_a_uncertain

    def textb5(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb5 = ast.literal_eval(yokinglist.get(Constants.proboptionb5))
        mmb5 = ast.literal_eval(yokinglist.get(Constants.mmb5))
        if proboptionb5 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb5)) + '.'
        return Constants.text_b_uncertain

    def texta6(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona6 = ast.literal_eval(yokinglist.get(Constants.proboptiona6))
        mma6 = ast.literal_eval(yokinglist.get(Constants.mma6))
        if proboptiona6 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma6)) + '.'
        return Constants.text_a_uncertain

    def textb6(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb6 = ast.literal_eval(yokinglist.get(Constants.proboptionb6))
        mmb6 = ast.literal_eval(yokinglist.get(Constants.mmb6))
        if proboptionb6 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb6)) + '.'
        return Constants.text_b_uncertain

    def texta7(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona7 = ast.literal_eval(yokinglist.get(Constants.proboptiona7))
        mma7 = ast.literal_eval(yokinglist.get(Constants.mma7))
        if proboptiona7 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma7)) + '.'
        return Constants.text_a_uncertain

    def textb7(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb7 = ast.literal_eval(yokinglist.get(Constants.proboptionb7))
        mmb7 = ast.literal_eval(yokinglist.get(Constants.mmb7))
        if proboptionb7 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb7)) + '.'
        return Constants.text_b_uncertain

    def texta8(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona8 = ast.literal_eval(yokinglist.get(Constants.proboptiona8))
        mma8 = ast.literal_eval(yokinglist.get(Constants.mma8))
        if proboptiona8 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma8)) + '.'
        return Constants.text_a_uncertain

    def textb8(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb8 = ast.literal_eval(yokinglist.get(Constants.proboptionb8))
        mmb8 = ast.literal_eval(yokinglist.get(Constants.mmb8))
        if proboptionb8 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb8)) + '.'
        return Constants.text_b_uncertain

    def texta9(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona9 = ast.literal_eval(yokinglist.get(Constants.proboptiona9))
        mma9 = ast.literal_eval(yokinglist.get(Constants.mma9))
        if proboptiona9 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma9)) + '.'
        return Constants.text_a_uncertain

    def textb9(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb9 = ast.literal_eval(yokinglist.get(Constants.proboptionb9))
        mmb9 = ast.literal_eval(yokinglist.get(Constants.mmb9))
        if proboptionb9 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb9)) + '.'
        return Constants.text_b_uncertain

    def texta10(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptiona10 = ast.literal_eval(yokinglist.get(Constants.proboptiona10))
        mma10 = ast.literal_eval(yokinglist.get(Constants.mma10))
        if proboptiona10 == 1.0:
            return Constants.text_a_certain + ' ' + str(round(mma10)) + '.'
        return Constants.text_a_uncertain

    def textb10(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb10 = ast.literal_eval(yokinglist.get(Constants.proboptionb10))
        mmb10 = ast.literal_eval(yokinglist.get(Constants.mmb10))
        if proboptionb10 == 1.0:
            return Constants.text_b_certain + ' ' + str(round(mmb10)) + '.'
        return Constants.text_b_uncertain

   # for explaination text of highchart: money machine A or B
    def machine1(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb1 = ast.literal_eval(yokinglist.get(Constants.proboptionb1))
        if proboptionb1 == 1.0:
            return "A"
        return "B"

    def machine2(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb2 = ast.literal_eval(yokinglist.get(Constants.proboptionb2))
        if proboptionb2 == 1.0:
            return "A"
        return "B"

    def machine3(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb3 = ast.literal_eval(yokinglist.get(Constants.proboptionb3))
        if proboptionb3 == 1.0:
            return "A"
        return "B"

    def machine4(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb4 = ast.literal_eval(yokinglist.get(Constants.proboptionb4))
        if proboptionb4 == 1.0:
            return "A"
        return "B"

    def machine5(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb5 = ast.literal_eval(yokinglist.get(Constants.proboptionb5))
        if proboptionb5 == 1.0:
            return "A"
        return "B"

    def machine6(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb6 = ast.literal_eval(yokinglist.get(Constants.proboptionb6))
        if proboptionb6 == 1.0:
            return "A"
        return "B"

    def machine7(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb7 = ast.literal_eval(yokinglist.get(Constants.proboptionb7))
        if proboptionb7 == 1.0:
            return "A"
        return "B"

    def machine8(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb8 = ast.literal_eval(yokinglist.get(Constants.proboptionb8))
        if proboptionb8 == 1.0:
            return "A"
        return "B"

    def machine9(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb9 = ast.literal_eval(yokinglist.get(Constants.proboptionb9))
        if proboptionb9 == 1.0:
            return "A"
        return "B"

    def machine10(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb10 = ast.literal_eval(yokinglist.get(Constants.proboptionb10))
        if proboptionb10 == 1.0:
            return "A"
        return "B"


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
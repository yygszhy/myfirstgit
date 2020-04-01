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


author = 'Feibai'

doc = """
Confidence Study1a
"""


class Constants(BaseConstants):
    name_in_url = 'Confidence_study1a'
    players_per_group = None
    showupfee = 100
    num_rounds = 1
    num_problemsets = 10
    mmacolor = 'lightblue'
    mmbcolor = 'orange'
    textcertaina = 'Money Machine A has one possible outcome only, always'
    textuncertaina = 'Here you see sample outcomes for Money Machine A.'
    textcertainb = 'Money Machine B has one possible outcome only, always'
    textuncertainb = 'Here you see sample outcomes for Money Machine B.'
    shorttext = 'Your sample outcome(s)'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    # # self.get_player() = [<Player 1>, <Player 2>, <Player 3>, <Player 4>, <Player 5>, <Player 6>, <Player 7>, <Player 8>, <Player 9>, <Player 10>]
    # def sweepstakes(self):
    #      stake = []
    #      for p in self.get_player():
    #          p.playerstake = (p.payoff + Constants.showupfee)/sum[(p.payoff + Constants.showupfee)]
    #          stake.append(p.playerstake)
    #      winner = np.random.choice(np.arange(1, Constants.players_per_group), p=stake)
    #      return self.get_player_by_id(winner)
    pass


class Player(BasePlayer):

    # randomly choose one problem set for payoff

    def random():
        return random.randint(1, 10)

    randompayoff = models.IntegerField(default = random)

    # define fields for the money machines in instruction page
    clicksmma_ins = models.PositiveIntegerField(doc="participant drawn sample size for mma in instruction page")
    clicksmmb_ins = models.PositiveIntegerField(doc="participant drawn sample size for mmb in instruction page")

    # define fields for realized attributes of each money machine after randomization

    optiona1 = models.CharField(doc="choice-set specific, mma1 text display")
    optionb1 = models.CharField(doc="choice-set specific, mmb1 text display")
    # proboptiona1 = models.CharField(doc="choice-set specific, mma1 probabilities text display underneath")
    # proboptionb1 = models.CharField(doc="choice-set specific, mmb1 probabilities text display underneath")
    clicksmma1 = models.PositiveIntegerField(doc="participant drawn sample size a1")
    clicksmmb1 = models.PositiveIntegerField(doc="participant drawn sample size b1")
    samplemma1 = models.CharField(doc = "python randomly generated 100 samples a1")
    samplemmb1 = models.CharField(doc = "python randomly generated 100 samples b1")
   # choice1 = models.CharField(doc = "chosen money machine A or B")
    realsamplea1 = models.CharField(doc = "participant drawn samples a1")
    realsampleb1 = models.CharField(doc = "participant drawn samples b1")
    realproba1 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a1")
    realprobb1 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b1")
    realamounta1 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a1")
    realamountb1 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b1")
    bo1 = models.FloatField(doc = "bad outcome in pair 1")

    optiona2 = models.CharField(doc="choice-set specific,mma2 text display")
    optionb2 = models.CharField(doc="choice-set specific,mmb2 text display")
    # proboptiona2 = models.CharField(doc="choice-set specific,mma2 probabilities text display underneath")
    # proboptionb2 = models.CharField(doc="choice-set specific,mmb2 probabilities text display underneath")
    clicksmma2 = models.PositiveIntegerField(doc="participant drawn sample size a2")
    clicksmmb2 = models.PositiveIntegerField(doc="participant drawn sample size b2")
    samplemma2 = models.CharField(doc = "python randomly generated 100 samples a2")
    samplemmb2 = models.CharField(doc = "python randomly generated 100 samples b2")
  #  choice2 = models.CharField(doc = "chosen money machine A or B")
    realsamplea2 = models.CharField(doc = "participant drawn samples a2")
    realsampleb2 = models.CharField(doc = "participant drawn samples b2")
    realproba2 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a2")
    realprobb2 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b2")
    realamounta2 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a2")
    realamountb2 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b2")
    bo2 = models.FloatField(doc = "bad outcome in pair 2")

    optiona3 = models.CharField(doc="choice-set specific,mma3 text display")
    optionb3 = models.CharField(doc="choice-set specific,mmb3 text display")
    # proboptiona3 = models.CharField(doc="choice-set specific,mma3 probabilities text display underneath")
    # proboptionb3 = models.CharField(doc="choice-set specific, mmb3 probabilities text display underneath")
    clicksmma3 = models.PositiveIntegerField(doc="participant drawn sample size a3")
    clicksmmb3 = models.PositiveIntegerField(doc="participant drawn sample size b3")
    samplemma3 = models.CharField(doc = "python randomly generated 100 samples a3")
    samplemmb3 = models.CharField(doc = "python randomly generated 100 samples b3")
   # choice3 = models.CharField()
    realsamplea3 = models.CharField(doc = "participant drawn samples a3")
    realsampleb3 = models.CharField(doc = "participant drawn samples b3")
    realproba3 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a3")
    realprobb3 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b3")
    realamounta3 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a3")
    realamountb3 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b3")
    bo3 = models.FloatField(doc = "bad outcome in pair 3")

    optiona4 = models.CharField(doc="choice-set specific, mma4 text display")
    optionb4 = models.CharField(doc="choice-set specific, mmb4 text display")
    # proboptiona4 = models.CharField(doc="choice-set specific, mma4 probabilities text display underneath")
    # proboptionb4 = models.CharField(doc="choice-set specific, mmb4 probabilities text display underneath")
    clicksmma4 = models.PositiveIntegerField(doc="participant drawn sample size a4")
    clicksmmb4 = models.PositiveIntegerField(doc="participant drawn sample size b4")
    samplemma4 = models.CharField(doc = "python randomly generated 100 samples a4")
    samplemmb4 = models.CharField(doc = "python randomly generated 100 samples b4")
  #  choice4 = models.CharField()
    realsamplea4 = models.CharField(doc = "participant drawn samples a4")
    realsampleb4 = models.CharField(doc = "participant drawn samples b4")
    realproba4 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a4")
    realprobb4 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b4")
    realamounta4 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a4")
    realamountb4 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b4")
    bo4 = models.FloatField(doc = "bad outcome in pair 4")

    optiona5 = models.CharField(doc="choice-set specific, mma5 text display")
    optionb5 = models.CharField(doc="choice-set specific, mmb5 text display")
    # proboptiona5 = models.CharField(doc="choice-set specific, mma5 probabilities text display underneath")
    # proboptionb5 = models.CharField(doc="choice-set specific, mmb5 probabilities text display underneath")
    clicksmma5 = models.PositiveIntegerField(doc="participant drawn sample size a5")
    clicksmmb5 = models.PositiveIntegerField(doc="participant drawn sample size b5")
    samplemma5 = models.CharField(doc = "python randomly generated 100 samples a5")
    samplemmb5 = models.CharField(doc = "python randomly generated 100 samples b5")
   # choice5 = models.CharField()
    realsamplea5 = models.CharField(doc = "participant drawn samples a5")
    realsampleb5 = models.CharField(doc = "participant drawn samples b5")
    realproba5 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a5")
    realprobb5 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b5")
    realamounta5 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a5")
    realamountb5 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b5")
    bo5 = models.FloatField(doc = "bad outcome in pair 5")

    optiona6 = models.CharField(doc="choice-set specific, mma6 text display")
    optionb6 = models.CharField(doc="choice-set specific, mmb6 text display")
    # proboptiona6 = models.CharField(doc="choice-set specific, mma6 probabilities text display underneath")
    # proboptionb6 = models.CharField(doc="choice-set specific, mmb6 probabilities text display underneath")
    clicksmma6 = models.PositiveIntegerField(doc="participant drawn sample size a6")
    clicksmmb6 = models.PositiveIntegerField(doc="participant drawn sample size b6")
    samplemma6 = models.CharField(doc = "python randomly generated 100 samples a6")
    samplemmb6 = models.CharField(doc = "python randomly generated 100 samples b6")
   # choice6 = models.CharField()
    realsamplea6 = models.CharField(doc = "participant drawn samples a6")
    realsampleb6 = models.CharField(doc = "participant drawn samples b6")
    realproba6 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a6")
    realprobb6 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b6")
    realamounta6 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a6")
    realamountb6 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b6")
    bo6 = models.FloatField(doc = "bad outcome in pair 6")

    optiona7 = models.CharField(doc="choice-set specific, mma7 text display")
    optionb7 = models.CharField(doc="choice-set specific, mmb7 text display")
    # proboptiona7 = models.CharField(doc="choice-set specific, mma7 probabilities text display underneath")
    # proboptionb7 = models.CharField(doc="choice-set specific, mmb7 probabilities text display underneath")
    clicksmma7 = models.PositiveIntegerField(doc="participant drawn sample size a7")
    clicksmmb7 = models.PositiveIntegerField(doc="participant drawn sample size b7")
    samplemma7 = models.CharField(doc = "python randomly generated 100 samples a7")
    samplemmb7 = models.CharField(doc = "python randomly generated 100 samples b7")
   # choice7 = models.CharField()
    realsamplea7 = models.CharField(doc = "participant drawn samples a7")
    realsampleb7 = models.CharField(doc = "participant drawn samples b7")
    realproba7 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a7")
    realprobb7 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b7")
    realamounta7 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a7")
    realamountb7 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b7")
    bo7 = models.FloatField(doc = "bad outcome in pair 7")

    optiona8 = models.CharField(doc="choice-set specific, mma8 text display")
    optionb8 = models.CharField(doc="choice-set specific, mmb8 text display")
    # proboptiona8 = models.CharField(doc="choice-set specific, mma8 probabilities text display underneath")
    # proboptionb8 = models.CharField(doc="choice-set specific, mmb8 probabilities text display underneath")
    clicksmma8 = models.PositiveIntegerField(doc="participant drawn sample size a8")
    clicksmmb8 = models.PositiveIntegerField(doc="participant drawn sample size b8")
    samplemma8 = models.CharField(doc = "python randomly generated 100 samples a8")
    samplemmb8 = models.CharField(doc = "python randomly generated 100 samples b8")
   # choice8 = models.CharField()
    realsamplea8 = models.CharField(doc = "participant drawn samples a8")
    realsampleb8 = models.CharField(doc = "participant drawn samples b8")
    realproba8 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a8")
    realprobb8 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b8")
    realamounta8 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a8")
    realamountb8 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b8")
    bo8 = models.FloatField(doc = "bad outcome in pair 8")

    optiona9 = models.CharField(doc="choice-set specific, mma9 text display")
    optionb9 = models.CharField(doc="choice-set specific, mmb9 text display")
    # proboptiona9 = models.CharField(doc="choice-set specific, mma9 probabilities text display underneath")
    # proboptionb9 = models.CharField(doc="choice-set specific, mmb9 probabilities text display underneath")
    clicksmma9 = models.PositiveIntegerField(doc="participant drawn sample size a9")
    clicksmmb9 = models.PositiveIntegerField(doc="participant drawn sample size b9")
    samplemma9 = models.CharField(doc = "python randomly generated 100 samples a9")
    samplemmb9 = models.CharField(doc = "python randomly generated 100 samples b9")
   # choice9 = models.CharField()
    realsamplea9 = models.CharField(doc = "participant drawn samples a9")
    realsampleb9 = models.CharField(doc = "participant drawn samples b9")
    realproba9 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a9")
    realprobb9 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b9")
    realamounta9 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a9")
    realamountb9 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b9")
    bo9 = models.FloatField(doc = "bad outcome in pair 9")

    optiona10 = models.CharField(doc="choice-set specific, mma10 text display")
    optionb10 = models.CharField(doc="choice-set specific, mmb10 text display")
    # proboptiona10 = models.CharField(doc="choice-set specific, mma10 probabilities text display underneath")
    # proboptionb10 = models.CharField(doc="choice-set specific, mmb10 probabilities text display underneath")
    clicksmma10 = models.PositiveIntegerField(doc="participant drawn sample size a10")
    clicksmmb10 = models.PositiveIntegerField(doc="participant drawn sample size b10")
    samplemma10 = models.CharField(doc = "python randomly generated 100 samples a10")
    samplemmb10 = models.CharField(doc = "python randomly generated 100 samples b10")
   # choice10 = models.CharField()
    realsamplea10 = models.CharField(doc = "participant drawn samples a10")
    realsampleb10 = models.CharField(doc = "participant drawn samples b10")
    realproba10 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine a10")
    realprobb10 = models.FloatField(doc = "probabilities as number parameter for binomial distribution to draw samples from money machine b10")
    realamounta10 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine a10")
    realamountb10 = models.FloatField(doc = "outcome as number parameter for binomial distribution to draw samples from money machine b10")
    bo10 = models.FloatField(doc = "bad outcome in pair 10")
    # index of problem sets for each pair of money machine. identifier of problem sets after randomization
    # index = 1: 80% 4 vs. 100% 3
    # index = 2: 80% -4 vs. 100% -3
    # index = 3: 10% 32 vs. 100% 3
    # index = 4: 90% 10 vs. 100% 9
    # index = 5: 90% -10 vs. 100% -9
    # index = 6: 50% 2 vs. 100% 1
    # index = 7: 50% -10 vs. 100% -5
    # index = 8: 80% 2 vs. 100% 1
    # index = 9: 80% -2 vs. 100% -1
    # index = 10: 90% 10 vs. 100% 5
    index1 = models.IntegerField(doc = "which money machines are in pair 1 after randomization")
    index2 = models.IntegerField(doc="which money machines are in pair 2 after randomization")
    index3 = models.IntegerField(doc="which money machines are in pair 3 after randomization")
    index4 = models.IntegerField(doc="which money machines are in pair 4 after randomization")
    index5 = models.IntegerField(doc="which money machines are in pair 5 after randomization")
    index6 = models.IntegerField(doc="which money machines are in pair 6 after randomization")
    index7 = models.IntegerField(doc="which money machines are in pair 7 after randomization")
    index8 = models.IntegerField(doc="which money machines are in pair 8 after randomization")
    index9 = models.IntegerField(doc="which money machines are in pair 9 after randomization")
    index10 = models.IntegerField(doc="which money machines are in pair 10 after randomization")

    trivial1 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial2 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial3 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial4 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial5 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial6 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial7 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial8 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial9 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")
    trivial10 = models.BooleanField(doc="check if the samples of the risky option only contains one outcome.")

    # define parameter for randomly determined payoff pair

    def getmoneymachines(self):
       # Attributes of money machine pairs based on problem set long list dated 20.07.2017
        class Mm1(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes 0¢ or 40¢'
                self.outcomebtext = 'Possible outcome 30¢'
                # self.outcomeaprob = 'Outcome probabilities 20% or 80%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = 40
                self.amountb = 30
                self.proba = 0.8
                self.probb = 1.0
                self.index = 1
        pass
        mm1 = Mm1()

        class Mm2(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes -40¢ or 0¢'
                self.outcomebtext = 'Possible outcome -30¢'
                # self.outcomeaprob = 'Outcome probabilities 80% or 20%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = -40
                self.amountb = -30
                self.proba = 0.8
                self.probb = 1.0
                self.index = 2

        pass
        mm2 = Mm2()

        class Mm3(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes 0¢ or 320¢'
                self.outcomebtext = 'Possible outcome 30¢'
               # self.outcomeaprob = 'Outcome probabilities 90% or 10%'
            # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = 320
                self.amountb = 30
                self.proba = 0.1
                self.probb = 1.0
                self.index = 3

        pass
        mm3 = Mm3()

        class Mm4(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes -100¢ or 0¢'
                self.outcomebtext = 'Possible outcome -90¢'
                # self.outcomeaprob = 'Outcome probabilities 90% or 10%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = -100
                self.amountb = -90
                self.proba = 0.9
                self.probb = 1.0
                self.index = 5

        pass
        mm4 = Mm4()

        class Mm5(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes 100¢ or 0¢'
                self.outcomebtext = 'Possible outcome 90¢'
                # self.outcomeaprob = 'Outcome probabilities 90% or 10%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = 100
                self.amountb = 90
                self.proba = 0.9
                self.probb = 1.0
                self.index = 4

        pass
        mm5 = Mm5()

        class Mm6(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes 20¢ or 0¢'
                self.outcomebtext = 'Possible outcome 10¢'
                # self.outcomeaprob = 'Outcome probabilities 50% or 50%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = 20
                self.amountb = 10
                self.proba = 0.5
                self.probb = 1.0
                self.index = 6

        pass
        mm6 = Mm6()

        class Mm7(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes -100¢ or 0¢'
                self.outcomebtext = 'Possible outcome -50¢'
                # self.outcomeaprob = 'Outcome probabilities 50% or 50%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = -100
                self.amountb = -50
                self.proba = 0.5
                self.probb = 1.0
                self.index = 7

        pass
        mm7 = Mm7()

        class Mm8(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes 20¢ or 0¢'
                self.outcomebtext = 'Possible outcome 10¢'
                # self.outcomeaprob = 'Outcome probabilities 80% or 20%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = 20
                self.amountb = 10
                self.proba = 0.8
                self.probb = 1.0
                self.index = 8

        pass
        mm8 = Mm8()

        class Mm9(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes -20¢ or 0¢'
                self.outcomebtext = 'Possible outcome -10¢'
                # self.outcomeaprob = 'Outcome probabilities 80% or 20%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = -20
                self.amountb = -10
                self.proba = 0.8
                self.probb = 1.0
                self.index = 9

        pass
        mm9 = Mm9()

        class Mm10(object):
            def __init__(self):
                self.outcomeatext = 'Possible outcomes 100¢ or 0¢'
                self.outcomebtext = 'Possible outcome 50¢'
                # self.outcomeaprob = 'Outcome probabilities 90% or 10%'
                # self.outcomebprob = 'Outcome probability 100%'
                self.amounta = 100
                self.amountb = 50
                self.proba = 0.9
                self.probb = 1.0
                self.index = 10

        pass
        mm10 = Mm10()


        # randomly set the order of problem sets
        sequence = ["mm1", "mm2", "mm3", "mm4", "mm5", "mm6", "mm7", "mm8", "mm9", "mm10"]
        random.shuffle(sequence)
        realmm1 = sequence[0]
        realmm2 = sequence[1]
        realmm3 = sequence[2]
        realmm4 = sequence[3]
        realmm5 = sequence[4]
        realmm6 = sequence[5]
        realmm7 = sequence[6]
        realmm8 = sequence[7]
        realmm9 = sequence[8]
        realmm10 = sequence[9]

        dictmm = {"mm1": mm1, "mm2": mm2, "mm3": mm3, "mm4": mm4, "mm5": mm5, "mm6": mm6, "mm7": mm7, "mm8": mm8, "mm9": mm9, "mm10": mm10}
        outcomea1 = getattr(dictmm[realmm1], "outcomeatext")
        outcomeb1 = getattr(dictmm[realmm1], "outcomebtext")
        # probtexta1 = getattr(dictmm[realmm1], "outcomeaprob")
        # probtextb1 = getattr(dictmm[realmm1], "outcomebprob")
        amounta1 = getattr(dictmm[realmm1], "amounta")
        amountb1 = getattr(dictmm[realmm1], "amountb")
        proba1 = getattr(dictmm[realmm1], "proba")
        probb1 = getattr(dictmm[realmm1], "probb")


        outcomea2 = getattr(dictmm[realmm2], "outcomeatext")
        outcomeb2 = getattr(dictmm[realmm2], "outcomebtext")
        # probtexta2 = getattr(dictmm[realmm2], "outcomeaprob")
        # probtextb2 = getattr(dictmm[realmm2], "outcomebprob")
        amounta2 = getattr(dictmm[realmm2], "amounta")
        amountb2 = getattr(dictmm[realmm2], "amountb")
        proba2 = getattr(dictmm[realmm2], "proba")
        probb2 = getattr(dictmm[realmm2], "probb")

        outcomea3 = getattr(dictmm[realmm3], "outcomeatext")
        outcomeb3 = getattr(dictmm[realmm3], "outcomebtext")
        # probtexta3 = getattr(dictmm[realmm3], "outcomeaprob")
        # probtextb3 = getattr(dictmm[realmm3], "outcomebprob")
        amounta3 = getattr(dictmm[realmm3], "amounta")
        amountb3 = getattr(dictmm[realmm3], "amountb")
        proba3 = getattr(dictmm[realmm3], "proba")
        probb3 = getattr(dictmm[realmm3], "probb")

        outcomea4 = getattr(dictmm[realmm4], "outcomeatext")
        outcomeb4 = getattr(dictmm[realmm4], "outcomebtext")
        # probtexta4 = getattr(dictmm[realmm4], "outcomeaprob")
        # probtextb4 = getattr(dictmm[realmm4], "outcomebprob")
        amounta4 = getattr(dictmm[realmm4], "amounta")
        amountb4 = getattr(dictmm[realmm4], "amountb")
        proba4 = getattr(dictmm[realmm4], "proba")
        probb4 = getattr(dictmm[realmm4], "probb")

        outcomea5 = getattr(dictmm[realmm5], "outcomeatext")
        outcomeb5 = getattr(dictmm[realmm5], "outcomebtext")
        # probtexta5 = getattr(dictmm[realmm5], "outcomeaprob")
        # probtextb5 = getattr(dictmm[realmm5], "outcomebprob")
        amounta5 = getattr(dictmm[realmm5], "amounta")
        amountb5 = getattr(dictmm[realmm5], "amountb")
        proba5 = getattr(dictmm[realmm5], "proba")
        probb5 = getattr(dictmm[realmm5], "probb")

        outcomea6 = getattr(dictmm[realmm6], "outcomeatext")
        outcomeb6 = getattr(dictmm[realmm6], "outcomebtext")
        # probtexta6 = getattr(dictmm[realmm6], "outcomeaprob")
        # probtextb6 = getattr(dictmm[realmm6], "outcomebprob")
        amounta6 = getattr(dictmm[realmm6], "amounta")
        amountb6 = getattr(dictmm[realmm6], "amountb")
        proba6 = getattr(dictmm[realmm6], "proba")
        probb6 = getattr(dictmm[realmm6], "probb")

        outcomea7 = getattr(dictmm[realmm7], "outcomeatext")
        outcomeb7 = getattr(dictmm[realmm7], "outcomebtext")
        # probtexta7 = getattr(dictmm[realmm7], "outcomeaprob")
        # probtextb7 = getattr(dictmm[realmm7], "outcomebprob")
        amounta7 = getattr(dictmm[realmm7], "amounta")
        amountb7 = getattr(dictmm[realmm7], "amountb")
        proba7 = getattr(dictmm[realmm7], "proba")
        probb7 = getattr(dictmm[realmm7], "probb")

        outcomea8 = getattr(dictmm[realmm8], "outcomeatext")
        outcomeb8 = getattr(dictmm[realmm8], "outcomebtext")
        # probtexta8 = getattr(dictmm[realmm8], "outcomeaprob")
        # probtextb8 = getattr(dictmm[realmm8], "outcomebprob")
        amounta8 = getattr(dictmm[realmm8], "amounta")
        amountb8 = getattr(dictmm[realmm8], "amountb")
        proba8 = getattr(dictmm[realmm8], "proba")
        probb8 = getattr(dictmm[realmm8], "probb")

        outcomea9 = getattr(dictmm[realmm9], "outcomeatext")
        outcomeb9 = getattr(dictmm[realmm9], "outcomebtext")
        # probtexta9 = getattr(dictmm[realmm9], "outcomeaprob")
        # probtextb9 = getattr(dictmm[realmm9], "outcomebprob")
        amounta9 = getattr(dictmm[realmm9], "amounta")
        amountb9 = getattr(dictmm[realmm9], "amountb")
        proba9 = getattr(dictmm[realmm9], "proba")
        probb9 = getattr(dictmm[realmm9], "probb")

        outcomea10 = getattr(dictmm[realmm10], "outcomeatext")
        outcomeb10 = getattr(dictmm[realmm10], "outcomebtext")
        # probtexta10 = getattr(dictmm[realmm10], "outcomeaprob")
        # probtextb10 = getattr(dictmm[realmm10], "outcomebprob")
        amounta10 = getattr(dictmm[realmm10], "amounta")
        amountb10 = getattr(dictmm[realmm10], "amountb")
        proba10 = getattr(dictmm[realmm10], "proba")
        probb10 = getattr(dictmm[realmm10], "probb")


        self.index1 = getattr(dictmm[realmm1], "index")
        self.index2 = getattr(dictmm[realmm2], "index")
        self.index3 = getattr(dictmm[realmm3], "index")
        self.index4 = getattr(dictmm[realmm4], "index")
        self.index5 = getattr(dictmm[realmm5], "index")
        self.index6 = getattr(dictmm[realmm6], "index")
        self.index7 = getattr(dictmm[realmm7], "index")
        self.index8 = getattr(dictmm[realmm8], "index")
        self.index9 = getattr(dictmm[realmm9], "index")
        self.index10 = getattr(dictmm[realmm10], "index")


       # Set up realized outcome & probabilities after randomization in formfields

        aorb1 = random.randint(1, 2)
        if aorb1 == 1:
            self.optiona1 = outcomea1
            self.optionb1 = outcomeb1
            # self.proboptiona1 = probtexta1
            # self.proboptionb1 = probtextb1
            self.realproba1 = proba1
            self.realprobb1 = probb1
            self.realamounta1 = amounta1
            self.realamountb1 = amountb1
        else:
            self.optiona1 = outcomeb1
            self.optionb1 = outcomea1
            # self.proboptiona1 = probtextb1
            # self.proboptionb1 = probtexta1
            self.realproba1 = probb1
            self.realprobb1 = proba1
            self.realamounta1 = amountb1
            self.realamountb1 = amounta1

        aorb2 = random.randint(1, 2)
        if aorb2 == 1:
            self.optiona2 = outcomea2
            self.optionb2 = outcomeb2
            # self.proboptiona2 = probtexta2
            # self.proboptionb2 = probtextb2
            self.realproba2 = proba2
            self.realprobb2 = probb2
            self.realamounta2 = amounta2
            self.realamountb2 = amountb2
        else:
            self.optiona2 = outcomeb2
            self.optionb2 = outcomea2
            # self.proboptiona2 = probtextb2
            # self.proboptionb2 = probtexta2
            self.realproba2 = probb2
            self.realprobb2 = proba2
            self.realamounta2 = amountb2
            self.realamountb2 = amounta2

        aorb3 = random.randint(1, 2)
        if aorb3 == 1:
            self.optiona3 = outcomea3
            self.optionb3 = outcomeb3
            # self.proboptiona3 = probtexta3
            # self.proboptionb3 = probtextb3
            self.realproba3 = proba3
            self.realprobb3 = probb3
            self.realamounta3 = amounta3
            self.realamountb3 = amountb3
        else:
            self.optiona3 = outcomeb3
            self.optionb3 = outcomea3
            # self.proboptiona3 = probtextb3
            # self.proboptionb3 = probtexta3
            self.realproba3 = probb3
            self.realprobb3 = proba3
            self.realamounta3 = amountb3
            self.realamountb3 = amounta3

        aorb4 = random.randint(1, 2)
        if aorb4 == 1:
            self.optiona4 = outcomea4
            self.optionb4 = outcomeb4
            # self.proboptiona4 = probtexta4
            # self.proboptionb4 = probtextb4
            self.realproba4 = proba4
            self.realprobb4 = probb4
            self.realamounta4 = amounta4
            self.realamountb4 = amountb4
        else:
            self.optiona4 = outcomeb4
            self.optionb4 = outcomea4
            # self.proboptiona4 = probtextb4
            # self.proboptionb4 = probtexta4
            self.realproba4 = probb4
            self.realprobb4 = proba4
            self.realamounta4 = amountb4
            self.realamountb4 = amounta4

        aorb5 = random.randint(1, 2)
        if aorb5 == 1:
            self.optiona5 = outcomea5
            self.optionb5 = outcomeb5
            # self.proboptiona5 = probtexta5
            # self.proboptionb5 = probtextb5
            self.realproba5 = proba5
            self.realprobb5 = probb5
            self.realamounta5 = amounta5
            self.realamountb5 = amountb5
        else:
            self.optiona5 = outcomeb5
            self.optionb5 = outcomea5
            # self.proboptiona5 = probtextb5
            # self.proboptionb5 = probtexta5
            self.realproba5 = probb5
            self.realprobb5 = proba5
            self.realamounta5 = amountb5
            self.realamountb5 = amounta5

        aorb6 = random.randint(1, 2)
        if aorb6 == 1:
            self.optiona6 = outcomea6
            self.optionb6 = outcomeb6
            # self.proboptiona6 = probtexta6
            # self.proboptionb6 = probtextb6
            self.realproba6 = proba6
            self.realprobb6 = probb6
            self.realamounta6 = amounta6
            self.realamountb6 = amountb6
        else:
            self.optiona6 = outcomeb6
            self.optionb6 = outcomea6
            # self.proboptiona6 = probtextb6
            # self.proboptionb6 = probtexta6
            self.realproba6 = probb6
            self.realprobb6 = proba6
            self.realamounta6 = amountb6
            self.realamountb6 = amounta6

        aorb7 = random.randint(1, 2)
        if aorb7 == 1:
            self.optiona7 = outcomea7
            self.optionb7 = outcomeb7
            # self.proboptiona7 = probtexta7
            # self.proboptionb7 = probtextb7
            self.realproba7 = proba7
            self.realprobb7 = probb7
            self.realamounta7 = amounta7
            self.realamountb7 = amountb7
        else:
            self.optiona7 = outcomeb7
            self.optionb7 = outcomea7
            # self.proboptiona7 = probtextb7
            # self.proboptionb7 = probtexta7
            self.realproba7 = probb7
            self.realprobb7 = proba7
            self.realamounta7 = amountb7
            self.realamountb7 = amounta7

        aorb8 = random.randint(1, 2)
        if aorb8 == 1:
            self.optiona8 = outcomea8
            self.optionb8 = outcomeb8
            # self.proboptiona8 = probtexta8
            # self.proboptionb8 = probtextb8
            self.realproba8 = proba8
            self.realprobb8 = probb8
            self.realamounta8 = amounta8
            self.realamountb8 = amountb8
        else:
            self.optiona8 = outcomeb8
            self.optionb8 = outcomea8
            # self.proboptiona8 = probtextb8
            # self.proboptionb8 = probtexta8
            self.realproba8 = probb8
            self.realprobb8 = proba8
            self.realamounta8 = amountb8
            self.realamountb8 = amounta8

        aorb9 = random.randint(1, 2)
        if aorb9 == 1:
            self.optiona9 = outcomea9
            self.optionb9 = outcomeb9
            # self.proboptiona9 = probtexta9
            # self.proboptionb9 = probtextb9
            self.realproba9 = proba9
            self.realprobb9 = probb9
            self.realamounta9 = amounta9
            self.realamountb9 = amountb9
        else:
            self.optiona9 = outcomeb9
            self.optionb9 = outcomea9
            # self.proboptiona9 = probtextb9
            # self.proboptionb9 = probtexta9
            self.realproba9 = probb9
            self.realprobb9 = proba9
            self.realamounta9 = amountb9
            self.realamountb9 = amounta9

        aorb10 = random.randint(1, 2)
        if aorb10 == 1:
            self.optiona10 = outcomea10
            self.optionb10 = outcomeb10
            # self.proboptiona10 = probtexta10
            # self.proboptionb10 = probtextb10
            self.realproba10 = proba10
            self.realprobb10 = probb10
            self.realamounta10 = amounta10
            self.realamountb10 = amountb10
        else:
            self.optiona10 = outcomeb10
            self.optionb10 = outcomea10
            # self.proboptiona10 = probtextb10
            # self.proboptionb10 = probtexta10
            self.realproba10 = probb10
            self.realprobb10 = proba10
            self.realamounta10 = amountb10
            self.realamountb10 = amounta10


    # which money machine is chosen by subjects
    mm1 = models.BooleanField(doc = "which money machine button in pair 1 was clicked: 1=machine A; 0=machine B")
    mm2 = models.BooleanField(doc = "which money machine button in pair 2 was clicked: 1=machine A; 0=machine B")
    mm3 = models.BooleanField(doc = "which money machine button in pair 3 was clicked: 1=machine A; 0=machine B")
    mm4 = models.BooleanField(doc = "which money machine button in pair 4 was clicked: 1=machine A; 0=machine B")
    mm5 = models.BooleanField(doc = "which money machine button in pair 5 was clicked: 1=machine A; 0=machine B")
    mm6 = models.BooleanField(doc = "which money machine button in pair 6 was clicked: 1=machine A; 0=machine B")
    mm7 = models.BooleanField(doc = "which money machine button in pair 7 was clicked: 1=machine A; 0=machine B")
    mm8 = models.BooleanField(doc = "which money machine button in pair 8 was clicked: 1=machine A; 0=machine B")
    mm9 = models.BooleanField(doc = "which money machine button in pair 9 was clicked: 1=machine A; 0=machine B")
    mm10 = models.BooleanField(doc = "which money machine button in pair 10 was clicked: 1=machine A; 0=machine B")



    # combine number of clicks and generated sample list to get the real sample seen by subjects

    def getrealsamples1(self):
        samples_a = self.samplemma1.split(",")
        num_samples_a = self.clicksmma1
        self.realsamplea1 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb1.split(",")
        num_samples_b = self.clicksmmb1
        self.realsampleb1 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea1)) <= 1 and len(set(self.realsampleb1)) <= 1:
            self.trivial1 = 1
        else:
            self.trivial1 = 0

    def getrealsamples2(self):
        samples_a = self.samplemma2.split(",")
        num_samples_a = self.clicksmma2
        self.realsamplea2 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb2.split(",")
        num_samples_b = self.clicksmmb2
        self.realsampleb2 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea2)) <= 1 and len(set(self.realsampleb2)) <= 1:
            self.trivial2 = 1
        else:
            self.trivial2 = 0

    def getrealsamples3(self):
        samples_a = self.samplemma3.split(",")
        num_samples_a = self.clicksmma3
        self.realsamplea3 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb3.split(",")
        num_samples_b = self.clicksmmb3
        self.realsampleb3 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea3)) <= 1 and len(set(self.realsampleb3)) <= 1:
            self.trivial3 = 1
        else:
            self.trivial3 = 0

    def getrealsamples4(self):
        samples_a = self.samplemma4.split(",")
        num_samples_a = self.clicksmma4
        self.realsamplea4 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb4.split(",")
        num_samples_b = self.clicksmmb4
        self.realsampleb4 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea4)) <= 1 and len(set(self.realsampleb4)) <= 1:
            self.trivial4 = 1
        else:
            self.trivial4 = 0

    def getrealsamples5(self):
        samples_a = self.samplemma5.split(",")
        num_samples_a = self.clicksmma5
        self.realsamplea5 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb5.split(",")
        num_samples_b = self.clicksmmb5
        self.realsampleb5 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea5)) <= 1 and len(set(self.realsampleb5)) <= 1:
            self.trivial5 = 1
        else:
            self.trivial5 = 0

    def getrealsamples6(self):
        samples_a = self.samplemma6.split(",")
        num_samples_a = self.clicksmma6
        self.realsamplea6 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb6.split(",")
        num_samples_b = self.clicksmmb6
        self.realsampleb6 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea6)) <= 1 and len(set(self.realsampleb6)) <= 1:
            self.trivial6 = 1
        else:
            self.trivial6 = 0

    def getrealsamples7(self):
        samples_a = self.samplemma7.split(",")
        num_samples_a = self.clicksmma7
        self.realsamplea7 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb7.split(",")
        num_samples_b = self.clicksmmb7
        self.realsampleb7 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea7)) <= 1 and len(set(self.realsampleb7)) <= 1:
            self.trivial7 = 1
        else:
            self.trivial7 = 0

    def getrealsamples8(self):
        samples_a = self.samplemma8.split(",")
        num_samples_a = self.clicksmma8
        self.realsamplea8 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb8.split(",")
        num_samples_b = self.clicksmmb8
        self.realsampleb8 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea8)) <= 1 and len(set(self.realsampleb8)) <= 1:
            self.trivial8 = 1
        else:
            self.trivial8 = 0

    def getrealsamples9(self):
        samples_a = self.samplemma9.split(",")
        num_samples_a = self.clicksmma9
        self.realsamplea9 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb9.split(",")
        num_samples_b = self.clicksmmb9
        self.realsampleb9 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea9)) <= 1 and len(set(self.realsampleb9)) <= 1:
            self.trivial9 = 1
        else:
            self.trivial9 = 0

    def getrealsamples10(self):
        samples_a = self.samplemma10.split(",")
        num_samples_a = self.clicksmma10
        self.realsamplea10 = samples_a[0:num_samples_a]
        samples_b = self.samplemmb10.split(",")
        num_samples_b = self.clicksmmb10
        self.realsampleb10 = samples_b[0:num_samples_b]
        if len(set(self.realsamplea10)) <= 1 and len(set(self.realsampleb10)) <= 1:
            self.trivial10 = 1
        else:
            self.trivial10 = 0

    # text shown in the sampling box for Money Machines
    def text1a(self):
        if self.realprobb1 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta1)) + '¢.'

    def text2a(self):
        if self.realprobb2 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta2)) + '¢.'

    def text3a(self):
        if self.realprobb3 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina+ ' ' + str(int(self.realamounta3)) + '¢.'

    def text4a(self):
        if self.realprobb4 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta4)) + '¢.'

    def text5a(self):
        if self.realprobb5 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta5)) + '¢.'

    def text6a(self):
        if self.realprobb6 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta6)) + '¢.'

    def text7a(self):
        if self.realprobb7 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta7)) + '¢.'

    def text8a(self):
        if self.realprobb8 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta8)) + '¢.'

    def text9a(self):
        if self.realprobb9 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta9)) + '¢.'

    def text10a(self):
        if self.realprobb10 == 1.0:
            return Constants.textuncertaina
        return Constants.textcertaina + ' ' + str(int(self.realamounta10)) + '¢.'

    def text1b(self):
        if self.realproba1 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb1)) + '¢.'

    def text2b(self):
        if self.realproba2 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb2)) + '¢.'

    def text3b(self):
        if self.realproba3 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb3)) + '¢.'

    def text4b(self):
        if self.realproba4 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb4)) + '¢.'

    def text5b(self):
        if self.realproba5 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb5)) + '¢.'

    def text6b(self):
        if self.realproba6 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb6)) + '¢.'

    def text7b(self):
        if self.realproba7 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb7)) + '¢.'

    def text8b(self):
        if self.realproba8 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb8)) + '¢.'

    def text9b(self):
        if self.realproba9 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb9)) + '¢.'

    def text10b(self):
        if self.realproba10 == 1.0:
            return Constants.textuncertainb
        return Constants.textcertainb + ' ' + str(int(self.realamountb10)) + '¢.'


    # short text "your sample outcomes" shown in the decision stage underneath the sampling box for Money Machines

    def shorttext1a(self):
        if self.clicksmma1 == 0:
            return ''
        return Constants.shorttext

    def shorttext2a(self):
        if self.clicksmma2 == 0:
            return ''
        return Constants.shorttext

    def shorttext3a(self):
        if self.clicksmma3 == 0:
            return ''
        return Constants.shorttext

    def shorttext4a(self):
        if self.clicksmma4 == 0:
            return ''
        return Constants.shorttext

    def shorttext5a(self):
        if self.clicksmma5 == 0:
            return ''
        return Constants.shorttext

    def shorttext6a(self):
        if self.clicksmma6 == 0:
            return ''
        return Constants.shorttext

    def shorttext7a(self):
        if self.clicksmma7 == 0:
            return ''
        return Constants.shorttext

    def shorttext8a(self):
        if self.clicksmma8 == 0:
            return ''
        return Constants.shorttext

    def shorttext9a(self):
        if self.clicksmma9 == 0:
            return ''
        return Constants.shorttext

    def shorttext10a(self):
        if self.clicksmma10 == 0:
            return ''
        return Constants.shorttext

    def shorttext1b(self):
        if self.clicksmmb1 == 0:
            return ''
        return Constants.shorttext

    def shorttext2b(self):
        if self.clicksmmb2 == 0:
            return ''
        return Constants.shorttext

    def shorttext3b(self):
        if self.clicksmmb3 == 0:
            return ''
        return Constants.shorttext

    def shorttext4b(self):
        if self.clicksmmb4 == 0:
            return ''
        return Constants.shorttext

    def shorttext5b(self):
        if self.clicksmmb5 == 0:
            return ''
        return Constants.shorttext

    def shorttext6b(self):
        if self.clicksmmb6 == 0:
            return ''
        return Constants.shorttext

    def shorttext7b(self):
        if self.clicksmmb7 == 0:
            return ''
        return Constants.shorttext

    def shorttext8b(self):
        if self.clicksmmb8 == 0:
            return ''
        return Constants.shorttext

    def shorttext9b(self):
        if self.clicksmmb9 == 0:
            return ''
        return Constants.shorttext

    def shorttext10b(self):
        if self.clicksmmb10 == 0:
            return ''
        return Constants.shorttext



    # for the color of bad outcome samples shown differently in HTML page
    def getbo(self):
        self.bo1 = min(self.realamounta1, self.realamountb1, 0)
        self.bo2 = min(self.realamounta2, self.realamountb2, 0)
        self.bo3 = min(self.realamounta3, self.realamountb3, 0)
        self.bo4 = min(self.realamounta4, self.realamountb4, 0)
        self.bo5 = min(self.realamounta5, self.realamountb5, 0)
        self.bo6 = min(self.realamounta6, self.realamountb6, 0)
        self.bo7 = min(self.realamounta7, self.realamountb7, 0)
        self.bo8 = min(self.realamounta8, self.realamountb8, 0)
        self.bo9 = min(self.realamounta9, self.realamountb9, 0)
        self.bo10 = min(self.realamounta10, self.realamountb10, 0)


# Choices chosen for the confirmation page for each problem set and the formfield
# mm1 = 1 -> machine A chosen; mm1 = 0 -> machine B chosen

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

    #sample draw parameters of binomial distribution for each pair

    def sa1(self):
        return int(self.realamounta1 * np.random.binomial(1, self.realproba1))

    def sb1(self):
        return int(self.realamountb1 * np.random.binomial(1, self.realprobb1))

    def sa2(self):
        return int(self.realamounta2 * np.random.binomial(1, self.realproba2))

    def sb2(self):
        return int(self.realamountb2 * np.random.binomial(1, self.realprobb2))

    def sa3(self):
        return int(self.realamounta3 * np.random.binomial(1, self.realproba3))

    def sb3(self):
        return int(self.realamountb3 * np.random.binomial(1, self.realprobb3))

    def sa4(self):
        return int(self.realamounta4 * np.random.binomial(1, self.realproba4))

    def sb4(self):
        return int(self.realamountb4 * np.random.binomial(1, self.realprobb4))

    def sa5(self):
        return int(self.realamounta5 * np.random.binomial(1, self.realproba5))

    def sb5(self):
        return int(self.realamountb5 * np.random.binomial(1, self.realprobb5))

    def sa6(self):
        return int(self.realamounta6 * np.random.binomial(1, self.realproba6))

    def sb6(self):
        return int(self.realamountb6 * np.random.binomial(1, self.realprobb6))

    def sa7(self):
        return int(self.realamounta7 * np.random.binomial(1, self.realproba7))

    def sb7(self):
        return int(self.realamountb7 * np.random.binomial(1, self.realprobb7))

    def sa8(self):
        return int(self.realamounta8 * np.random.binomial(1, self.realproba8))

    def sb8(self):
        return int(self.realamountb8 * np.random.binomial(1, self.realprobb8))

    def sa9(self):
        return int(self.realamounta9 * np.random.binomial(1, self.realproba9))

    def sb9(self):
        return int(self.realamountb9 * np.random.binomial(1, self.realprobb9))

    def sa10(self):
        return int(self.realamounta10 * np.random.binomial(1, self.realproba10))

    def sb10(self):
        return int(self.realamountb10 * np.random.binomial(1, self.realprobb10))


    ############ outcome

    def choice11euro(self):
        if self.mm1 == 1:
            return self.optiona1
        return self.optionb1

    def choice12euro(self):
        if self.mm2 == 1:
            return self.optiona2
        return self.optionb2

    def choice13euro(self):
        if self.mm3 == 1:
            return self.optiona3
        return self.optionb3

    def choice14euro(self):
        if self.mm4 == 1:
            return self.optiona4
        return self.optionb4

    def choice15euro(self):
        if self.mm5 == 1:
            return self.optiona5
        return self.optionb5

    def choice16euro(self):
        if self.mm6 == 1:
            return self.optiona6
        return self.optionb6

    def choice17euro(self):
        if self.mm7 == 1:
            return self.optiona7
        return self.optionb7

    def choice18euro(self):
        if self.mm8 == 1:
            return self.optiona8
        return self.optionb8

    def choice19euro(self):
        if self.mm9 == 1:
            return self.optiona9
        return self.optionb9

    def choice110euro(self):
        if self.mm10 == 1:
            return self.optiona10
        return self.optionb10


    # amount for sample draw
    def amount1(self):
        if self.mm1 == 1:
            return self.realamounta1
        return self.realamountb1

    def amount2(self):
        if self.mm2 == 1:
            return self.realamounta2
        return self.realamountb2

    def amount3(self):
        if self.mm3 == 1:
            return self.realamounta3
        return self.realamountb3

    def amount4(self):
        if self.mm4 == 1:
            return self.realamounta4
        return self.realamountb4

    def amount5(self):
        if self.mm5 == 1:
            return self.realamounta5
        return self.realamountb5

    def amount6(self):
        if self.mm6 == 1:
            return self.realamounta6
        return self.realamountb6

    def amount7(self):
        if self.mm7 == 1:
            return self.realamounta7
        return self.realamountb7

    def amount8(self):
        if self.mm8 == 1:
            return self.realamounta8
        return self.realamountb8

    def amount9(self):
        if self.mm9 == 1:
            return self.realamounta9
        return self.realamountb9

    def amount10(self):
        if self.mm10 == 1:
            return self.realamounta10
        return self.realamountb10

    # probabilities for sample draw
    def prob1(self):
        if self.mm1 == 1:
            return self.realproba1
        return self.realprobb1

    def prob2(self):
        if self.mm2 == 1:
            return self.realproba2
        return self.realprobb2

    def prob3(self):
        if self.mm3 == 1:
            return self.realproba3
        return self.realprobb3

    def prob4(self):
        if self.mm4 == 1:
            return self.realproba4
        return self.realprobb4

    def prob5(self):
        if self.mm5 == 1:
            return self.realproba5
        return self.realprobb5

    def prob6(self):
        if self.mm6 == 1:
            return self.realproba6
        return self.realprobb6

    def prob7(self):
        if self.mm7 == 1:
            return self.realproba7
        return self.realprobb7

    def prob8(self):
        if self.mm8 == 1:
            return self.realproba8
        return self.realprobb8

    def prob9(self):
        if self.mm9 == 1:
            return self.realproba9
        return self.realprobb9

    def prob10(self):
        if self.mm10 == 1:
            return self.realproba10
        return self.realprobb10



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

    # def payoffeuroa(self):
    #     if self.randompayoff == 1:
    #         return self.optiona1
    #     elif self.randompayoff == 2:
    #         return self.optiona2
    #     elif self.randompayoff == 3:
    #         return self.optiona3
    #     elif self.randompayoff == 4:
    #         return self.optiona4
    #     elif self.randompayoff == 5:
    #         return self.optiona5
    #     elif self.randompayoff == 6:
    #         return self.optiona6
    #     elif self.randompayoff == 7:
    #         return self.optiona7
    #     elif self.randompayoff == 8:
    #         return self.optiona8
    #     elif self.randompayoff == 9:
    #         return self.optiona9
    #     return self.optiona10
    #
    # def payoffeurob(self):
    #     if self.randompayoff == 1:
    #         return self.optionb1
    #     elif self.randompayoff == 2:
    #         return self.optionb2
    #     elif self.randompayoff == 3:
    #         return self.optionb3
    #     elif self.randompayoff == 4:
    #         return self.optionb4
    #     elif self.randompayoff == 5:
    #         return self.optionb5
    #     elif self.randompayoff == 6:
    #         return self.optionb6
    #     elif self.randompayoff == 7:
    #         return self.optionb7
    #     elif self.randompayoff == 8:
    #         return self.optionb8
    #     elif self.randompayoff == 9:
    #         return self.optionb9
    #     return self.optionb10

    # def payoffprob(self):
    #     if self.randompayoff == 1:
    #         return self.choice11prob()
    #     elif self.randompayoff == 2:
    #         return self.choice12prob()
    #     elif self.randompayoff == 3:
    #         return self.choice13prob()
    #     elif self.randompayoff == 4:
    #         return self.choice14prob()
    #     elif self.randompayoff == 5:
    #         return self.choice15prob()
    #     elif self.randompayoff == 6:
    #         return self.choice16prob()
    #     elif self.randompayoff == 7:
    #         return self.choice17prob()
    #     elif self.randompayoff == 8:
    #         return self.choice18prob()
    #     elif self.randompayoff == 9:
    #         return self.choice19prob()
    #     return self.choice110prob()

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
        if self.ps() < 1:
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


    # define information fields for subjects

    gender = models.CharField(
        choices=['Male', 'Female'],
        widget=widgets.RadioSelect()
    )
    age = models.PositiveIntegerField()

    # completion = models.CharField(doc = "completion code to check if the player finishes the app")




    pass

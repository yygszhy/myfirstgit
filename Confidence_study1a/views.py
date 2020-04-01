from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
# from tkinter import *
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


class Instructions(Page):


    form_model = models.Player
    form_fields = ['clicksmma_ins', 'clicksmmb_ins']


    def before_next_page(self):
        self.player.getmoneymachines()
        self.player.getbo()

    pass

class Instructions2(Page):

    def vars_for_template(self):
        return {
            'num_samplea_ins': self.player.clicksmma_ins,
            'num_sampleb_ins': self.player.clicksmmb_ins,
        }


    pass

class r1p1(Page):

    form_model = models.Player
    form_fields = ['clicksmma1', 'clicksmmb1', 'samplemma1', 'samplemmb1']

    def vars_for_template(self):
        return {
            'sa1': self.player.sa1(),
            'bo1': self.player.bo1,
            'amounta1': round(self.player.realamounta1),
            'amountb1': round(self.player.realamountb1),
            'proba1': self.player.realproba1,
            'probb1': self.player.realprobb1,

        }

    def before_next_page(self):
        self.player.getrealsamples1()

class r1p1_decision(Page):
    form_model = models.Player
    form_fields = ['mm1']

    def vars_for_template(self):
        return {
            'samplea1': self.player.samplemma1,
            'sampleb1': self.player.samplemmb1,
            'num_samplea1': self.player.clicksmma1,
            'num_sampleb1': self.player.clicksmmb1,
            'bo1': self.player.bo1,
            'probb1': self.player.realprobb1,
            'amounta1': round(self.player.realamounta1),
            'amountb1': round(self.player.realamountb1),
        }


class r1p1_result(Page):
    pass

class r1p2(Page):

    form_model = models.Player
    form_fields = ['clicksmma2', 'clicksmmb2', 'samplemma2', 'samplemmb2']

    def vars_for_template(self):
        return {
            'sa2': self.player.sa2(),
            'bo2': self.player.bo2,
            'probb2': self.player.realprobb2,
            'proba2': self.player.realproba2,
            'amounta2': round(self.player.realamounta2),
            'amountb2': round(self.player.realamountb2),
        }

    def before_next_page(self):
        self.player.getrealsamples2()

class r1p2_decision(Page):
    form_model = models.Player
    form_fields = ['mm2']

    def vars_for_template(self):
        return {
            'samplea2': self.player.samplemma2,
            'sampleb2': self.player.samplemmb2,
            'num_samplea2': self.player.clicksmma2,
            'num_sampleb2': self.player.clicksmmb2,
            'bo2': self.player.bo2,
            'probb2': self.player.realprobb2,
            'amounta2': round(self.player.realamounta2),
            'amountb2': round(self.player.realamountb2),
        }



class r1p2_result(Page):
    pass

class r1p3(Page):

    form_model = models.Player
    form_fields = ['clicksmma3', 'clicksmmb3', 'samplemma3', 'samplemmb3']

    def vars_for_template(self):
        return {
            'sa3': self.player.sa3(),
            'bo3': self.player.bo3,
            'probb3': self.player.realprobb3,
            'proba3': self.player.realproba3,
            'amounta3': round(self.player.realamounta3),
            'amountb3': round(self.player.realamountb3),
        }

    def before_next_page(self):
        self.player.getrealsamples3()

class r1p3_decision(Page):
    form_model = models.Player
    form_fields = ['mm3']

    def vars_for_template(self):
        return {
            'samplea3': self.player.samplemma3,
            'sampleb3': self.player.samplemmb3,
            'num_samplea3': self.player.clicksmma3,
            'num_sampleb3': self.player.clicksmmb3,
            'bo3': self.player.bo3,
            'probb3': self.player.realprobb3,
            'amounta3': round(self.player.realamounta3),
            'amountb3': round(self.player.realamountb3),
        }



class r1p3_result(Page):
    pass

class r1p4(Page):
    form_model = models.Player
    form_fields = ['clicksmma4', 'clicksmmb4', 'samplemma4', 'samplemmb4']

    def vars_for_template(self):
        return {
            'sa4': self.player.sa4(),
            'bo4': self.player.bo4,
            'probb4': self.player.realprobb4,
            'proba4': self.player.realproba4,
            'amounta4': round(self.player.realamounta4),
            'amountb4': round(self.player.realamountb4),
        }

    def before_next_page(self):
        self.player.getrealsamples4()

class r1p4_decision(Page):
    form_model = models.Player
    form_fields = ['mm4']

    def vars_for_template(self):
        return {
            'samplea4': self.player.samplemma4,
            'sampleb4': self.player.samplemmb4,
            'num_samplea4': self.player.clicksmma4,
            'num_sampleb4': self.player.clicksmmb4,
            'bo4': self.player.bo4,
            'probb4': self.player.realprobb4,
            'amounta4': round(self.player.realamounta4),
            'amountb4': round(self.player.realamountb4),
        }




class r1p4_result(Page):
    pass

class r1p5(Page):
    form_model = models.Player
    form_fields = ['clicksmma5', 'clicksmmb5', 'samplemma5', 'samplemmb5']

    def vars_for_template(self):
        return {
            'sa5': self.player.sa5(),
            'bo5': self.player.bo5,
            'probb5': self.player.realprobb5,
            'proba5': self.player.realproba5,
            'amounta5': round(self.player.realamounta5),
            'amountb5': round(self.player.realamountb5),
        }

    def before_next_page(self):
        self.player.getrealsamples5()

class r1p5_decision(Page):
    form_model = models.Player
    form_fields = ['mm5']

    def vars_for_template(self):
        return {
            'samplea5': self.player.samplemma5,
            'sampleb5': self.player.samplemmb5,
            'num_samplea5': self.player.clicksmma5,
            'num_sampleb5': self.player.clicksmmb5,
            'bo5': self.player.bo5,
            'probb5': self.player.realprobb5,
            'amounta5': round(self.player.realamounta5),
            'amountb5': round(self.player.realamountb5),
        }



class r1p5_result(Page):
    pass

class r1p6(Page):
    form_model = models.Player
    form_fields = ['clicksmma6', 'clicksmmb6', 'samplemma6', 'samplemmb6']

    def vars_for_template(self):
        return {
            'sa6': self.player.sa6(),
            'bo6': self.player.bo6,
            'probb6': self.player.realprobb6,
            'proba6': self.player.realproba6,
            'amounta6': round(self.player.realamounta6),
            'amountb6': round(self.player.realamountb6),
        }

    def before_next_page(self):
        self.player.getrealsamples6()

class r1p6_decision(Page):
    form_model = models.Player
    form_fields = ['mm6']

    def vars_for_template(self):
        return {
            'samplea6': self.player.samplemma6,
            'sampleb6': self.player.samplemmb6,
            'num_samplea6': self.player.clicksmma6,
            'num_sampleb6': self.player.clicksmmb6,
            'bo6': self.player.bo6,
            'probb6': self.player.realprobb6,
            'amounta6': round(self.player.realamounta6),
            'amountb6': round(self.player.realamountb6),
        }



class r1p6_result(Page):
    pass

class r1p7(Page):
    form_model = models.Player
    form_fields = ['clicksmma7', 'clicksmmb7', 'samplemma7', 'samplemmb7']

    def vars_for_template(self):
        return {
            'sa7': self.player.sa7(),
            'bo7': self.player.bo7,
            'probb7': self.player.realprobb7,
            'proba7': self.player.realproba7,
            'amounta7': round(self.player.realamounta7),
            'amountb7': round(self.player.realamountb7),
        }

    def before_next_page(self):
        self.player.getrealsamples7()

class r1p7_decision(Page):
    form_model = models.Player
    form_fields = ['mm7']

    def vars_for_template(self):
        return {
            'samplea7': self.player.samplemma7,
            'sampleb7': self.player.samplemmb7,
            'num_samplea7': self.player.clicksmma7,
            'num_sampleb7': self.player.clicksmmb7,
            'bo7': self.player.bo7,
            'probb7': self.player.realprobb7,
            'amounta7': round(self.player.realamounta7),
            'amountb7': round(self.player.realamountb7),
        }



class r1p7_result(Page):
    pass

class r1p8(Page):
    form_model = models.Player
    form_fields = ['clicksmma8', 'clicksmmb8', 'samplemma8', 'samplemmb8']

    def vars_for_template(self):
        return {
            'sa8': self.player.sa8(),
            'bo8': self.player.bo8,
            'probb8': self.player.realprobb8,
            'proba8': self.player.realproba8,
            'amounta8': round(self.player.realamounta8),
            'amountb8': round(self.player.realamountb8),
        }

    def before_next_page(self):
        self.player.getrealsamples8()

class r1p8_decision(Page):
    form_model = models.Player
    form_fields = ['mm8']

    def vars_for_template(self):
        return {
            'samplea8': self.player.samplemma8,
            'sampleb8': self.player.samplemmb8,
            'num_samplea8': self.player.clicksmma8,
            'num_sampleb8': self.player.clicksmmb8,
            'bo8': self.player.bo8,
            'probb8': self.player.realprobb8,
            'amounta8': round(self.player.realamounta8),
            'amountb8': round(self.player.realamountb8),
        }



class r1p8_result(Page):
    pass

class r1p9(Page):
    form_model = models.Player
    form_fields = ['clicksmma9', 'clicksmmb9', 'samplemma9', 'samplemmb9']

    def vars_for_template(self):
        return {
            'sa9': self.player.sa9(),
            'bo9': self.player.bo9,
            'probb9': self.player.realprobb9,
            'proba9': self.player.realproba9,
            'amounta9': round(self.player.realamounta9),
            'amountb9': round(self.player.realamountb9),
        }

    def before_next_page(self):
        self.player.getrealsamples9()

class r1p9_decision(Page):
    form_model = models.Player
    form_fields = ['mm9']

    def vars_for_template(self):
        return {
            'samplea9': self.player.samplemma9,
            'sampleb9': self.player.samplemmb9,
            'num_samplea9': self.player.clicksmma9,
            'num_sampleb9': self.player.clicksmmb9,
            'bo9': self.player.bo9,
            'probb9': self.player.realprobb9,
            'amounta9': round(self.player.realamounta9),
            'amountb9': round(self.player.realamountb9),
        }



class r1p9_result(Page):
    pass

class r1p10(Page):
    form_model = models.Player
    form_fields = ['clicksmma10', 'clicksmmb10', 'samplemma10', 'samplemmb10']

    def vars_for_template(self):
        return {
            'sa10': self.player.sa10(),
            'bo10': self.player.bo10,
            'probb10': self.player.realprobb10,
            'proba10': self.player.realproba10,
            'amounta10': round(self.player.realamounta10),
            'amountb10': round(self.player.realamountb10),
        }

    def before_next_page(self):
        self.player.getrealsamples10()

class r1p10_decision(Page):
    form_model = models.Player
    form_fields = ['mm10']

    def vars_for_template(self):
        return {
            'samplea10': self.player.samplemma10,
            'sampleb10': self.player.samplemmb10,
            'num_samplea10': self.player.clicksmma10,
            'num_sampleb10': self.player.clicksmmb10,
            'bo10': self.player.bo10,
            'probb10': self.player.realprobb10,
            'proba10': self.player.realproba10,
            'amounta10': round(self.player.realamounta10),
            'amountb10': round(self.player.realamountb10),
        }



class r1p10_result(Page):
    pass

class s1a_result (Page):
    def before_next_page(self):
        self.player.set_payoffs()



    def vars_for_template(self):
        return {

            'amounta10': round(self.player.realamounta10),
            'amountb10': round(self.player.realamountb10),
            'amounta9': round(self.player.realamounta9),
            'amountb9': round(self.player.realamountb9),
            'amounta8': round(self.player.realamounta8),
            'amountb8': round(self.player.realamountb8),
            'amounta7': round(self.player.realamounta7),
            'amountb7': round(self.player.realamountb7),
            'amounta6': round(self.player.realamounta6),
            'amountb6': round(self.player.realamountb6),
            'amounta5': round(self.player.realamounta5),
            'amountb5': round(self.player.realamountb5),
            'amounta4': round(self.player.realamounta4),
            'amountb4': round(self.player.realamountb4),
            'amounta3': round(self.player.realamounta3),
            'amountb3': round(self.player.realamountb3),
            'amounta2': round(self.player.realamounta2),
            'amountb2': round(self.player.realamountb2),
            'amounta1': round(self.player.realamounta1),
            'amountb1': round(self.player.realamountb1),
            'probb10': self.player.realprobb10,
            'probb9': self.player.realprobb9,
            'probb8': self.player.realprobb8,
            'probb7': self.player.realprobb7,
            'probb6': self.player.realprobb6,
            'probb5': self.player.realprobb5,
            'probb4': self.player.realprobb4,
            'probb3': self.player.realprobb3,
            'probb2': self.player.realprobb2,
            'probb1': self.player.realprobb1,
        }

class s1a_result_2(Page):

    def is_displayed(self):
        return self.player.playmm() == 0

    def vars_for_template(self):
        if self.player.randompayoff == 1:
            payoffmma = round(self.player.realamounta1)
            payoffmmb = round(self.player.realamountb1)
            payoffprobb = self.player.realprobb1
        elif self.player.randompayoff == 2:
            payoffmma = round(self.player.realamounta2)
            payoffmmb = round(self.player.realamountb2)
            payoffprobb = self.player.realprobb2
        elif self.player.randompayoff == 3:
            payoffmma = round(self.player.realamounta3)
            payoffmmb = round(self.player.realamountb3)
            payoffprobb = self.player.realprobb3
        elif self.player.randompayoff == 4:
            payoffmma = round(self.player.realamounta4)
            payoffmmb = round(self.player.realamountb4)
            payoffprobb = self.player.realprobb4
        elif self.player.randompayoff == 5:
            payoffmma = round(self.player.realamounta5)
            payoffmmb = round(self.player.realamountb5)
            payoffprobb = self.player.realprobb5
        elif self.player.randompayoff == 6:
            payoffmma = round(self.player.realamounta6)
            payoffmmb = round(self.player.realamountb6)
            payoffprobb = self.player.realprobb6
        elif self.player.randompayoff == 7:
            payoffmma = round(self.player.realamounta7)
            payoffmmb = round(self.player.realamountb7)
            payoffprobb = self.player.realprobb7
        elif self.player.randompayoff == 8:
            payoffmma = round(self.player.realamounta8)
            payoffmmb = round(self.player.realamountb8)
            payoffprobb = self.player.realprobb8
        elif self.player.randompayoff == 9:
            payoffmma = round(self.player.realamounta9)
            payoffmmb = round(self.player.realamountb9)
            payoffprobb = self.player.realprobb9
        else:
            payoffmma = round(self.player.realamounta10)
            payoffmmb = round(self.player.realamountb10)
            payoffprobb = self.player.realprobb10
        return {
            'payoffmma': payoffmma,
            'payoffmmb': payoffmmb,
            'payoffprobb': payoffprobb,
            'payoffpair': self.player.payoffpair(),
            'payoffpairaorb': self.player.payoffpairaorb(),
            'payoff': round(self.player.payoff),

        }



class s1a_result_3 (Page):
    def is_displayed(self):
        return self.player.playmm() == 1


    def vars_for_template(self):
        if self.player.randompayoff == 1:
            payoffmma = round(self.player.realamounta1)
            payoffmmb = round(self.player.realamountb1)
            payoffprobb = self.player.realprobb1
        elif self.player.randompayoff == 2:
            payoffmma = round(self.player.realamounta2)
            payoffmmb = round(self.player.realamountb2)
            payoffprobb = self.player.realprobb2
        elif self.player.randompayoff == 3:
            payoffmma = round(self.player.realamounta3)
            payoffmmb = round(self.player.realamountb3)
            payoffprobb = self.player.realprobb3
        elif self.player.randompayoff == 4:
            payoffmma = round(self.player.realamounta4)
            payoffmmb = round(self.player.realamountb4)
            payoffprobb = self.player.realprobb4
        elif self.player.randompayoff == 5:
            payoffmma = round(self.player.realamounta5)
            payoffmmb = round(self.player.realamountb5)
            payoffprobb = self.player.realprobb5
        elif self.player.randompayoff == 6:
            payoffmma = round(self.player.realamounta6)
            payoffmmb = round(self.player.realamountb6)
            payoffprobb = self.player.realprobb6
        elif self.player.randompayoff == 7:
            payoffmma = round(self.player.realamounta7)
            payoffmmb = round(self.player.realamountb7)
            payoffprobb = self.player.realprobb7
        elif self.player.randompayoff == 8:
            payoffmma = round(self.player.realamounta8)
            payoffmmb = round(self.player.realamountb8)
            payoffprobb = self.player.realprobb8
        elif self.player.randompayoff == 9:
            payoffmma = round(self.player.realamounta9)
            payoffmmb = round(self.player.realamountb9)
            payoffprobb = self.player.realprobb9
        else:
            payoffmma = round(self.player.realamounta10)
            payoffmmb = round(self.player.realamountb10)
            payoffprobb = self.player.realprobb10
        return {
            'payoffmma': payoffmma,
            'payoffmmb': payoffmmb,
            'payoffprobb': payoffprobb,
            'payoffpair': self.player.payoffpair(),
            'payoffpairaorb': self.player.payoffpairaorb(),
            'payoff': round(self.player.payoff),

        }



class s1a_result_5 (Page):

    # form_model = models.Player
    # form_fields = ['completion']

    def vars_for_template(self):
        a = int(self.player.payoff + Constants.showupfee)
        b = round(a)
        return {
            'totalpayoff': b,
            'payoff': round(self.player.payoff),
            'code': self.participant.code,
        }
    pass


class general(Page):
    form_model = models.Player
    form_fields = ['gender', 'age']

# class finish(Page):
#     pass

page_sequence = [Instructions,
                 Instructions2,
                 r1p1,
                 r1p1_decision,
                 r1p1_result,
                 r1p2,
                 r1p2_decision,
                 r1p2_result,
                 r1p3,
                 r1p3_decision,
                 r1p3_result,
                 r1p4,
                 r1p4_decision,
                 r1p4_result,
                 r1p5,
                 r1p5_decision,
                 r1p5_result,
                 r1p6,
                 r1p6_decision,
                 r1p6_result,
                 r1p7,
                 r1p7_decision,
                 r1p7_result,
                 r1p8,
                 r1p8_decision,
                 r1p8_result,
                 r1p9,
                 r1p9_decision,
                 r1p9_result,
                 r1p10,
                 r1p10_decision,
                 r1p10_result,
                 general,
                 s1a_result,
                 s1a_result_2,
                 s1a_result_3,
                 s1a_result_5,
             #    finish,
                 ]



from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
# from tkinter import *
import simplejson as json
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
import csv
import ast


class tool(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'
    def before_next_page(self):
        self.player.getparameters()
        self.player.getdata1()
        self.player.getdata2()
        self.player.getdata3()
        self.player.getdata4()
        self.player.getdata5()
        self.player.getdata6()
        self.player.getdata7()
        self.player.getdata8()
        self.player.getdata9()
        self.player.getdata10()
        self.group.getdatafortool()
        self.player.getyoked()


class tool2(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['rr_tool', 'confidence_tool']

    def vars_for_template(self):
        return {
            'highcharts_series': json.loads(self.group.data),
        }

class tool3(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    def vars_for_template(self):
        return {
            'highcharts_series': json.loads(self.group.data),
            'rr_tool': round(self.player.rr_tool),
            'confidence_tool': self.player.confidence_tool,
            'rr_go': 100 - round(self.player.rr_tool),
        }

class r1p1(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm1', 'riskthreshold1', 'confidence1']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa1 = ast.literal_eval(yokinglist[Constants.samplesizea1])  # ss = sample size
        ssb1 = ast.literal_eval(yokinglist[Constants.samplesizeb1])
        samplea1 = ast.literal_eval(yokinglist[Constants.samplea1])
        sampleb1 = ast.literal_eval(yokinglist[Constants.sampleb1])
        proboptionb1 = ast.literal_eval(yokinglist[Constants.proboptionb1])
        if proboptionb1 == 1.0:
            theothermachine = "B" # for the wording in the explanation of the highchart
            samplesizea1 = ssa1
            samplesizeb1 = 1
        else:
            theothermachine = "A"
            samplesizea1 = 1
            samplesizeb1 = ssb1
        return {
            'highcharts_series1': json.loads(self.player.data1),
            'samplea1': samplea1,
            'sampleb1': sampleb1,
            'num_samplea1': samplesizea1,
            'num_sampleb1': samplesizeb1,
            'bo1': self.player.bo1,
            'bo1show': round(self.player.bo1),
            'theothermachine': theothermachine,
            'go1': self.player.go1,
            'probb1': proboptionb1,
            'amounta1': self.player.amounta1(),
            'amountb1': self.player.amountb1(),
            'initialc1': self.player.getinitialc1(),
        }



class r1p1_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'
    pass

class r1p2(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm2', 'riskthreshold2', 'confidence2']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa2 = ast.literal_eval(yokinglist[Constants.samplesizea2])  # ss = sample size
        ssb2 = ast.literal_eval(yokinglist[Constants.samplesizeb2])
        samplea2 = ast.literal_eval(yokinglist[Constants.samplea2])
        sampleb2 = ast.literal_eval(yokinglist[Constants.sampleb2])
        proboptionb2 = ast.literal_eval(yokinglist[Constants.proboptionb2])
        if proboptionb2 == 1.0:
            theothermachine = "B"
            samplesizea2 = ssa2
            samplesizeb2 = 1
        else:
            theothermachine = "A"
            samplesizeb2 = ssb2
            samplesizea2 = 1
        return {
            'highcharts_series2': json.loads(self.player.data2),
            'samplea2': samplea2,
            'sampleb2': sampleb2,
            'num_samplea2': samplesizea2,
            'num_sampleb2': samplesizeb2,
            'bo2': self.player.bo2,
            'bo2show': round(self.player.bo2),
            'theothermachine': theothermachine,
            'go2': self.player.go2,
            'probb2': proboptionb2,
            'amounta2': self.player.amounta2(),
            'amountb2': self.player.amountb2(),
            'initialc2': self.player.getinitialc2(),
        }


class r1p2_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'
    pass

class r1p3(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm3', 'riskthreshold3', 'confidence3']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa3 = ast.literal_eval(yokinglist[Constants.samplesizea3])  # ss = sample size
        ssb3 = ast.literal_eval(yokinglist[Constants.samplesizeb3])
        samplea3 = ast.literal_eval(yokinglist[Constants.samplea3])
        sampleb3 = ast.literal_eval(yokinglist[Constants.sampleb3])
        proboptionb3 = ast.literal_eval(yokinglist[Constants.proboptionb3])
        if proboptionb3 == 1.0:
            theothermachine = "B"
            samplesizea3 = ssa3
            samplesizeb3 = 1
        else:
            theothermachine = "A"
            samplesizeb3 = ssb3
            samplesizea3 = 1
        return {
            'highcharts_series3': json.loads(self.player.data3),
            'samplea3': samplea3,
            'sampleb3': sampleb3,
            'num_samplea3': samplesizea3,
            'num_sampleb3': samplesizeb3,
            'bo3': self.player.bo3,
            'bo3show': round(self.player.bo3),
            'theothermachine': theothermachine,
            'go3': self.player.go3,
            'probb3': proboptionb3,
            'amounta3': self.player.amounta3(),
            'amountb3': self.player.amountb3(),
            'initialc3': self.player.getinitialc3(),
        }



class r1p3_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class r1p4(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm4', 'riskthreshold4', 'confidence4']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa4 = ast.literal_eval(yokinglist[Constants.samplesizea4])  # ss = sample size
        ssb4 = ast.literal_eval(yokinglist[Constants.samplesizeb4])
        samplea4 = ast.literal_eval(yokinglist[Constants.samplea4])
        sampleb4 = ast.literal_eval(yokinglist[Constants.sampleb4])
        proboptionb4 = ast.literal_eval(yokinglist[Constants.proboptionb4])
        if proboptionb4 == 1.0:
            theothermachine = "B"
            samplesizea4 = ssa4
            samplesizeb4 = 1
        else:
            theothermachine = "A"
            samplesizeb4 = ssb4
            samplesizea4 = 1
        return {
            'highcharts_series4': json.loads(self.player.data4),
            'samplea4': samplea4,
            'sampleb4': sampleb4,
            'num_samplea4': samplesizea4,
            'num_sampleb4': samplesizeb4,
            'bo4': self.player.bo4,
            'bo4show': round(self.player.bo4),
            'theothermachine': theothermachine,
            'go4': self.player.go4,
            'probb4': proboptionb4,
            'amounta4': self.player.amounta4(),
            'amountb4': self.player.amountb4(),
            'initialc4': self.player.getinitialc4(),
        }



class r1p4_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class r1p5(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm5', 'riskthreshold5', 'confidence5']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa5 = ast.literal_eval(yokinglist[Constants.samplesizea5])
        ssb5 = ast.literal_eval(yokinglist[Constants.samplesizeb5])
        samplea5 = ast.literal_eval(yokinglist[Constants.samplea5])
        sampleb5 = ast.literal_eval(yokinglist[Constants.sampleb5])
        proboptionb5 = ast.literal_eval(yokinglist[Constants.proboptionb5])
        if proboptionb5 == 1.0:
            theothermachine = "B"
            samplesizea5 = ssa5
            samplesizeb5 = 1
        else:
            theothermachine = "A"
            samplesizeb5 = ssb5
            samplesizea5 = 1
        return {
            'highcharts_series5': json.loads(self.player.data5),
            'samplea5': samplea5,
            'sampleb5': sampleb5,
            'num_samplea5': samplesizea5,
            'num_sampleb5': samplesizeb5,
            'bo5': self.player.bo5,
            'bo5show': round(self.player.bo5),
            'theothermachine': theothermachine,
            'go5': self.player.go5,
            'probb5': proboptionb5,
            'amounta5': self.player.amounta5(),
            'amountb5': self.player.amountb5(),
            'initialc5': self.player.getinitialc5(),
        }



class r1p5_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class r1p6(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm6', 'riskthreshold6', 'confidence6']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa6 = ast.literal_eval(yokinglist[Constants.samplesizea6])
        ssb6 = ast.literal_eval(yokinglist[Constants.samplesizeb6])
        samplea6 = ast.literal_eval(yokinglist[Constants.samplea6])
        sampleb6 = ast.literal_eval(yokinglist[Constants.sampleb6])
        proboptionb6 = ast.literal_eval(yokinglist[Constants.proboptionb6])
        if proboptionb6 == 1.0:
            theothermachine = "B"
            samplesizea6 = ssa6
            samplesizeb6 = 1
        else:
            theothermachine = "A"
            samplesizeb6 = ssb6
            samplesizea6 = 1
        return {
            'highcharts_series6': json.loads(self.player.data6),
            'samplea6': samplea6,
            'sampleb6': sampleb6,
            'num_samplea6': samplesizea6,
            'num_sampleb6': samplesizeb6,
            'bo6': self.player.bo6,
            'bo6show': round(self.player.bo6),
            'theothermachine': theothermachine,
            'go6': self.player.go6,
            'probb6': proboptionb6,
            'amounta6': self.player.amounta6(),
            'amountb6': self.player.amountb6(),
            'initialc6': self.player.getinitialc6(),
        }


class r1p6_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class r1p7(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm7', 'riskthreshold7', 'confidence7']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa7 = ast.literal_eval(yokinglist[Constants.samplesizea7])
        ssb7 = ast.literal_eval(yokinglist[Constants.samplesizeb7])
        samplea7 = ast.literal_eval(yokinglist[Constants.samplea7])
        sampleb7 = ast.literal_eval(yokinglist[Constants.sampleb7])
        proboptionb7 = ast.literal_eval(yokinglist[Constants.proboptionb7])
        if proboptionb7 == 1.0:
            theothermachine = "B"
            samplesizea7 = ssa7
            samplesizeb7 = 1
        else:
            theothermachine = "A"
            samplesizeb7 = ssb7
            samplesizea7 = 1
        return {
            'highcharts_series7': json.loads(self.player.data7),
            'samplea7': samplea7,
            'sampleb7': sampleb7,
            'num_samplea7': samplesizea7,
            'num_sampleb7': samplesizeb7,
            'bo7': self.player.bo7,
            'bo7show': round(self.player.bo7),
            'theothermachine': theothermachine,
            'go7': self.player.go7,
            'probb7': proboptionb7,
            'amounta7': self.player.amounta7(),
            'amountb7': self.player.amountb7(),
            'initialc7': self.player.getinitialc7(),
        }



class r1p7_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class r1p8(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm8', 'riskthreshold8', 'confidence8']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa8 = ast.literal_eval(yokinglist[Constants.samplesizea8])
        ssb8 = ast.literal_eval(yokinglist[Constants.samplesizeb8])
        samplea8 = ast.literal_eval(yokinglist[Constants.samplea8])
        sampleb8 = ast.literal_eval(yokinglist[Constants.sampleb8])
        proboptionb8 = ast.literal_eval(yokinglist[Constants.proboptionb8])
        if proboptionb8 == 1.0:
            theothermachine = "B"
            samplesizea8 = ssa8
            samplesizeb8 = 1
        else:
            theothermachine = "A"
            samplesizeb8 = ssb8
            samplesizea8 = 1
        return {
            'highcharts_series8': json.loads(self.player.data8),
            'samplea8': samplea8,
            'sampleb8': sampleb8,
            'num_samplea8': samplesizea8,
            'num_sampleb8': samplesizeb8,
            'bo8': self.player.bo8,
            'bo8show': round(self.player.bo8),
            'theothermachine': theothermachine,
            'go8': self.player.go8,
            'probb8': proboptionb8,
            'amounta8': self.player.amounta8(),
            'amountb8': self.player.amountb8(),
            'initialc8': self.player.getinitialc8(),
        }



class r1p8_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class r1p9(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm9', 'riskthreshold9', 'confidence9']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa9 = ast.literal_eval(yokinglist[Constants.samplesizea9])
        ssb9 = ast.literal_eval(yokinglist[Constants.samplesizeb9])
        samplea9 = ast.literal_eval(yokinglist[Constants.samplea9])
        sampleb9 = ast.literal_eval(yokinglist[Constants.sampleb9])
        proboptionb9 = ast.literal_eval(yokinglist[Constants.proboptionb9])
        if proboptionb9 == 1.0:
            theothermachine = "B"
            samplesizea9 = ssa9
            samplesizeb9 = 1
        else:
            theothermachine = "A"
            samplesizeb9 = ssb9
            samplesizea9 = 1
        return {
            'highcharts_series9': json.loads(self.player.data9),
            'samplea9': samplea9,
            'sampleb9': sampleb9,
            'num_samplea9': samplesizea9,
            'num_sampleb9': samplesizeb9,
            'bo9': self.player.bo9,
            'bo9show': round(self.player.bo9),
            'theothermachine': theothermachine,
            'go9': self.player.go9,
            'probb9': proboptionb9,
            'amounta9': self.player.amounta9(),
            'amountb9': self.player.amountb9(),
            'initialc9': self.player.getinitialc9(),
        }



class r1p9_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class r1p10(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['mm10', 'riskthreshold10', 'confidence10']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        ssa10 = ast.literal_eval(yokinglist[Constants.samplesizea10])
        ssb10 = ast.literal_eval(yokinglist[Constants.samplesizeb10])
        samplea10 = ast.literal_eval(yokinglist[Constants.samplea10])
        sampleb10 = ast.literal_eval(yokinglist[Constants.sampleb10])
        proboptionb10 = ast.literal_eval(yokinglist[Constants.proboptionb10])
        if proboptionb10 == 1.0:
            theothermachine = "B"
            samplesizea10 = ssa10
            samplesizeb10 = 1
        else:
            theothermachine = "A"
            samplesizeb10 = ssb10
            samplesizea10 = 1
        return {
            'highcharts_series10': json.loads(self.player.data10),
            'samplea10': samplea10,
            'sampleb10': sampleb10,
            'num_samplea10': samplesizea10,
            'num_sampleb10': samplesizeb10,
            'bo10': self.player.bo10,
            'bo10show': round(self.player.bo10),
            'theothermachine': theothermachine,
            'go10': self.player.go10,
            'probb10': proboptionb10,
            'amounta10': self.player.amounta10(),
            'amountb10': self.player.amountb10(),
            'initialc10': self.player.getinitialc10(),
        }


class r1p10_result(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    pass

class general(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    form_model = models.Player
    form_fields = ['gender', 'age']

class s1d_result (Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'

    def before_next_page(self):
        self.player.set_payoffs()

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        proboptionb1 = ast.literal_eval(yokinglist[Constants.proboptionb1])
        proboptionb2 = ast.literal_eval(yokinglist[Constants.proboptionb2])
        proboptionb3 = ast.literal_eval(yokinglist[Constants.proboptionb3])
        proboptionb4 = ast.literal_eval(yokinglist[Constants.proboptionb4])
        proboptionb5 = ast.literal_eval(yokinglist[Constants.proboptionb5])
        proboptionb6 = ast.literal_eval(yokinglist[Constants.proboptionb6])
        proboptionb7 = ast.literal_eval(yokinglist[Constants.proboptionb7])
        proboptionb8 = ast.literal_eval(yokinglist[Constants.proboptionb8])
        proboptionb9 = ast.literal_eval(yokinglist[Constants.proboptionb9])
        proboptionb10 = ast.literal_eval(yokinglist[Constants.proboptionb10])
        return {
            'probb10': proboptionb10,
            'probb9': proboptionb9,
            'probb8': proboptionb8,
            'probb7': proboptionb7,
            'probb6': proboptionb6,
            'probb5': proboptionb5,
            'probb4': proboptionb4,
            'probb3': proboptionb3,
            'probb2': proboptionb2,
            'probb1': proboptionb1,
        }

class s1d_result_2(Page):

    def is_displayed(self):
        return self.player.playmm() == 0 and self.participant.vars['treatment'] == 'yellow'


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        mma1 = round(ast.literal_eval(yokinglist[Constants.mma1]))
        mma2 = round(ast.literal_eval(yokinglist[Constants.mma2]))
        mma3 = round(ast.literal_eval(yokinglist[Constants.mma3]))
        mma4 = round(ast.literal_eval(yokinglist[Constants.mma4]))
        mma5 = round(ast.literal_eval(yokinglist[Constants.mma5]))
        mma6 = round(ast.literal_eval(yokinglist[Constants.mma6]))
        mma7 = round(ast.literal_eval(yokinglist[Constants.mma7]))
        mma8 = round(ast.literal_eval(yokinglist[Constants.mma8]))
        mma9 = round(ast.literal_eval(yokinglist[Constants.mma9]))
        mma10 = round(ast.literal_eval(yokinglist[Constants.mma10]))
        mmb1 = round(ast.literal_eval(yokinglist[Constants.mmb1]))
        mmb2 = round(ast.literal_eval(yokinglist[Constants.mmb2]))
        mmb3 = round(ast.literal_eval(yokinglist[Constants.mmb3]))
        mmb4 = round(ast.literal_eval(yokinglist[Constants.mmb4]))
        mmb5 = round(ast.literal_eval(yokinglist[Constants.mmb5]))
        mmb6 = round(ast.literal_eval(yokinglist[Constants.mmb6]))
        mmb7 = round(ast.literal_eval(yokinglist[Constants.mmb7]))
        mmb8 = round(ast.literal_eval(yokinglist[Constants.mmb8]))
        mmb9 = round(ast.literal_eval(yokinglist[Constants.mmb9]))
        mmb10 = round(ast.literal_eval(yokinglist[Constants.mmb10]))
        proboptionb1 = ast.literal_eval(yokinglist[Constants.proboptionb1])
        proboptionb2 = ast.literal_eval(yokinglist[Constants.proboptionb2])
        proboptionb3 = ast.literal_eval(yokinglist[Constants.proboptionb3])
        proboptionb4 = ast.literal_eval(yokinglist[Constants.proboptionb4])
        proboptionb5 = ast.literal_eval(yokinglist[Constants.proboptionb5])
        proboptionb6 = ast.literal_eval(yokinglist[Constants.proboptionb6])
        proboptionb7 = ast.literal_eval(yokinglist[Constants.proboptionb7])
        proboptionb8 = ast.literal_eval(yokinglist[Constants.proboptionb8])
        proboptionb9 = ast.literal_eval(yokinglist[Constants.proboptionb9])
        proboptionb10 = ast.literal_eval(yokinglist[Constants.proboptionb10])
        if self.player.randompayoff == 1:
            payoffa = mma1
            payoffb = mmb1
            opacitya = self.player.opacitya1()
            opacityb = self.player.opacityb1()
            payoffpair = "Pair 1"
            payoffchoice = self.player.choice1()
            probb = proboptionb1
        elif self.player.randompayoff == 2:
            payoffa = mma2
            payoffb = mmb2
            opacitya = self.player.opacitya2()
            opacityb = self.player.opacityb2()
            payoffpair = "Pair 2"
            payoffchoice = self.player.choice2()
            probb = proboptionb2
        elif self.player.randompayoff == 3:
            payoffa = mma3
            payoffb = mmb3
            opacitya = self.player.opacitya3()
            opacityb = self.player.opacityb3()
            payoffpair = "Pair 3"
            payoffchoice = self.player.choice3()
            probb = proboptionb3
        elif self.player.randompayoff == 4:
            payoffa = mma4
            payoffb = mmb4
            opacitya = self.player.opacitya4()
            opacityb = self.player.opacityb4()
            payoffpair = "Pair 4"
            payoffchoice = self.player.choice4()
            probb = proboptionb4
        elif self.player.randompayoff == 5:
            payoffa = mma5
            payoffb = mmb5
            opacitya = self.player.opacitya5()
            opacityb = self.player.opacityb5()
            payoffpair = "Pair 5"
            payoffchoice = self.player.choice5()
            probb = proboptionb5
        elif self.player.randompayoff == 6:
            payoffa = mma6
            payoffb = mmb6
            opacitya = self.player.opacitya6()
            opacityb = self.player.opacityb6()
            payoffpair = "Pair 6"
            payoffchoice = self.player.choice6()
            probb = proboptionb6
        elif self.player.randompayoff == 7:
            payoffa = mma7
            payoffb = mmb7
            opacitya = self.player.opacitya7()
            opacityb = self.player.opacityb7()
            payoffpair = "Pair 7"
            payoffchoice = self.player.choice7()
            probb = proboptionb7
        elif self.player.randompayoff == 8:
            payoffa = mma8
            payoffb = mmb8
            opacitya = self.player.opacitya8()
            opacityb = self.player.opacityb8()
            payoffpair = "Pair 8"
            payoffchoice = self.player.choice8()
            probb = proboptionb8
        elif self.player.randompayoff == 9:
            payoffa = mma9
            payoffb = mmb9
            opacitya = self.player.opacitya9()
            opacityb = self.player.opacityb9()
            payoffpair = "Pair 9"
            payoffchoice = self.player.choice9()
            probb = proboptionb9
        elif self.player.randompayoff == 10:
            payoffa = mma10
            payoffb = mmb10
            opacitya = self.player.opacitya10()
            opacityb = self.player.opacityb10()
            payoffpair = "Pair 10"
            payoffchoice = self.player.choice10()
            probb = proboptionb10
        return {
            'payoffa': payoffa,
            'payoffb': payoffb,
            'opacitya': opacitya,
            'opacityb': opacityb,
            'payoffpair': payoffpair,
            'payoffpairaorb': payoffchoice,
            'payoff': round(self.player.payoff),
            'probb': probb,
        }

class s1d_result_3 (Page):
    def is_displayed(self):
        return self.player.playmm() == 1 and self.participant.vars['treatment'] == 'yellow'

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        mma1 = round(ast.literal_eval(yokinglist[Constants.mma1]))
        mma2 = round(ast.literal_eval(yokinglist[Constants.mma2]))
        mma3 = round(ast.literal_eval(yokinglist[Constants.mma3]))
        mma4 = round(ast.literal_eval(yokinglist[Constants.mma4]))
        mma5 = round(ast.literal_eval(yokinglist[Constants.mma5]))
        mma6 = round(ast.literal_eval(yokinglist[Constants.mma6]))
        mma7 = round(ast.literal_eval(yokinglist[Constants.mma7]))
        mma8 = round(ast.literal_eval(yokinglist[Constants.mma8]))
        mma9 = round(ast.literal_eval(yokinglist[Constants.mma9]))
        mma10 = round(ast.literal_eval(yokinglist[Constants.mma10]))
        mmb1 = round(ast.literal_eval(yokinglist[Constants.mmb1]))
        mmb2 = round(ast.literal_eval(yokinglist[Constants.mmb2]))
        mmb3 = round(ast.literal_eval(yokinglist[Constants.mmb3]))
        mmb4 = round(ast.literal_eval(yokinglist[Constants.mmb4]))
        mmb5 = round(ast.literal_eval(yokinglist[Constants.mmb5]))
        mmb6 = round(ast.literal_eval(yokinglist[Constants.mmb6]))
        mmb7 = round(ast.literal_eval(yokinglist[Constants.mmb7]))
        mmb8 = round(ast.literal_eval(yokinglist[Constants.mmb8]))
        mmb9 = round(ast.literal_eval(yokinglist[Constants.mmb9]))
        mmb10 = round(ast.literal_eval(yokinglist[Constants.mmb10]))
        proboptionb1 = ast.literal_eval(yokinglist[Constants.proboptionb1])
        proboptionb2 = ast.literal_eval(yokinglist[Constants.proboptionb2])
        proboptionb3 = ast.literal_eval(yokinglist[Constants.proboptionb3])
        proboptionb4 = ast.literal_eval(yokinglist[Constants.proboptionb4])
        proboptionb5 = ast.literal_eval(yokinglist[Constants.proboptionb5])
        proboptionb6 = ast.literal_eval(yokinglist[Constants.proboptionb6])
        proboptionb7 = ast.literal_eval(yokinglist[Constants.proboptionb7])
        proboptionb8 = ast.literal_eval(yokinglist[Constants.proboptionb8])
        proboptionb9 = ast.literal_eval(yokinglist[Constants.proboptionb9])
        proboptionb10 = ast.literal_eval(yokinglist[Constants.proboptionb10])
        if self.player.randompayoff == 1:
            payoffa = mma1
            payoffb = mmb1
            opacitya = self.player.opacitya1()
            opacityb = self.player.opacityb1()
            payoffpair = "Pair 1"
            payoffchoice = self.player.choice1()
            probb = proboptionb1
        elif self.player.randompayoff == 2:
            payoffa = mma2
            payoffb = mmb2
            opacitya = self.player.opacitya2()
            opacityb = self.player.opacityb2()
            payoffpair = "Pair 2"
            payoffchoice = self.player.choice2()
            probb = proboptionb2
        elif self.player.randompayoff == 3:
            payoffa = mma3
            payoffb = mmb3
            opacitya = self.player.opacitya3()
            opacityb = self.player.opacityb3()
            payoffpair = "Pair 3"
            payoffchoice = self.player.choice3()
            probb = proboptionb3
        elif self.player.randompayoff == 4:
            payoffa = mma4
            payoffb = mmb4
            opacitya = self.player.opacitya4()
            opacityb = self.player.opacityb4()
            payoffpair = "Pair 4"
            payoffchoice = self.player.choice4()
            probb = proboptionb4
        elif self.player.randompayoff == 5:
            payoffa = mma5
            payoffb = mmb5
            opacitya = self.player.opacitya5()
            opacityb = self.player.opacityb5()
            payoffpair = "Pair 5"
            payoffchoice = self.player.choice5()
            probb = proboptionb5
        elif self.player.randompayoff == 6:
            payoffa = mma6
            payoffb = mmb6
            opacitya = self.player.opacitya6()
            opacityb = self.player.opacityb6()
            payoffpair = "Pair 6"
            payoffchoice = self.player.choice6()
            probb = proboptionb6
        elif self.player.randompayoff == 7:
            payoffa = mma7
            payoffb = mmb7
            opacitya = self.player.opacitya7()
            opacityb = self.player.opacityb7()
            payoffpair = "Pair 7"
            payoffchoice = self.player.choice7()
            probb = proboptionb7
        elif self.player.randompayoff == 8:
            payoffa = mma8
            payoffb = mmb8
            opacitya = self.player.opacitya8()
            opacityb = self.player.opacityb8()
            payoffpair = "Pair 8"
            payoffchoice = self.player.choice8()
            probb = proboptionb8
        elif self.player.randompayoff == 9:
            payoffa = mma9
            payoffb = mmb9
            opacitya = self.player.opacitya9()
            opacityb = self.player.opacityb9()
            payoffpair = "Pair 9"
            payoffchoice = self.player.choice9()
            probb = proboptionb9
        elif self.player.randompayoff == 10:
            payoffa = mma10
            payoffb = mmb10
            opacitya = self.player.opacitya10()
            opacityb = self.player.opacityb10()
            payoffpair = "Pair 10"
            payoffchoice = self.player.choice10()
            probb = proboptionb10
        return {
            'payoffa': payoffa,
            'payoffb': payoffb,
            'opacitya': opacitya,
            'opacityb': opacityb,
            'payoffpair': payoffpair,
            'payoffpairaorb': payoffchoice,
            'payoff': round(self.player.payoff),
            'probb': probb,
        }



class s1d_result_5 (Page):

    # form_model = models.Player
    # form_fields = ['completion']

    def is_displayed(self):
        return self.participant.vars['treatment'] == 'yellow'


    def vars_for_template(self):
        a = int(self.player.payoff + Constants.showupfee)
        b = round(a)
        return {
            'totalpayoff': b,
            'payoff': round(self.player.payoff),
            'code': self.participant.code,
        }
    pass


# class finish(Page):
#
#     def is_displayed(self):
#         return self.participant.vars['treatment'] == 'yellow'
#     pass

page_sequence = [
        tool,
        tool2,
        tool3,
        r1p1,
        r1p1_result,
         r1p2,
         r1p2_result,
         r1p3,
         r1p3_result,
         r1p4,
         r1p4_result,
         r1p5,
         r1p5_result,
         r1p6,
         r1p6_result,
         r1p7,
         r1p7_result,
         r1p8,
         r1p8_result,
         r1p9,
         r1p9_result,
         r1p10,
         r1p10_result,
         general,
         s1d_result,
         s1d_result_2,
         s1d_result_3,
         s1d_result_5,
   # finish,
]

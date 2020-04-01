from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
# from tkinter import *




# sequences of methods matters
class Instructions(Page):
    def before_next_page(self):
        self.player.getbo()
        self.player.getmoneymachine1()
        self.player.getmoneymachine2()
        self.player.getmoneymachine3()
        self.player.getmoneymachine4()
        self.player.getmoneymachine5()
        self.player.getmoneymachine6()
        self.player.getmoneymachine7()
        self.player.getmoneymachine8()
        self.player.getmoneymachine9()
        self.player.getmoneymachine10()
        self.player.getyoked()
        self.player.setactive()


    def vars_for_template(self):
        return {
            'yokinglist': self.participant.vars['yokinglist'],
        }


    pass

class Instructions2(Page):
    def before_next_page(self):
        self.player.checkactive()
    pass

class r1p1(Page):
    form_model = models.Player
    form_fields = ['mm1']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb1))
        return {
            'amounta1': round(self.player.amounta1),
            'amountb1': round(self.player.amountb1),
            'proba1': self.player.proba1,
            'probb1': self.player.probb1,
            'realprobb': realprobb,
        }



class r1p1_result(Page):
    pass


class r1p2(Page):
    form_model = models.Player
    form_fields = ['mm2']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb2))
        return {
            'amounta2': round(self.player.amounta2),
            'amountb2': round(self.player.amountb2),
            'proba2': self.player.proba2,
            'probb2': self.player.probb2,
            'realprobb': realprobb,
        }




class r1p2_result(Page):
    pass


class r1p3(Page):
    form_model = models.Player
    form_fields = ['mm3']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb3))
        return {
            'amounta3': round(self.player.amounta3),
            'amountb3': round(self.player.amountb3),
            'proba3': self.player.proba3,
            'probb3': self.player.probb3,
            'realprobb': realprobb,
        }



class r1p3_result(Page):
    pass

class r1p4(Page):
    form_model = models.Player
    form_fields = ['mm4']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb4))
        return {
            'amounta4': round(self.player.amounta4),
            'amountb4': round(self.player.amountb4),
            'proba4': self.player.proba4,
            'probb4': self.player.probb4,
            'realprobb': realprobb,
        }



class r1p4_result(Page):
    pass

class r1p5(Page):
    form_model = models.Player
    form_fields = ['mm5']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb5))
        return {
            'amounta5': round(self.player.amounta5),
            'amountb5': round(self.player.amountb5),
            'proba5': self.player.proba5,
            'probb5': self.player.probb5,
            'realprobb': realprobb,
        }


class r1p5_result(Page):
    pass

class r1p6(Page):
    form_model = models.Player
    form_fields = ['mm6']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb6))
        return {
            'amounta6': round(self.player.amounta6),
            'amountb6': round(self.player.amountb6),
            'proba6': self.player.proba6,
            'probb6': self.player.probb6,
            'realprobb': realprobb,
        }



class r1p6_result(Page):
    pass

class r1p7(Page):
    form_model = models.Player
    form_fields = ['mm7']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb7))
        return {
            'amounta7': round(self.player.amounta7),
            'amountb7': round(self.player.amountb7),
            'proba7': self.player.proba7,
            'probb7': self.player.probb7,
            'realprobb': realprobb,
        }


class r1p7_result(Page):
    pass

class r1p8(Page):
    form_model = models.Player
    form_fields = ['mm8']

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb8))
        return {
            'amounta8': round(self.player.amounta8),
            'amountb8': round(self.player.amountb8),
            'proba8': self.player.proba8,
            'probb8': self.player.probb8,
            'realprobb': realprobb,
        }



class r1p8_result(Page):
    pass

class r1p9(Page):
    form_model = models.Player
    form_fields = ['mm9']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb9))
        return {
            'amounta9': round(self.player.amounta9),
            'amountb9': round(self.player.amountb9),
            'proba9': self.player.proba9,
            'probb9': self.player.probb9,
            'realprobb': realprobb,
        }



class r1p9_result(Page):
    pass

class r1p10(Page):
    form_model = models.Player
    form_fields = ['mm10']


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
        realprobb = float(yokinglist.get(Constants.probb10))
        return {
            'amounta10': round(self.player.amounta10),
            'amountb10': round(self.player.amountb10),
            'proba10': self.player.proba10,
            'probb10': self.player.probb10,
            'realprobb': realprobb,
        }


class r1p10_result(Page):
    pass

class s1b_result (Page):
    def before_next_page(self):
        self.player.set_payoffs()

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
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
        return {
            'amounta1': round(self.player.amounta1),
            'amountb1': round(self.player.amountb1),
            'proba1': self.player.proba1,
            'probb1': self.player.probb1,
            'amounta2': round(self.player.amounta2),
            'amountb2': round(self.player.amountb2),
            'proba2': self.player.proba2,
            'probb2': self.player.probb2,
            'amounta3': round(self.player.amounta3),
            'amountb3': round(self.player.amountb3),
            'proba3': self.player.proba3,
            'probb3': self.player.probb3,
            'amounta4': round(self.player.amounta4),
            'amountb4': round(self.player.amountb4),
            'proba4': self.player.proba4,
            'probb4': self.player.probb4,
            'amounta5': round(self.player.amounta5),
            'amountb5': round(self.player.amountb5),
            'proba5': self.player.proba5,
            'probb5': self.player.probb5,
            'amounta6': round(self.player.amounta6),
            'amountb6': round(self.player.amountb6),
            'proba6': self.player.proba6,
            'probb6': self.player.probb6,
            'amounta7': round(self.player.amounta7),
            'amountb7': round(self.player.amountb7),
            'proba7': self.player.proba7,
            'probb7': self.player.probb7,
            'amounta8': round(self.player.amounta8),
            'amountb8': round(self.player.amountb8),
            'proba8': self.player.proba8,
            'probb8': self.player.probb8,
            'amounta9': round(self.player.amounta9),
            'amountb9': round(self.player.amountb9),
            'proba9': self.player.proba9,
            'probb9': self.player.probb9,
            'amounta10': round(self.player.amounta10),
            'amountb10': round(self.player.amountb10),
            'proba10': self.player.proba10,
            'probb10': self.player.probb10,
            'realprobb1': realprobb1,
            'realprobb2': realprobb2,
            'realprobb3': realprobb3,
            'realprobb4': realprobb4,
            'realprobb5': realprobb5,
            'realprobb6': realprobb6,
            'realprobb7': realprobb7,
            'realprobb8': realprobb8,
            'realprobb9': realprobb9,
            'realprobb10': realprobb10,
        }

class s1b_result_2(Page):

    def is_displayed(self):
        return self.player.playmm() == 0

    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
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
        if self.player.randompayoff == 1:
            payoffa = round(self.player.amounta1)
            payoffb = round(self.player.amountb1)
            probau = self.player.proboptiona1u
            probad = self.player.proboptiona1d
            probbu = self.player.proboptionb1u
            probbd = self.player.proboptionb1d
            payoffpair = "Pair 1"
            payoffchoice = self.player.choice1()
            realprobb = realprobb1
        elif self.player.randompayoff == 2:
            payoffa = round(self.player.amounta2)
            payoffb = round(self.player.amountb2)
            probau = self.player.proboptiona2u
            probad = self.player.proboptiona2d
            probbu = self.player.proboptionb2u
            probbd = self.player.proboptionb2d
            payoffpair = "Pair 2"
            payoffchoice = self.player.choice2()
            realprobb = realprobb2
        elif self.player.randompayoff == 3:
            payoffa = round(self.player.amounta3)
            payoffb = round(self.player.amountb3)
            probau = self.player.proboptiona3u
            probad = self.player.proboptiona3d
            probbu = self.player.proboptionb3u
            probbd = self.player.proboptionb3d
            payoffpair = "Pair 3"
            payoffchoice = self.player.choice3()
            realprobb = realprobb3
        elif self.player.randompayoff == 4:
            payoffa = round(self.player.amounta4)
            payoffb = round(self.player.amountb4)
            probau = self.player.proboptiona4u
            probad = self.player.proboptiona4d
            probbu = self.player.proboptionb4u
            probbd = self.player.proboptionb4d
            payoffpair = "Pair 4"
            payoffchoice = self.player.choice4()
            realprobb = realprobb4
        elif self.player.randompayoff == 5:
            payoffa = round(self.player.amounta5)
            payoffb = round(self.player.amountb5)
            probau = self.player.proboptiona5u
            probad = self.player.proboptiona5d
            probbu = self.player.proboptionb5u
            probbd = self.player.proboptionb5d
            payoffpair = "Pair 5"
            payoffchoice = self.player.choice5()
            realprobb = realprobb5
        elif self.player.randompayoff == 6:
            payoffa = round(self.player.amounta6)
            payoffb = round(self.player.amountb6)
            probau = self.player.proboptiona6u
            probad = self.player.proboptiona6d
            probbu = self.player.proboptionb6u
            probbd = self.player.proboptionb6d
            payoffpair = "Pair 6"
            payoffchoice = self.player.choice6()
            realprobb = realprobb6
        elif self.player.randompayoff == 7:
            payoffa = round(self.player.amounta7)
            payoffb = round(self.player.amountb7)
            probau = self.player.proboptiona7u
            probad = self.player.proboptiona7d
            probbu = self.player.proboptionb7u
            probbd = self.player.proboptionb7d
            payoffpair = "Pair 7"
            payoffchoice = self.player.choice7()
            realprobb = realprobb7
        elif self.player.randompayoff == 8:
            payoffa = round(self.player.amounta8)
            payoffb = round(self.player.amountb8)
            probau = self.player.proboptiona8u
            probad = self.player.proboptiona8d
            probbu = self.player.proboptionb8u
            probbd = self.player.proboptionb8d
            payoffpair = "Pair 8"
            payoffchoice = self.player.choice8()
            realprobb = realprobb8
        elif self.player.randompayoff == 9:
            payoffa = round(self.player.amounta9)
            payoffb = round(self.player.amountb9)
            probau = self.player.proboptiona9u
            probad = self.player.proboptiona9d
            probbu = self.player.proboptionb9u
            probbd = self.player.proboptionb9d
            payoffpair = "Pair 9"
            payoffchoice = self.player.choice9()
            realprobb = realprobb9
        elif self.player.randompayoff == 10:
            payoffa = round(self.player.amounta10)
            payoffb = round(self.player.amountb10)
            probau = self.player.proboptiona10u
            probad = self.player.proboptiona10d
            probbu = self.player.proboptionb10u
            probbd = self.player.proboptionb10d
            payoffpair = "Pair 10"
            payoffchoice = self.player.choice10()
            realprobb = realprobb10
        return {
        'payoffa': payoffa,
        'payoffb': payoffb,
        'payoffpair': payoffpair,
        'payoffpairaorb': payoffchoice,
        'payoff': round(self.player.payoff),
        'realprobb': realprobb,
        'payoff_probau': probau,
        'payoff_probad': probad,
        'payoff_probbu': probbu,
        'payoff_probbd': probbd,
        }

class s1b_result_3 (Page):

    def is_displayed(self):
        return self.player.playmm() == 1


    def vars_for_template(self):
        yokinglist = self.participant.vars['yokinglist']
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
        if self.player.randompayoff == 1:
            payoffa = round(self.player.amounta1)
            payoffb = round(self.player.amountb1)
            probau = self.player.proboptiona1u
            probad = self.player.proboptiona1d
            probbu = self.player.proboptionb1u
            probbd = self.player.proboptionb1d
            payoffpair = "Pair 1"
            payoffchoice = self.player.choice1()
            realprobb = realprobb1
        elif self.player.randompayoff == 2:
            payoffa = round(self.player.amounta2)
            payoffb = round(self.player.amountb2)
            probau = self.player.proboptiona2u
            probad = self.player.proboptiona2d
            probbu = self.player.proboptionb2u
            probbd = self.player.proboptionb2d
            payoffpair = "Pair 2"
            payoffchoice = self.player.choice2()
            realprobb = realprobb2
        elif self.player.randompayoff == 3:
            payoffa = round(self.player.amounta3)
            payoffb = round(self.player.amountb3)
            probau = self.player.proboptiona3u
            probad = self.player.proboptiona3d
            probbu = self.player.proboptionb3u
            probbd = self.player.proboptionb3d
            payoffpair = "Pair 3"
            payoffchoice = self.player.choice3()
            realprobb = realprobb3
        elif self.player.randompayoff == 4:
            payoffa = round(self.player.amounta4)
            payoffb = round(self.player.amountb4)
            probau = self.player.proboptiona4u
            probad = self.player.proboptiona4d
            probbu = self.player.proboptionb4u
            probbd = self.player.proboptionb4d
            payoffpair = "Pair 4"
            payoffchoice = self.player.choice4()
            realprobb = realprobb4
        elif self.player.randompayoff == 5:
            payoffa = round(self.player.amounta5)
            payoffb = round(self.player.amountb5)
            probau = self.player.proboptiona5u
            probad = self.player.proboptiona5d
            probbu = self.player.proboptionb5u
            probbd = self.player.proboptionb5d
            payoffpair = "Pair 5"
            payoffchoice = self.player.choice5()
            realprobb = realprobb5
        elif self.player.randompayoff == 6:
            payoffa = round(self.player.amounta6)
            payoffb = round(self.player.amountb6)
            probau = self.player.proboptiona6u
            probad = self.player.proboptiona6d
            probbu = self.player.proboptionb6u
            probbd = self.player.proboptionb6d
            payoffpair = "Pair 6"
            payoffchoice = self.player.choice6()
            realprobb = realprobb6
        elif self.player.randompayoff == 7:
            payoffa = round(self.player.amounta7)
            payoffb = round(self.player.amountb7)
            probau = self.player.proboptiona7u
            probad = self.player.proboptiona7d
            probbu = self.player.proboptionb7u
            probbd = self.player.proboptionb7d
            payoffpair = "Pair 7"
            payoffchoice = self.player.choice7()
            realprobb = realprobb7
        elif self.player.randompayoff == 8:
            payoffa = round(self.player.amounta8)
            payoffb = round(self.player.amountb8)
            probau = self.player.proboptiona8u
            probad = self.player.proboptiona8d
            probbu = self.player.proboptionb8u
            probbd = self.player.proboptionb8d
            payoffpair = "Pair 8"
            payoffchoice = self.player.choice8()
            realprobb = realprobb8
        elif self.player.randompayoff == 9:
            payoffa = round(self.player.amounta9)
            payoffb = round(self.player.amountb9)
            probau = self.player.proboptiona9u
            probad = self.player.proboptiona9d
            probbu = self.player.proboptionb9u
            probbd = self.player.proboptionb9d
            payoffpair = "Pair 9"
            payoffchoice = self.player.choice9()
            realprobb = realprobb9
        elif self.player.randompayoff == 10:
            payoffa = round(self.player.amounta10)
            payoffb = round(self.player.amountb10)
            probau = self.player.proboptiona10u
            probad = self.player.proboptiona10d
            probbu = self.player.proboptionb10u
            probbd = self.player.proboptionb10d
            payoffpair = "Pair 10"
            payoffchoice = self.player.choice10()
            realprobb = realprobb10
        return {
            'payoffa': payoffa,
            'payoffb': payoffb,
            'payoffpair': payoffpair,
            'payoffpairaorb': payoffchoice,
            'payoff': round(self.player.payoff),
            'realprobb': realprobb,
            'payoff_probau': probau,
            'payoff_probad': probad,
            'payoff_probbu': probbu,
            'payoff_probbd': probbd,
        }




class s1b_result_5 (Page):



    def vars_for_template(self):
        a = int(self.player.payoff + Constants.showupfee)
        b = round(a)
        return {
            'totalpayoff': b,
            'payoff': round(self.player.payoff),
        }

    pass



class general(Page):
    form_model = models.Player
    form_fields = ['gender', 'age']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.sweepstakes()

    title_text = " "
    body_text = "Please remain seated and silent. The outcome of the lottery will be displayed on this screen as soon as everyone finished."


class sweepstakeresult0 (Page):

    def is_displayed(self):
        return self.player.sswin() == 0

class sweepstakeresult1 (Page):

    def is_displayed(self):
        return self.player.sswin() == 1


page_sequence = [#MyWaitPage,
                 Instructions,
                 Instructions2,
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
                 s1b_result,
                 s1b_result_2,
                 s1b_result_3,
                 s1b_result_5,
                 #ResultsWaitPage,
                 #sweepstakeresult0,
                 #sweepstakeresult1,
                 ]



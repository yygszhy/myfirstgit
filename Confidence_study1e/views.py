from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# sequences of methods matters
class Instructions(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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


    def vars_for_template(self):
        return {
            'yokinglist': self.participant.vars['yokinglist'],
        }


    pass

class Instructions2(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p1(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass


class r1p2(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass


class r1p3(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p4(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p5(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p6(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p7(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p8(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p9(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class r1p10(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    pass

class s1b_result (Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
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
        return self.player.playmm() == 0 and self.participant.vars['treatment'] == 'blue'

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
            payoff_samplesize_a = self.player.samplesizemma1
            payoff_samplesize_b = self.player.samplesizemmb1
            payoff_text_a = self.player.texta1()
            payoff_text_b = self.player.textb1()
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
            payoff_samplesize_a = self.player.samplesizemma2
            payoff_samplesize_b = self.player.samplesizemmb2
            payoff_text_a = self.player.texta2()
            payoff_text_b = self.player.textb2()
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
            payoff_samplesize_a = self.player.samplesizemma3
            payoff_samplesize_b = self.player.samplesizemmb3
            payoff_text_a = self.player.texta3()
            payoff_text_b = self.player.textb3()
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
            payoff_samplesize_a = self.player.samplesizemma4
            payoff_samplesize_b = self.player.samplesizemmb4
            payoff_text_a = self.player.texta4()
            payoff_text_b = self.player.textb4()
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
            payoff_samplesize_a = self.player.samplesizemma5
            payoff_samplesize_b = self.player.samplesizemmb5
            payoff_text_a = self.player.texta5()
            payoff_text_b = self.player.textb5()
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
            payoff_samplesize_a = self.player.samplesizemma6
            payoff_samplesize_b = self.player.samplesizemmb6
            payoff_text_a = self.player.texta6()
            payoff_text_b = self.player.textb6()
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
            payoff_samplesize_a = self.player.samplesizemma7
            payoff_samplesize_b = self.player.samplesizemmb7
            payoff_text_a = self.player.texta7()
            payoff_text_b = self.player.textb7()
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
            payoff_samplesize_a = self.player.samplesizemma8
            payoff_samplesize_b = self.player.samplesizemmb8
            payoff_text_a = self.player.texta8()
            payoff_text_b = self.player.textb8()
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
            payoff_samplesize_a = self.player.samplesizemma9
            payoff_samplesize_b = self.player.samplesizemmb9
            payoff_text_a = self.player.texta9()
            payoff_text_b = self.player.textb9()
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
            payoff_samplesize_a = self.player.samplesizemma10
            payoff_samplesize_b = self.player.samplesizemmb10
            payoff_text_a = self.player.texta10()
            payoff_text_b = self.player.textb10()
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
        'payoff_text_a': payoff_text_a,
        'payoff_text_b': payoff_text_b,
        'payoff_samplesize_a': payoff_samplesize_a,
        'payoff_samplesize_b': payoff_samplesize_b,
        }

class s1b_result_3 (Page):

    def is_displayed(self):
        return self.player.playmm() == 1 and self.participant.vars['treatment'] == 'blue'


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
            payoff_samplesize_a = self.player.samplesizemma1
            payoff_samplesize_b = self.player.samplesizemmb1
            payoff_text_a = self.player.texta1()
            payoff_text_b = self.player.textb1()
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
            payoff_samplesize_a = self.player.samplesizemma2
            payoff_samplesize_b = self.player.samplesizemmb2
            payoff_text_a = self.player.texta2()
            payoff_text_b = self.player.textb2()
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
            payoff_samplesize_a = self.player.samplesizemma3
            payoff_samplesize_b = self.player.samplesizemmb3
            payoff_text_a = self.player.texta3()
            payoff_text_b = self.player.textb3()
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
            payoff_samplesize_a = self.player.samplesizemma4
            payoff_samplesize_b = self.player.samplesizemmb4
            payoff_text_a = self.player.texta4()
            payoff_text_b = self.player.textb4()
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
            payoff_samplesize_a = self.player.samplesizemma5
            payoff_samplesize_b = self.player.samplesizemmb5
            payoff_text_a = self.player.texta5()
            payoff_text_b = self.player.textb5()
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
            payoff_samplesize_a = self.player.samplesizemma6
            payoff_samplesize_b = self.player.samplesizemmb6
            payoff_text_a = self.player.texta6()
            payoff_text_b = self.player.textb6()
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
            payoff_samplesize_a = self.player.samplesizemma7
            payoff_samplesize_b = self.player.samplesizemmb7
            payoff_text_a = self.player.texta7()
            payoff_text_b = self.player.textb7()
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
            payoff_samplesize_a = self.player.samplesizemma8
            payoff_samplesize_b = self.player.samplesizemmb8
            payoff_text_a = self.player.texta8()
            payoff_text_b = self.player.textb8()
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
            payoff_samplesize_a = self.player.samplesizemma9
            payoff_samplesize_b = self.player.samplesizemmb9
            payoff_text_a = self.player.texta9()
            payoff_text_b = self.player.textb9()
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
            payoff_samplesize_a = self.player.samplesizemma10
            payoff_samplesize_b = self.player.samplesizemmb10
            payoff_text_a = self.player.texta10()
            payoff_text_b = self.player.textb10()
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
            'payoff_text_a':payoff_text_a,
            'payoff_text_b':payoff_text_b,
            'payoff_samplesize_a':payoff_samplesize_a,
            'payoff_samplesize_b':payoff_samplesize_b,
        }

class s1b_result_5 (Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'

    # form_model = models.Player
    # form_fields = ['completion']

    def vars_for_template(self):
        a = int(self.player.payoff + Constants.showupfee)
        b = round(a)
        # if self.player == self.group.sweepstakes():
        #     result = "win"
        # else:
        #     result = "lost"
        return {
            'totalpayoff': b,
            'payoff': round(self.player.payoff),
            'code': self.participant.code,
         #   'result': self.group.sweepstakes(),
        }

    pass


# class finish(Page):
#     def is_displayed(self):
#         return self.participant.vars['treatment'] == 'blue'
#     pass



class general(Page):
    def is_displayed(self):
        return self.participant.vars['treatment'] == 'blue'
    form_model = models.Player
    form_fields = ['gender', 'age']

page_sequence = [Instructions,
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
      #           finish,
                 ]



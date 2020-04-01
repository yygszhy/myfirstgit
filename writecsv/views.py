from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def vars_for_template(self):
        return{'questOrder':self.participant.vars['questOrder']}


class MyPage2(Page):
    pass


class ResultsWaitPage(WaitPage):
        pass


class Results(Page):

    def is_displayed(self):
        # returns True if ...
        return self.round_number == 3


page_sequence = [
    MyPage,
    MyPage2,
    Results
]

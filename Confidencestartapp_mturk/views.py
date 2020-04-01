from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    #
    # form_model = models.Player
    # form_fields = ['active']
    #
    # def before_next_page(self):
    #     self.player.setactive()
    #     self.player.checkactive()

    pass


page_sequence = [
    MyPage,
    # ResultsWaitPage,
    # Results
]

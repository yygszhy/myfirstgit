from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Instructions)
        yield (views.Instructions_r1)
        yield (views.r1p1)
        yield (views.r1p1_result)
        yield (views.r1p2)
        yield (views.r1p2_result)
        yield (views.r1p3)
        yield (views.r1p3_result)
        yield (views.r1p4)
        yield (views.r1p4_result)
        yield (views.r1p5)
        yield (views.r1p5_result)
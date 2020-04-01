from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Feibai'

doc = """
Confidencestartapp - randomization of study1b, 1c and 1d condition
"""


class Constants(BaseConstants):
    name_in_url = 'Confidencestartapp_mturk'
    players_per_group = None
    num_rounds = 1
    showupfee = 10



class Subsession(BaseSubsession):

    # Condition b/c/d randomization
    # blue = condition 1b
    # red = condition 1c
    # yellow = condition 1d

    def creating_session(self):
      #  colors = itertools.cycle(['blue', 'red', 'yellow'])
        # randomize to treatments
        for player in self.get_players():
            player.participant.vars['treatment'] = 'blue'


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # active = models.BooleanField(doc='real player=true', initial=False)
    #
    # def setactive(self):
    #     self.active = True
    #
    # def checkactive(self):
    #     if self.active == True:
    #         self.participant.vars['active'] = 1
    #     else:
    #         self.participant.vars['active'] = 0

    pass
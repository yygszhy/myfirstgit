from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np


doc = """
Confidencefinishapp - sweepstakes
"""


class Constants(BaseConstants):
    name_in_url = 'confidencefinish'
    players_per_group = None
    num_rounds = 1
    showupfee = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    winner = models.IntegerField(
        doc="one player is chosen by sweepstakes")
    # self.get_players() = [<Player 1>, <Player 2>, <Player 3>, <Player 4>, <Player 5>, <Player 6>, <Player 7>, <Player 8>, <Player 9>, <Player 10>]
    # all payoffs have to be positive. can't have negative payoff.
    def sweepstakes(self):
        if self.session.config['sweepstakes'] == 1:
            stake0 = []
            # get total points of all players (i.e. all points earned + base pay)
            # groupsum = sum(p.mystake for p in self.get_players())
            for p in self.get_players():
                p.mystake = p.participant.vars.get('sweepstake')
            groupsum = sum(p.mystake for p in self.get_players())
            # get number of the players
            num_players = len(self.get_players())
            # for each player, his stake = his points (earned + base pay) / total points of all players
            stake0.append((p.mystake / groupsum) for p in self.get_players())
            # put all individual stakes as a list of probabilities of being drawn. e.g. (0.1, 0.2, 0.3, 0.2, 0.2)
            stake = [list(float(y) for y in x) for x in stake0][0]
            # draw one number from 1 to number of players (python list starts from 0, that's why +1), based on the list of probabilities
            # list of probabilities corresponds to the stake of each individual
            self.winner = np.random.choice(np.arange(1, num_players+1), p=stake)
        else:
            self.winner = 999


class Player(BasePlayer):

    mystake = models.IntegerField()

    # pass stake data from previous apps via participant.vars
    # sweepstake is the final points including 10 points endowment for each player
    def getstake(self):
        self.mystake = self.participant.vars.get('sweepstake')

    def sswin(self):
        if self.id_in_group == self.group.winner:
            return 1
        else:
            return 0
    pass



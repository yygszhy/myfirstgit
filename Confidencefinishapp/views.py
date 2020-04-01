from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    title_text = " "
    body_text = "Please remain seated and silent. The outcome of the lottery will be displayed on this screen as soon as everyone finished."


    def get_players_for_group(self, waiting_players):
        players = [p for p in waiting_players]
        activeplayers = [p for p in self.session.get_participants() if p.vars.get('active') == 1]
        #activeplayers = self.session.config['num_players']
        if len(players) == len(activeplayers):
            return players

class result(Page):

    def before_next_page(self):
        self.player.getstake()

    def vars_for_template(self):
        return {
            'payoff': self.participant.vars.get('sweepstake') - Constants.showupfee,
            'totalpayoff': self.participant.vars.get('sweepstake'),
        }
    pass




class ResultsWaitPage(WaitPage):
    title_text = " "
    body_text = "Please remain seated and silent. The outcome of the lottery will be displayed on this screen as soon as everyone finished."

    def after_all_players_arrive(self):
        self.group.sweepstakes()

    pass

class sweepstakeresult0(Page):
    def is_displayed(self):
        return self.player.sswin() == 0

class sweepstakeresult1(Page):
    def is_displayed(self):
        return self.player.sswin() == 1

page_sequence = [
    MyWaitPage,
    #result,
    ResultsWaitPage,
    sweepstakeresult0,
    sweepstakeresult1,
]

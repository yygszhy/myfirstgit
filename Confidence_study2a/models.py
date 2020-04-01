from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'confidence_study2a'
    players_per_group = None
    num_rounds = 1
    num_problemsets = 5
    showupfee = 5
    mmatext = "€0|€32"
    mmbtext = "€0|€3"
    mmacolor = "lightblue"
    mmbcolor = "orange"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

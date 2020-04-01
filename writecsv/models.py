from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# shuffles lists
from random import shuffle
# specific csv writing
import csv
# to copy lists
from copy import deepcopy as dcp

author = 'Felix Albrecht'

doc = """
Create randomized question order
"""


class Constants(BaseConstants):
    name_in_url = 'writecsv'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):

    def creating_session(self):

        if self.round_number == 1:
            # if you want to create a new ordering file
            # gets executed if 'create_ques_order' SESSION_CONFIG is True
            if self.session.config['create_ques_order']:
                # create question number 0 to 6 (7 questions)
                ques = [i for i in range(7)]
                # open writable file in folder 'storage' in otree root directory
                with open('storage/questOrder.csv', 'w', newline='') as csvfile:
                    # create a csv write object (tab delimited)
                    storewriter = csv.writer(csvfile, delimiter='\t')
                    # get player objects
                    for p in self.get_players():
                        # make deep copy to avoid resetting values for all players
                        randomOrder = dcp(ques)
                        # randomize question list for each player
                        shuffle(randomOrder)
                        # assign order to player's participants vars
                        p.participant.vars['questOrder'] = randomOrder
                        # make a deep copy from the quest list
                        line = dcp(randomOrder)
                        # add player ID to front of order list
                        line.insert(0, p.id)
                        # write each line from the list above to the csvfile
                        storewriter.writerow(line)
                    # closing is done automatically

                    ''' Now every player has a questions order in their participant
                    vars 'questOrder'. You can use this list item and condition
                    in each number in views.py or a template'''

            else:
                # of create_ques_order is False, open file for reading
                with open('storage/questOrder.csv', 'r') as csvfile:
                    # create reader object
                    storereader = csv.reader(csvfile, delimiter='\t')
                    # read row
                    addrow = []
                    for row in storereader:
                        # create list x list object
                        addrow.append(row)
                    j = 0
                    # add vars to participant
                    for p in self.get_players():
                        # assign to stored questOrder to player
                        p.participant.vars['questOrder'] = addrow[j][1:]
                        j = 1 + j

# Warning one drawback of this approach is that you need to IDENTICAL number of participants


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    basefield = models.CharField()


    # Notes: You need to watch the permissions of the folder 'storage' it has to have 777 (read, write, execution), otherwise the file cannot be written.

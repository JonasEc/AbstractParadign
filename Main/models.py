from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)

from otree_tools.widgets import AdvancedSliderWidget
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Main'
	players_per_group = None
	num_rounds = 20

	NumPeople = 60

	categories = {  'A': [1,10],
					'B': [11,20],
					'C': [21,30],
					'D': [31,40],
					'E': [41,50],
					'F': [51,60]
				}

class Subsession(BaseSubsession):
	def creating_session(self):
		if self.round_number == 1:
			for p in self.get_players():
				p.participant.vars['truth'] = random.randint(1,Constants.NumPeople)


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	truth = models.PositiveIntegerField()
	signal = models.PositiveIntegerField()
	update = models.PositiveIntegerField(min=1,max=Constants.NumPeople, widget=AdvancedSliderWidget(attrs={'step': 1,'tick_interval': 10 ,},show_value=True), initial = 1)

	def genSignal(self):
		r = random.randint(1,Constants.NumPeople)
		while r == self.truth:
			r = random.randint(1,Constants.NumPeople)

		if r > self.participant.vars['truth']:
			return 0
		else:
			return 1


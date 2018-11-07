from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)

# from otree_tools.widgets import AdvancedSliderWidget
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Main'
	players_per_group = None
	
	num_rounds = 30
	PrePeriod = 5
	RemPeriod = num_rounds - PrePeriod

	NumPeople = 60
	NumPeopleLessOne = NumPeople - 1

	HIT = c(1)
	QuadBonus = c(2)
	GradeBonus = c(0.5)
	MaxBonus = c(2.5)

	treatment = [1,0,0]


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
	# update = models.PositiveIntegerField(min=1,max=Constants.NumPeople,widget=AdvancedSliderWidget(attrs={'step': 1,'tick_interval': 10 ,},show_value=True), initial=1)
	# update = models.PositiveIntegerField(min=1,max=Constants.NumPeople, initial=1, widget = widgets.Slider)
	update = models.PositiveIntegerField(min=1,max=Constants.NumPeople)
	finalguess = models.PositiveIntegerField()

	def genSignal(self):
		r = random.randint(1,Constants.NumPeople)
		while r == self.truth:
			r = random.randint(1,Constants.NumPeople)

		if r > self.participant.vars['truth']:
			return 0
		else:
			return 1


	def findPayoffs(self):
		r1 = random.randint(Constants.PrePeriod, Constants.num_rounds)

		payoff  = max(0,Constants.QuadBonus - 1/100*(self.in_round(r1).update  -self.participant.vars['truth'])**2)

		if self.participant.vars['Treatment'][0]:
			pdic = {0: range(1,11), 1: range(11,21), 2: range(21,31), 3: range(31,41),4: range(41,51),5: range(51,61)}
		elif self.participant.vars['Treatment'][1]:
			pdic = {0: range(1,21), 1: range(21,41), 2: range(41,61)}			
		elif self.participant.vars['Treatment'][2]:
			pdic = {0: range(1,31), 1: range(31,61)}

		if self.participant.vars['truth'] in pdic[self.finalguess]:
			payoff += Constants.GradeBonus

		self.payoff = payoff



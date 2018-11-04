from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants




class Update(Page):
	form_model = 'player'
	form_fields = ['update']


	def before_next_page(self):
		self.player.signal = self.player.genSignal()


	def vars_for_template(self):
		if self.round_number == 1:
			self.player.truth = self.player.participant.vars['truth']

		if self.round_number > 1:
			update=  self.player.in_round(self.round_number - 1).update
			signal= self.player.in_round(self.round_number - 1).signal
		else:
			update = 0
			signal = 0

		return {
				# 'cats': Constants.categories,
				'update': update,
				'signal': signal
				}




class Signal(Page):
	def vars_for_template(self):
		return {
				# 'cats': Constants.categories,
				'signal': self.player.signal,
				'update': self.player.update
		}


page_sequence = [
	Update,
	Signal
]

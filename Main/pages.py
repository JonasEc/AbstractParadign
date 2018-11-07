from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
	def is_displayed(self):
		if self.round_number == 1:
			if 'treatment' in self.session.config:
				self.player.participant.vars['treatment']= self.session.config['treatment']
			else:
				self.player.participant.vars['treatment']= Constants.treatment			
			return True
		else:
			return False 

	def vars_for_template(self):
		treatmentMany = self.player.participant.vars['Treatment'][0]
		treatmentMiddle = self.player.participant.vars['Treatment'][1]
		treatmentFew = self.player.participant.vars['Treatment'][2]				

		return {'treatmentMany':treatmentMany, 'treatmentMiddle': treatmentMiddle, 'treatmentFew': treatmentFew }


class Intro2(Page):
	def vars_for_template(self):
		treatmentMany = self.player.participant.vars['Treatment'][0]
		treatmentMiddle = self.player.participant.vars['Treatment'][1]
		treatmentFew = self.player.participant.vars['Treatment'][2]				

		return {'treatmentMany':treatmentMany, 'treatmentMiddle': treatmentMiddle, 'treatmentFew': treatmentFew}







class Update(Page):
	form_model = 'player'
	form_fields = ['update']

	def is_displayed(self):
		return self.round_number >= Constants.PrePeriod


	def vars_for_template(self):
		if self.round_number == 1:
			self.player.truth = self.player.participant.vars['truth']

		if self.round_number > 1:
			update= self.player.in_round(self.round_number - 1).update
			signal= self.player.in_round(self.round_number - 1).signal
		else:
			update = 0
			signal = 0

		if self.round_number == Constants.PrePeriod:
			modeTransition = 1
		else:
			modeTransition = 0

		treatmentMany = self.player.participant.vars['Treatment'][0]
		treatmentMiddle = self.player.participant.vars['Treatment'][1]
		treatmentFew = self.player.participant.vars['Treatment'][2]				

		return {'treatmentMany':treatmentMany, 'treatmentMiddle': treatmentMiddle, 'treatmentFew': treatmentFew ,
				'round': self.round_number
				'update': update,
				'signal': signal,
				'modeTransition': round5 
				}

	def before_next_page(self):
		self.player.signal = self.player.genSignal()


class Signal(Page):
	def vars_for_template(self):
		treatmentMany = self.player.participant.vars['Treatment'][0]
		treatmentMiddle = self.player.participant.vars['Treatment'][1]
		treatmentFew = self.player.participant.vars['Treatment'][2]				

		return {'treatmentMany':treatmentMany, 'treatmentMiddle': treatmentMiddle, 'treatmentFew': treatmentFew ,
				'round': self.round_number
				'signal': self.player.signal,
				'update': self.player.update,
				'pre': self.round_number < Constants.PrePeriod
		}





class Grade(Page):
	form_model = 'player'
	form_fields = ['finalguess']

	def is_displayed(self):
		treatmentMany = self.player.participant.vars['Treatment'][0]
		treatmentMiddle = self.player.participant.vars['Treatment'][1]
		treatmentFew = self.player.participant.vars['Treatment'][2]				

		return {'treatmentMany':treatmentMany, 'treatmentMiddle': treatmentMiddle, 'treatmentFew': treatmentFew}
	
	def finalguess_choices(self):
		if self.player.participant.vars['Treatment'][0]:
			return {[0, "A"], [1, "B"], [2, "C"], [3, "D"], [4, "E"], [5, "F"]}
		elif self.player.participant.vars['Treatment'][1]:
			return {[0, "A"], [1, "B"], [2, "F"]}			
		elif self.player.participant.vars['Treatment'][2]:
			return {[0, "Pass"], [1, "Fail"]}


	def before_next_page(self):
		self.player.payoff = self,player.findPayoffs()



class Payment(Page):
	def is_displayed(self):
		return self.round_number == Constants.num_rounds

	def vars_for_template(self):
		return {'p': self.player.payoff}



page_sequence = [
	Intro,
	Intro2,
	Intro3,
	Intro4,
	Update,
	Signal,
	Payment
]

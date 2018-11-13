from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Captcha(Page):
	form_model = 'player'
	form_fields = ['captcha']

	def vars_for_template(self):
		return {"png": self.player.participant.vars['png'], 'mis': self.player.mistakes, 'maxMis': Constants.maxMistakes}


	def error_message(self, values):		
		if self.player.mistakes >= Constants.maxMistakes:
			return "You have made too many mistakes. Please return this HIT."

		if values['captcha'] != self.player.participant.vars['solution']:
			mistakes = self.player.mistakes  + 1
			self.player.mistakes = mistakes

			text = "This was incorrect. You have " + str(Constants.maxMistakes - mistakes) + " attempts left."

			return text
		

    



page_sequence = [
	Captcha
]

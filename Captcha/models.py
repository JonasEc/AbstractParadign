from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)


author = 'Jonas Mueller Gastell'

doc = """
Home Made Captcha
"""

import random

from PIL import Image, ImageDraw, ImageFont, ImageChops

import os
import io
import base64

import textwrap


try:
	from django.conf import settings
	ARIAL_TTF = os.path.join(settings.FONTS_DIR, "arial.ttf")
except ImportError:
	ARIAL_TTF = "arial.ttf"


author = 'Jonas Mueller-Gastell'

doc = """
This is the main part of the experiment.
"""

ARIAL = settings.FONTS_DIR



class Constants(BaseConstants):
	name_in_url = 'Captcha'
	players_per_group = None
	num_rounds = 1

	maxMistakes = 5

	fontsize = 15
	textwidth = 110


class Subsession(BaseSubsession):
	def creating_session(self):
		pl = self.get_players()
		for p in pl:
			p.participant.vars['png'] = p.picturemaker()


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	captcha = models.PositiveIntegerField(label = '')
	mistakes = models.PositiveIntegerField(initial = 0)

	def picturemaker(self):	
	### Picture good/ bad
		k = [random.randint(1,12) for s in range(4)]
		text = " + ".join(str(s) for s in k) + " =  ???"
		self.participant.vars['solution'] = sum(k)

		#### CREATE THE DIMENSION OF THE PICTURE & the wrapper to be written
		# in console: myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
		font = ImageFont.truetype(ARIAL_TTF, Constants.fontsize)
		wrapper = textwrap.wrap(text, width=Constants.textwidth)
		lines = len(wrapper)
		width = 0
		height = 0
		for subwrap in wrapper:
			temp1, temp2 = font.getsize(subwrap)
			if temp1 > width:
				width = temp1
			if temp2 > height:
				height = temp2
		margin =  15
		offset = 15

		#### MAKE THE PICTURE
		image = Image.new("RGBA", (width + 2*margin, (height+3)*lines + 2*offset), (255,255,255))
		draw = ImageDraw.Draw(image)

		for line in wrapper:
			draw.text((margin, offset), line, font=font, fill = "#000000")
			offset += height + 3

		### SAVE THE PICTURE
		buff = io.BytesIO()
		buff.seek(0)
		image.save(buff, 'png')
		buff.seek(0)

		#### OUTPUT THE PICTURE
		encoded_image= base64.b64encode(buff.getvalue())
		return encoded_image
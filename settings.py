import os
from os import environ


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "_fonts")

	


mturk_hit_settings = {
    'keywords': ['bonus', 'study', 'reseach', 'fun'],
    'title': 'Research Study: Bonus Payment of up to $2.5',
    'description': 'In this study, you will receive information and then make guesses. Depending on the accuracy of these guesses you can earn up to $2.5 bonus',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 75,
    'expiration_hours': 6, 
    'qualification_requirements': [
        {
            'QualificationTypeId': "00000000000000000071",
    		'Comparator': "EqualTo",
    		'LocaleValues': [{'Country': "US"}]
        },
        {
            'QualificationTypeId': "00000000000000000040", ### number of HITs
            'Comparator': "GreaterThan",
         	'IntegerValues':[1000]
        },
        {
            'QualificationTypeId': "000000000000000000L0", ### percentage accept of HITs
            'Comparator': "GreaterThan",
         	'IntegerValues':[97]
        }
    ],
}



# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
	'real_world_currency_per_point': 1.00,
	'participation_fee': 0.50,
	'doc': "",
	'mturk_hit_settings': mturk_hit_settings
}

SESSION_CONFIGS = [


SESSION_CONFIGS = [
	{
		'name': 'Abstract',
		'display_name': "AbstractTest",
		'num_demo_participants': 3,
		'app_sequence': ['Captcha','Main'],
		'treatmentMany': 1,
		'treatmentMiddle': 0,
		'treatmentFew':0,		
	},
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'jonasmgoTree'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'abstractcategoricalthinking'


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 'b%edt=6o4@qqjxgdp_0f+n*n(v1z*6)3kc=npnba0zvjej0(_k'


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWSAccessKeyId_Jonas')
AWS_SECRET_ACCESS_KEY = environ.get('AWSSecretKey_Jonas')




# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


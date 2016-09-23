class GameStats(object):
	def __init__(self, settings):
		self.settings = settings
		#add mans_left to settings
		self.game_active = False
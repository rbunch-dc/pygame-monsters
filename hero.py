import pygame #duh

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen

		# Load the hero image, get it's rect
		self.image = pygame.image.load('images/hero.png')
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object so we can get some dimension and location
		self.screen_rect = screen.get_rect() #assign a var so the hero class knows how big and where the screen s

		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen
		self.rect.bottom = self.screen_rect.bottom #this will put our hero "bottom" at the bottom of the screen
		# not self.rect.centery beause we want the bottom on the bottom, not the center on the bottom

		self.moving_right = False #Set up movement booleans
		self.moving_left = False

	# Add update to the hero class to keep all the hero updates in the hero class
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 10 #Move the hero to the right!
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= 10 #Move the hero to the left!

	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect) #Draw the Surface... (the image, the where)

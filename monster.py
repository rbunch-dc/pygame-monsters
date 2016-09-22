import pygame
import math
from pygame.sprite import Sprite

class Monster(Sprite):
	def __init__(self, screen):
		super(Monster,self).__init__()
		self.image = pygame.image.load('images/monster1.png')
		self.rect = self.image.get_rect() 
		self.screen_rect = screen.get_rect()

		self.screen = screen
		self.rect.centery = self.screen_rect.centery
		self.rect.right = self.screen_rect.right

	def update(self, hero, speed = 5):
		dx = self.rect.x - hero.rect.x
		dy = self.rect.y - hero.rect.y
		dist = math.hypot(dx, dy)
		dx = dx / dist
		dy = dy / dist

		self.rect.x -= dx * speed
		self.rect.y -= dy * speed

	def draw_me(self):
		self.screen.blit(self.image, self.rect)

	def __exit__(self, error):
		self.remove(self)
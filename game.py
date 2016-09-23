import pygame #DUH
from hero import Hero #bring in the hero class with all it's methods and glory
from settings import Settings
import game_functions as gf
from pygame.sprite import Group, groupcollide
from monster import Monster
from start_button import Play_button

# Set up the main core function
def run_game():
	pygame.init() #initialize all the pygame modules
	game_settings = Settings() #create an instance of settings class
	screen = pygame.display.set_mode(game_settings.screen_size) #Set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar

	# Create a playbutton object and assign to a var
	play_button = Play_button(screen,'Play')

	hero = Hero(screen) #set a variable equal to the class and pass it the screen
	bullets = Group() #set the bullets to group
	enemies = Group()
	enemies.add(Monster(screen))

	tick = 0 #init counter at 0

	while 1: #run this loop forever...
		gf.check_events(hero, bullets, game_settings, screen) #call gf (aliased from game_functions module) and get the check_events method
		hero.update() #update the hero flags
		enemies.update(hero, game_settings.enemy_speed)
		tick += 1
		if tick % 150 == 0: 
			enemies.add(Monster(screen))
		bullets.update() #call the update method in the while loop
		theDict = groupcollide(enemies, bullets, True, True)
		# print theDict
		gf.update_screen(game_settings, screen, hero, enemies, bullets, play_button) #call the update_screen method which handles updating the screen
		for bullet in bullets: #get rid of bullets that are off the screen
			if bullet.rect.bottom <= 0: #bullet bottom is at the top of the screen
				bullets.remove(bullet) #call remove() against the group
		# print len(bullets) #print the list bullets for fun

run_game() #Start the game!
import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	drawable = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (drawable, updatable)
	Shot.containers = (shots, drawable, updatable)
	Asteroid.containers = (asteroids, drawable, updatable)
	AsteroidField.containers = updatable
	player = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
	asteroid_field = AsteroidField()
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		for thing in updatable:
			thing.update(dt)
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides(shot):
					shot.kill()
					asteroid.split()
			if asteroid.collides(player):
				print("Game over!")
				sys.exit()

		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

# http://www.nerdparadise.com/programming/pygame/part2

import pygame
import os

_image_library = {}

def get_image(path):
	global _image_library
	image = _image_library.get(path)
	if image == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		image = pygame.image.load(canonicalized_path)
		_image_library[path] = image
	return image

pygame.init()
screen = pygame.display.set_mode((400, 300))


image1 = pygame.image.load('ball.png')

done = False
clock = pygame.time.Clock()
fps = 60
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255))

	screen.blit(get_image('ball.png'), (20, 20))
	screen.blit(image1, (40, 40))

	pygame.display.flip()
	clock.tick(fps)

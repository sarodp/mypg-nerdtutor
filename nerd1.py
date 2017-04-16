# http://www.nerdparadise.com/programming/pygame/part1

import pygame

#1--pscreen
scrwidth = 400
scrheight = 300
pygame.init()
screen = pygame.display.set_mode((scrwidth,scrheight))

#1a--pvar's
done = False
idxcolor = 0

xl,yl = 60,60
xmin,xmax =0-xl*.8,scrwidth-xl*.2
ymin,ymax =0-yl*.8,scrheight-yl*.2
x,y = xl/2,yl/2

color =[]
color.append((255,0,0))		#color[0]
color.append((255,255,0))  	#color[1]
color.append((255,0,255))  	#color[3]
color.append((255,111,0))  	#color[4]
color.append((111,255,0))  	#color[5]
color.append((255,255,111))	#color[6]

#2--pwhile
pygame.mouse.set_visible (False)

clock = pygame.time.Clock()
fps = 10
clock.tick(fps)  #cpu time = 30% up

while not done:
		#--pevents
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
						done = True
				if event.type == pygame.KEYDOWN: 
					if event.key == pygame.K_ESCAPE:
						done = True
					if event.key == pygame.K_SPACE:
						idxcolor +=1
						if idxcolor > (len(color)-1): idxcolor = 0 
		#--keypress 
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]: y-=1 
		if pressed[pygame.K_DOWN]: y +=1 
		if pressed[pygame.K_LEFT]: x -=1 
		if pressed[pygame.K_RIGHT]: x +=1 
		
		#--x,y min/max
		if x<xmin: x=xmin 
		if x>xmax: x=xmax
		if y<ymin: y=ymin
		if y>ymax: y= ymax

		#--screen.fill...draw.Graphics...blit.FontText
		screen.fill((0, 0, 0))
		#pygame.draw.rect(screen, color[idxcolor], pygame.Rect(x, y, xl, yl))
		pygame.draw.rect(screen, color[idxcolor], (x, y, xl, yl))

		#--pflip
		pygame.display.flip()
		#clock.tick(fps)  # less cpu time = 10% or less

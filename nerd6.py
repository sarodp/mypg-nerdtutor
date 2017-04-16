# http://www.nerdparadise.com/programming/pygame/part6
#
# mouse input

import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	clock = pygame.time.Clock()

	radius = 15
	x = 0
	y = 0
	cmodes = ["red","green","blue"]
	points = []

	while True:
		pressed = pygame.key.get_pressed()

		alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
		ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

		for event in pygame.event.get():
			# determin if X was clicked, or Ctrl+W or Alt+F4 was used 
			if event.type == pygame.QUIT:
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w and ctrl_held:
					return
				if event.key == pygame.K_F4 and alt_held:
					return
				if event.key == pygame.K_ESCAPE:
					return

			#[1=Lclick 3=Rclick  2=Mclick  4=ScrUp 5=ScrDN]
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4: #ScrUP...grows radius 
					radius = min(200, radius + 1)
				if event.button == 5: #ScrDN..shrinks radius 
					radius = max(1, radius - 1)
				if event.button == 3: #Lclick...change cmodes[0] 
					cm0 = cmodes[0]
					cmodes = cmodes[1:]
					cmodes.append(cm0)

			# if mouse moved and left button down, add point to list 
			if event.type == pygame.MOUSEMOTION:
				if event.buttons[0] ==1:
					position = event.pos
					points = points + [position]
					points = points[-256:]

		screen.fill((0, 0, 0))

		# draw all points 
		i = 0
		while i < len(points) - 1:
			drawLineBetween(screen, i, points[i], points[i + 1], radius, cmodes[0])
			i += 1

		pygame.display.flip()
		clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in xrange(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = aprogress * start[0] + progress * end[0]
        y = aprogress * start[1] + progress * end[1]
        pygame.draw.circle(screen, color, (int(x), int(y)), width)

main()



'''
#================================================================
# While debugging and experimenting, 
# you can print an event object 
# for a quick display of its type and members. 
# 
# Events that come from the system 
# will have a guaranteed set of member items based on the type. 
#
# Here is a list of the event attributes 
# defined with each event type
#================================================================

# ---------------------   ---------------------------
# event.type              event.<attributes>
# ---------------------   ---------------------------
# pygame.QUIT             none
# pygame.ACTIVEEVENT      event.gain, event.state

# pygame.KEYDOWN          event.unicode, event.key, event.mod
# pygame.KEYUP            event.key, event.mod

# pygame.MOUSEMOTION      event.pos, event.rel, event.buttons
# pygame.MOUSEBUTTONUP    event.pos, event.button
# pygame.MOUSEBUTTONDOWN  event.pos, event.button

# pygame.JOYAXISMOTION    event.joy, event.axis, event.value
# pygame.JOYBALLMOTION    event.joy, event.ball, event.rel
# pygame.JOYHATMOTION     event.joy, event.hat, event.value
# pygame.JOYBUTTONUP      event.joy, event.button
# pygame.JOYBUTTONDOWN    event.joy, event.button

# pygame.VIDEORESIZE      event.size, event.w, event.h
# pygame.VIDEOEXPOSE      none

# pygame.USEREVENT        event.code
#
#================================================================
'''

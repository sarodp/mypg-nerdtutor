# http://www.nerdparadise.com/programming/pygame/part1
import pygame

#--print list of keycodes
print ("event.type: pygame.KEYUP/KEYDOWN")
print ("event.key : pygame.K_%%%%%")
print ("----------------------------------------------")
kcodes = filter(lambda x:'K_' in x, dir(pygame))
for ki in kcodes: print ('event.key == pygame.%s' % ki)

#--init screen,mouse,clock
pygame.init()
screen = pygame.display.set_mode((400, 300))

pygame.mouse.set_visible (True)

clock = pygame.time.Clock()
#clock.tick(10)

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_ESCAPE:
				done = True
		
	pygame.display.flip()
	clock.tick(10)


'''
# As you can imagine, 
# there is also a corresponding pygame.KEYUP event type 
# and a pygame.K_%%%%% for almost every key on your keyboard. 
# To see this list, go to a python terminal and use dir(pygame). 

import pygame
filter(lambda x:'K_' in x, dir(pygame))
[
'K_0', 'K_1', 'K_2', 'K_3', 'K_4', 'K_5', 'K_6', 'K_7', 'K_8', 'K_9', 

'K_AMPERSAND', 'K_ASTERISK', 'K_AT', 

'K_BACKQUOTE', 'K_BACKSLASH', 'K_BACKSPACE', 'K_BREAK', 

'K_CAPSLOCK', 'K_CARET', 'K_CLEAR', 'K_COLON', 'K_COMMA', 

'K_DELETE', 'K_DOLLAR', 'K_DOWN', 

'K_END', 'K_EQUALS', 'K_ESCAPE', 'K_EURO', 'K_EXCLAIM', 

'K_F1','K_F10', 'K_F11', 'K_F12', 'K_F13', 'K_F14', 'K_F15', 
'K_F2', 'K_F3', 'K_F4', 'K_F5', 'K_F6', 'K_F7', 'K_F8', 'K_F9', 

'K_FIRST', 
'K_GREATER', 
'K_HASH', 'K_HELP', 'K_HOME', 
'K_INSERT', 

'K_KP0', 'K_KP1', 'K_KP2', 'K_KP3', 'K_KP4', 
'K_KP5', 'K_KP6', 'K_KP7', 'K_KP8', 'K_KP9', 
'K_KP_DIVIDE', 'K_KP_ENTER', 'K_KP_EQUALS', 'K_KP_MINUS', 'K_KP_MULTIPLY', 
'K_KP_PERIOD', 'K_KP_PLUS', 

'K_LALT', 'K_LAST', 'K_LCTRL', 
'K_LEFT', 'K_LEFTBRACKET', 'K_LEFTPAREN', 
'K_LESS', 'K_LMETA', 'K_LSHIFT', 'K_LSUPER', 

'K_MENU', 'K_MINUS', 'K_MODE', 
'K_NUMLOCK', 

'K_PAGEDOWN', 'K_PAGEUP', 'K_PAUSE', 'K_PERIOD', 'K_PLUS', 'K_POWER', 'K_PRINT', 

'K_QUESTION', 'K_QUOTE', 'K_QUOTEDBL', 

'K_RALT', 'K_RCTRL', 'K_RETURN', 'K_RIGHT', 'K_RIGHTBRACKET',
'K_RIGHTPAREN', 'K_RMETA', 'K_RSHIFT', 'K_RSUPER', 

'K_SCROLLOCK', 'K_SEMICOLON', 'K_SLASH', 'K_SPACE', 'K_SYSREQ', 

'K_TAB', 

'K_UNDERSCORE', 'K_UNKNOWN', 'K_UP', 

'K_a', 'K_b', 'K_c', 'K_d', 'K_e', 'K_f', 'K_g', 'K_h', 'K_i', 'K_j', 
'K_k', 'K_l', 'K_m', 'K_n', 'K_o', 'K_p', 'K_q', 'K_r', 'K_s', 'K_t', 
'K_u', 'K_v', 'K_w', 'K_x', 'K_y', 'K_z'
]
>>>
'''

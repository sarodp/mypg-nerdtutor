# http://www.nerdparadise.com/programming/pygame/part3
#
# -- pygame.mixer.music 
# -- pygame.mixer.Sound

import pygame, glob
#init vars
xsound = glob.glob("./media/*.ogg")
xsound.sort()

#xmusic=glob.glob("./media/*.*['mid','mp3','wav']")
xmusic=glob.glob("./media/*.mid")
xmusic.sort()

#--init screen,mouse,clock
pygame.init()
screen = pygame.display.set_mode((400, 300))

pygame.mouse.set_visible (True)

pygame.mixer.music.load(xmusic[0])
pygame.mixer.music.play(0)

fps,si,mi = 60,0,0
clock = pygame.time.Clock()
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_ESCAPE:
				done = True
			if event.key == pygame.K_s:
				psnd1 = pygame.mixer.Sound(xsound[si])
				psnd1.play()
				si +=1 
				if si==len(xsound): si=0
				
			if event.key == pygame.K_m:
				pygame.mixer.music.load(xmusic[mi])
				pygame.mixer.music.play(0)
				mi +=1 
				if mi==len(xmusic): mi=0
			if event.key == pygame.K_n:
				pygame.mixer.music.stop()

	pygame.display.flip()
	clock.tick(fps)


'''
#====================================================
#--.music
#.play(0) ...play a song once
pygame.mixer.music.load(xmp3)
pygame.mixer.music.play(0)

pygame.mixer.music.load(xmp3)
pygame.mixer.music.play()

#.play(-1) ...play a song forever
pygame.mixer.music.load(xmp3)
pygame.mixer.music.play(-1)


#.queue() ...play a song immediately next
pygame.mixer.music.queue(xmp3)

#.stop() ...stop a song
pygame.mixer.music.stop()


#.set_endevent ...callback when a song ends
SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()

#====================================================
#--.Sound
sound1 = pygame.mixer.Sound(xsnd)
sound1.play()


'''

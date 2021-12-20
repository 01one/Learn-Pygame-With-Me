import glob
import pygame,sys
from pygame.locals import QUIT
from pygame import mixer
mixer.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((400,400))
lightgreen=(144, 238,144)

play=[pygame.image.load("background1.png"),pygame.image.load("background2.png")]


n=0
p=0

m=0
file1=glob.glob("music/*.mp3")

mp=mixer.music.load(file1[m])
############################################
play_pause=pygame.Rect(165,272,35,45)
previous=pygame.Rect(243,276,27,35)
forward=pygame.Rect(94,276,26,30)



###########################################
print(file1)
l=len(file1)





	
	



game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		mouse_position=pygame.mouse.get_pos()
		if event.type==pygame.MOUSEBUTTONDOWN:
			if play_pause.collidepoint(mouse_position):
				
				if event.button==1:
					if play_pause.collidepoint(mouse_position):
						if p>2:
							p=1
						if p==0 :
							mixer.music.play()
							n=1
						if p==1:
							mixer.music.pause()
							n=0
						else:
							mixer.music.unpause()
							n=1
						p+=1
					"""
					if previous.collidepoint(mouse_position):
						m+=1
						if m<l-1:
							m=0
						mixer.music.stop()
						mp=mixer.music.load(file1[m])
						mixer.music.play()
					if forward.collidepoint(mouse_position):
						m+=1
						if m>l-1:
							m=0
						mixer.music.stop()
						mp=mixer.music.load(file1[m])
						mixer.music.play()
						"""
		current_time=mixer.music.get_pos()
	screen.blit(play[n],(0,0))
	pygame.display.update()

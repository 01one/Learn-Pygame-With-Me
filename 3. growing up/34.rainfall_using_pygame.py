import pygame,sys
from pygame.locals import*
from random import randint

pygame.init()
clock=pygame.time.Clock()
user_display=pygame.display.Info()
width,height=user_display.current_w,user_display.current_h
screen=pygame.display.set_mode((width,height-50))


class Rainfall():
	def __init__(self):
		self.x=randint(1,width)
		self.y=randint(-height,-10)
	
	def show(self):
		pygame.draw.line(screen,((255,255,255)),(self.x,self.y),(self.x,self.y+2),2)
		
	def update(self):
		if self.y>height:
			self.y=randint(-10,0)

		else:
			self.y=10+self.y*1.03
    
Rain=[Rainfall() for i in range(2000)]
game_running=True
while game_running:
	clock.tick(100)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill((62,70,216))
	for i in range(len(Rain)):
		Rain[i].show()
		Rain[i].update()
	pygame.display.update()

#  Copyright 2022 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
from math import sqrt
from itertools import permutations
import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption("Travelling Salesman Problem")
screen=pygame.display.set_mode((800,600))
background=(255,255,255)
purple=(187,51,255)



#xy={"a":[80,120],"g":[160,120],"b":[200,160],"e":[200,224],"j":[160,240],"i":[56,240],"k":[120,200],"h":[120,160],"f":[72,160],"d":[96,176],"c":[144,200]} #"l":[120,152],"m":[136,244],"n":[216,00],"0":[100,248],"p":[200,76]}

xy={"a":[80,120],"b":[170,220],"c":[180,160],"d":[150,240],"e":[60,140],"f":[56,230],"g":[130,210],"h":[120,170],"i":[72,190]}
#completed path
path="bcdefghi"
#path="bcdefghijklmnop"
ways=permutations(path)
ways=list(ways)
ways = ["a"+''.join(item)+"a" for item in ways]


#different roads
roads="abcdefghia"
#roads="abcdefghijklmnopa"
road=permutations(roads,2)
road=list(road)
road= [''.join(item) for item in road]
#print(road)


def process(a,b):
	c=(a+b)
	return c
def distance(c):
	z=sqrt(abs(c[0]**2-c[2]**2))+sqrt(abs(c[1]**2-c[3]**2))
	return z

road_d={}
for i in range(len(road)-1):
	c=road[i]
	c1=xy[c[0]]
	c2=xy[c[1]]
	p=process(c1,c2)
	k=distance(p)
	road_d[c]=k

print(road_d)
cc=[]
dd=[]
for i in range(len(ways)):
	x=ways[i]
	l=[]
	m=[]
	d=0 #total distance
	for j in range(len(x)-1):
		a=x[j]
		b=x[j+1]
		c=a+b
		d+=road_d[c]
		l.append(c)
		m.append(a)

	dd.append(d)
	pp=[xy[item] for item in m]
	cc.append(pp)




ln=len(cc)-1
print(ln+1)
new=0
nn=[]

def show_distance(text):
    distance_font=pygame.font.Font(pygame.font.get_default_font(), 20)
    distance_text=distance_font.render(text,True,purple)
    screen.blit(distance_text,(50,50))
def show_shortage_distance(text):
    s_font=pygame.font.Font(pygame.font.get_default_font(), 20)
    s_text=s_font.render(text,True,purple)
    screen.blit(s_text,(350,50))

lowest=0

surface=pygame.Surface((300,250))

def draw_points(screen):
	for i in range(len(roads)-1):
		a=roads[i]
		b=xy[a]
		pygame.draw.circle(screen,(255,100,255),b,5,2)


game_running=True
while game_running:
	#clock.tick(30)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(background)
	draw_points(screen)
	pygame.draw.lines(screen,((255,100,255)),True,cc[new],1)
	if new==0:
		lowest=dd[0]
	if lowest>=dd[new]:
		lowest=dd[new]
		nn=cc[new]
		
	if new<ln:
		new+=1
	show_distance(str(dd[new]))
	surface.fill((240,240,240))
	pygame.draw.lines(surface,((255,100,255)),True,nn,1)
	draw_points(surface)
	screen.blit(surface,(350,0))
	show_shortage_distance(str(lowest))
	pygame.display.update()

	

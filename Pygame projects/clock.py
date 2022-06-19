import  pygame
from math import sin,cos,radians
import time



pygame.init()
surface=pygame.display.set_mode((600,600))

radius=250
min_len=200
centerX=300
centerY=300
theta=-60

points=12
endX=[]
endY=[]
num_img=[]
font = pygame.font.Font('freesansbold.ttf', 32)

for i in range(points):
    endX.append(centerX+min_len*cos(radians(theta)))
    endY.append(centerY+min_len*sin(radians(theta)))
    theta+=30

for i in range(1,points+1):
    num_img.append(font.render(str(i),True,(255,255,255)))

running=1
i=0
while running:
    if i==12:
        i=0
    surface.fill((0,0,0))
    pygame.draw.circle(surface, (255, 255, 255), (300, 300), radius, 4)
    for j in range(points):
        surface.blit(num_img[j],(endX[j]-10,endY[j]-10))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=0

    pygame.draw.line(surface,(255,255,255),(300,300),(endX[i],endY[i]),4)
    i+=1
    time.sleep(1)
    pygame.display.update()

import  pygame
from math import sin,cos,pi
from time import localtime,sleep

class Clock:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.current_time=localtime()
        self.center=(300,300)
        self.num_img=list()
        self.num_pos=list()
        self.radius=250
        self.min_len=200
        font = pygame.font.Font('freesansbold.ttf', 32)
        for i in range(1, 13):
            self.num_pos.append((self.center[0]+self.min_len*cos(i*2*pi/12 - pi/2),self.center[1]+self.min_len*sin(i*2*pi/12 -pi/2)))
            self.num_img.append(font.render(str(i), True, (255, 255, 255)))

    def hour_hand(self):
        hour_len=100
        hour=self.current_time.tm_hour
        hour_angle=hour*2*pi/12 + self.current_time.tm_min*pi/360 -pi/2
        hour_end=(self.center[0]+hour_len*cos(hour_angle),self.center[1]+hour_len*sin(hour_angle))
        pygame.draw.line(self.screen, (255, 255, 255),self.center,hour_end, 4)

    def minute_hand(self):
        min=self.current_time.tm_min
        min_angle=min*2*pi/60 - pi/2
        min_end=(self.center[0]+self.min_len*cos(min_angle),self.center[1]+self.min_len*sin(min_angle))
        pygame.draw.line(self.screen, (255, 255, 255), self.center, min_end, 4)


    def numbers(self):
        for i in range(12):
            self.screen.blit(self.num_img[i],(self.num_pos[i][0]-10,self.num_pos[i][1]-10))

    def main_loop(self):
        running=True
        i=0
        while running:
            self.screen.fill((0, 0, 0))
            i=i%12
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.hour_hand()
            self.minute_hand()
            self.numbers()

            pygame.draw.circle(self.screen, (255, 255, 255), (300, 300), self.radius, 4)
            pygame.draw.line(self.screen, (255, 255, 255), (300, 300), self.num_pos[i], 4)
            sleep(1)
            self.current_time=localtime()
            i=i+1
            pygame.display.update()



if __name__ =="__main__":
    clock_object=Clock()
    clock_object.main_loop()



import pygame

class Player:
    def __init__(self, screen):
        width, height = screen.get_size()
        self.pos = [width/2, height/2]
        self.to = [0, 0]
        self.angle = 0
        self.life = 10          #미션 4 : 비행기가 총알과 여러번 충돌해야 게임이 종료되도록 한다.
        self.image = pygame.image.load("dodge_src/player.png")
        self.image = pygame.transform.scale(self.image, (32, 32))


    def draw(self, screen):
        calib_pos = (
            self.pos[0] - self.image.get_size()[0]/2,
            self.pos[1] - self.image.get_size()[1]/2
        )

        if self.to == [-1, -1]: self.angle = 45
        elif self.to == [-1, 0]: self.angle = 90
        elif self.to == [-1, 1]: self.angle = 135
        elif self.to == [0, 1]: self.angle =  180
        elif self.to == [1, 1]: self.angle = -145
        elif self.to == [1, 0]: self.angle = -90
        elif self.to == [1, -1]: self.angle = 5
        elif self.to == [0, -1]: self.angle = 0

        rotated = pygame.transform.rotate(self.image, self.angle)
        calib_pos = (
            self.pos[0] - rotated.get_size()[0]/2, 
            self.pos[1] - rotated.get_size()[1]/2
            )
        screen.blit(rotated, calib_pos)
    
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y
    
    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * self.to[0] * 0.5)
        self.pos[1] = (self.pos[1] + dt * self.to[1] * 0.5)

        #화면 밖으로 나가지 않게, 16은 기체의 절반크기
        if self.pos[0] < 0:
            self.pos[0] = 16
        if self.pos[0] > width:
            self.pos[0] = width-1
        if self.pos[1] < 0:
            self.pos[1] = 16
        if self.pos[1] > height:
            self.pos[1] = height-16
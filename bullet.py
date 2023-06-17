import pygame

class Bullet1:
    score = 1
    name = "Bullet1"
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 3
        self.color = (255, 255, 0) #노란색

    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0] * 0.5) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1] * 0.5) % height
        #pygame의 원 그리기 툴
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

class Bullet2:
    score = 2
    name = "Bullet2"
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 4
        self.color = (0, 255, 0) #초록색

    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0] * 0.5) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1] * 0.5) % height
        #pygame의 원 그리기 툴
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

class Bullet3:
    score = 3
    name = "Bullet3"
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 5
        self.color = (80,188,223) #히늘색

    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0] * 0.5) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1] * 0.5) % height
        #pygame의 원 그리기 툴
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
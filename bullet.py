import pygame

class Bullet1:
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 4
        self.color = (255, 255, 0)
        self.score = 2

    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0] * 0.5) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1] * 0.5) % height
        #pygame의 원 그리기 툴
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

class Bullet2:
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 6
        self.color = (255, 255, 0)
        self.score = 3

    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0] * 0.5) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1] * 0.5) % height
        #pygame의 원 그리기 툴
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

class Bullet3:
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 3
        self.color = (255, 255, 0)
        self.score = 1

    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0] * 0.5) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1] * 0.5) % height
        #pygame의 원 그리기 툴
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
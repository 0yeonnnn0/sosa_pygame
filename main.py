import pygame
from player import Player
from bullet import Bullet
import random as rnd
import math
import time

def collision(obj1, obj2):
    if math.sqrt((obj1.pos[0] - obj2.pos[0]) ** 2 + obj1.pos[1] - obj2.pos[1] ** 2) < 20:
        return True
    return False

pygame.init()
WIDTH, HEIGHT = 1000, 800

pygame.display.set_caption("총알 피하기")

clock = pygame.time.Clock()
FPS = 60

player = Player(WIDTH/2, HEIGHT/2)

#총알 생성
bullets = []
for i in range(10):
    bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))

#그림 불러오기
image = pygame.image.load("총알피하기/리소스/player.png")
#그림 크기조절
image = pygame.transform.scale(image, (128, 128))


screen = pygame.display.set_mode((WIDTH, HEIGHT))

#game Loop
running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #X눌렀을때 게임닫기
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("왼쪽 방향키 누름")
                player.goto(-1, 0)
            elif event.key == pygame.K_RIGHT:
                print("오른쪽 방향키 누름")
                player.goto(1, 0)
            elif event.key == pygame.K_UP:
                print("윗쪽 방향키 누름")
            elif event.key == pygame.K_DOWN:
                print("아래쪽 방향키 누름")
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("왼쪽 방향키 뗌")
                player.goto(1, 0) 
            elif event.key == pygame.K_RIGHT:
                print("오른쪽 방향키 뗌")
                player.goto(-1, 0)
            elif event.key == pygame.K_UP:
                print("윗쪽 방향키 뗌")
            elif event.key == pygame.K_DOWN:
                print("아래쪽 방향키 뗌")
    for b in bullets:
        b.update_and_draw(dt, screen)

    #화면에 검은색 채우기
    screen.fill((0,0,0))

    player.update(dt, screen)
    player.draw(screen)

    pygame.display.update()         #이걸 작성해야 화면이 바뀜!

    for b in bullets:
        if collision(player, b):
            time.sleep(2)
            running = False

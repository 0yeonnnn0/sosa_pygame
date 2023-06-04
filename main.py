import pygame
from player import Player
from bullet import Bullet
import random as rnd
import time

def collision(a, b):
    dist = ((a.pos[0] - b.pos[0]) ** 2 + (a.pos[1] - b.pos[1]) **2) ** 0.5
    if dist < 10:
        return True
    else:
        return False

def draw_text(txt, size, pos, color):
    font = pygame.font.Font("freesansbold.ttf", size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)

def draw_img(img, width, height):
    screen.blit(img, (width, height))

bg_image = pygame.image.load("dodge_src/bg.jpg")
bg_image = pygame.transform.scale(bg_image, (1000, 800))
bg_pos = 0

pygame.init()
WIDTH, HEIGHT = 500, 400

pygame.display.set_caption("dodge2023")

#background music, -1 : 무한반복
#효과음 목록
bgm = pygame.mixer.Sound("dodge_src/bgm.wav")
collisionBgm = pygame.mixer.Sound("dodge_src/collision2.wav")
#bgm.play(-1)

clock = pygame.time.Clock()
FPS = 60

#총알 생성 
bullets = []
for i in range(5):
    bullets.append(Bullet(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
    
time_for_adding_bullets = 0
#그림 불러오기
image = pygame.image.load("dodge_src/player.png")
explosionImg = pygame.image.load("dodge_src/explosion.png")

#그림 크기조절
image = pygame.transform.scale(image, (128, 128))
explosionImg = pygame.transform.scale(explosionImg, (64, 64))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player(screen)

time_for_adding_bullets = 0

start_time = time.time()

gameover = False
score = 0
#game Loop
running = True
while running:
    dt = clock.tick(FPS)

    time_for_adding_bullets += dt
    if time_for_adding_bullets >= 1000:
        bullets.append(Bullet(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
        time_for_adding_bullets -= 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #X눌렀을때 게임닫기
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, -1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, 1)
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1, 0) 
            elif event.key == pygame.K_RIGHT:
                player.goto(-1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, -1)

    bg_pos -= 0.01 * dt                 #1초에 0.01씩 오른쪽으로 움직임 : 이부분 고치면 미션3 해결
    screen.blit(bg_image, (bg_pos, 0))

    player.update(dt, screen)
    player.draw(screen)

    for b in bullets:
        b.update_and_draw(dt, screen)

    for b in bullets:
        if collision(player, b):
            #충돌 시 배경음악 꺼짐, 충돌 BGM 켜짐
            bgm.stop()
            collisionBgm.play()     #미션 1
            #충돌 시 이미지 불러오기
            draw_img(explosionImg, player.pos[0]-32, player.pos[1]-32)  #미션 2
            pygame.display.update()                                     #화면 갱신

            #2초 기다리고 게임 종료
            time.sleep(2)
            running = False
            


    draw_text(f"Time: {time.time() - start_time:.2f}, Bullets: {len(bullets)}", 16, (10, 10), (255, 255, 255))

    pygame.display.update()         #이걸 작성해야 화면이 바뀜!


    
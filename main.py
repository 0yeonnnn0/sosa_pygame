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

bg_image = pygame.image.load("pygame_dodge/dodge_src/bg.jpg")
bg_pos = 0

#background music, -1 : 무한반복
#pygame.mixer.music.load("pygame_dodge/dodge_src/bgm.wav")
#pygame.mixer.music.play(-1)

pygame.init()
WIDTH, HEIGHT = 500, 400

pygame.display.set_caption("총알 피하기")

clock = pygame.time.Clock()
FPS = 60

#총알 생성 
bullets = []
for i in range(5):
    bullets.append(Bullet(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
    
time_for_adding_bullets = 0
#그림 불러오기
image = pygame.image.load("pygame_dodge/dodge_src/player.png")
#그림 크기조절
image = pygame.transform.scale(image, (128, 128))


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

    bg_pos -= 0.01 * dt
    screen.blit(bg_image, (bg_pos, 0))

    player.update(dt, screen)
    player.draw(screen)

    for b in bullets:
        b.update_and_draw(dt, screen)

    for b in bullets:
        if collision(player, b):
            time.sleep(2)
            running = False

    draw_text(f"Time: {time.time() - start_time:.2f}, Bullets: {len(bullets)}", 16, (10, 10), (255, 255, 255))

    pygame.display.update()         #이걸 작성해야 화면이 바뀜!


    
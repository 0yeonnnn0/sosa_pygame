import pygame
from player import Player
from bullet import Bullet1, Bullet2, Bullet3
import random as rnd
import time

#color
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

#충돌 감지 함수
def collision(a, b):
    dist = ((a.pos[0] - b.pos[0]) ** 2 + (a.pos[1] - b.pos[1]) **2) ** 0.5
    if dist < 10:
        return True
    else:
        return False
#텍스트 출력
def draw_text(txt, size, pos, color):
    font = pygame.font.Font("freesansbold.ttf", size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)
#이미지 출력
def draw_img(img, x, y):
    screen.blit(img, (x, y))

#플레이어 체력, 미션 6 함수
def draw_player_health(scr,x,y,life):
    if life<0:
        life=0
    BAR_LENGTH=100
    BAR_HEIGHT=20
    fill=life*BAR_LENGTH
    outline_rect=pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT)
    if life > 0.6:
        col=GREEN
    elif life>0.3:
        col=YELLOW
    else:
        col=RED
    pygame.draw.rect(scr,col,fill_rect)
    pygame.draw.rect(scr,WHITE,outline_rect,2)

def mujeok(time):
    if collision:
        nothing
    else:
        sd


#게임 기본정보
pygame.init()
WIDTH, HEIGHT = 500, 400
pygame.display.set_caption("dodge2023")

#효과음 목록
bgm = pygame.mixer.Sound("pygame_dodge/dodge_src/bgm.wav")
collisionBgm = pygame.mixer.Sound("pygame_dodge/dodge_src/collision2.wav")
#bgm.play(-1)

#시간
clock = pygame.time.Clock()
FPS = 60

#총알 생성 
bullets = []
for i in range(2):
    bullets.append(Bullet1(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
    bullets.append(Bullet2(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
    bullets.append(Bullet3(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
    
time_for_adding_bullets = 0
#그림 불러오기
bg_image = pygame.image.load("pygame_dodge/dodge_src/bg.jpg")
image = pygame.image.load("pygame_dodge/dodge_src/player.png")
explosionImg = pygame.image.load("pygame_dodge/dodge_src/explosion.png")

#그림 크기조절
image = pygame.transform.scale(image, (128, 128))
explosionImg = pygame.transform.scale(explosionImg, (64, 64))
bg_image = pygame.transform.scale(bg_image, (1000, 800))

#배경 위치
bg_x = 0
bg_y = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player(screen)

start_time = time.time()

gameover = False
score = 0
#game Loop
running = True
while running:
    dt = clock.tick(FPS)

    time_for_adding_bullets += dt
    if time_for_adding_bullets >= 1000:
        bullets.append(Bullet1(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
        bullets.append(Bullet2(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
        bullets.append(Bullet3(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
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

    bg_x -= 0.75 * player.to[0]   #미션 3 : player.to에 맞게 배경 이동
    bg_y -= 0.75 * player.to[1]   #가능하면 무한 배경 만들어보기 ?
    screen.blit(bg_image, (bg_x, bg_y))

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

            #2초 기다리고 게임 재시작, 3번 재시작하면 게임 종료?
            time.sleep(2)
            #과제 3, 총 5번 죽어야 게임이 끝나도록 만듬
            if player.life > 1 :
                pygame.init()
                #무적만들기

                player.life -= 1
            else:
                running = False

    draw_text(f"Time: {time.time() - start_time:.2f}, Bullets: {len(bullets)}", 16, (10, 10), WHITE)
    draw_player_health(screen, 10, 370, player.life / 5)        #미션 6 - 생명력막대기
    draw_text(f"Life : {player.life}", 16, (10, 350), WHITE)    #미션 6 - 생명력텍스트
    pygame.display.update()         #이걸 작성해야 화면이 바뀜!


    
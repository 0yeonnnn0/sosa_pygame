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

#미션 6 : 플레이어의 남은 생명력을 막대기로 표시한다.
def draw_player_health(scr,x,y,life):
    if life<0:
        life=0
    BAR_LENGTH=100
    LIFE_LENGTH = 50
    BAR_HEIGHT=20
    fill=life*LIFE_LENGTH
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

#게임 시작 시 나오는 화면
def draw_main_menu():
    global user_name

    draw_img(bg_image, 0, 0)
    draw_text("DODGE2023", 40, [130,20], YELLOW)
    draw_text("NAME? : ", 30, [50,90], WHITE)
    draw_text(f"{user_name}", 30, [185,90], YELLOW)
    draw_text("PRESS ENTER TO START!", 30, [60, 330], WHITE)
    pygame.display.update()

    global running
    global main_menu
    global start_time

    text_writing = True

    while text_writing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #X눌렀을때 게임닫기
                running = False
                text_writing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:            #이름 반환 및 text_writing 상태 종료
                    text_writing = False
                    break
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]              #마지막 문자 삭제
                    draw_img(bg_image, 0, 0)                #backspace를 구현하기 위해 전부 처음부터 다시 구현
                    draw_text("DODGE2023", 40, [130,20], YELLOW)
                    draw_text("NAME? : ", 30, [50,90], WHITE)
                    draw_text(f"{user_name}", 30, [185,90], YELLOW)
                    draw_text("PRESS ENTER TO START!", 30, [60, 330], WHITE)
                    pygame.display.update()
                else:
                    if len(user_name)>3:                    #최대 4글자만 가능
                        break
                    user_name += event.unicode              #유니코드 문자 추가
                    draw_text(f"{user_name}", 30, [185,90], YELLOW)#본인 이름 출력
                    pygame.display.update()
    else:
        main_menu = False
        start_time = time.time()
        draw_text(f"{user_name}", 30, [185,90], YELLOW)     #본인 이름 출력
        pygame.display.update()

def draw_game_over(name, sco):
    screen.blit(bg_image, (0, 0))    #초기화면으로 변경
    draw_text("!GAMEOVER!", 40, [120,20], YELLOW)   #GAMEOVER표시
    draw_text(f"YOUR NAME: {name} / SCORE: {sco}", 25, [50,60], WHITE)
    pygame.display.update()

def write_score(name, sco):
    f = open('gamelog.txt', 'a')
    f.write(f"{name}:{sco}")
    f.write("\n")
    f.close()
    global gameover
    global score_dict
    gameover = False
    rank_y = 1

    data_lines = open('gamelog.txt', 'r')
    keys = []
    values = []

    for line in data_lines:
        (value, key) = line.split(":")
        values.append(value)
        keys.append(float(key))

    data_lines.close()

    score_dict = list(zip(values, keys))
    score_dict.sort(key=lambda x:x[1], reverse=True)
    
    if len(score_dict) > 9:
        data_lines_write = open('gamelog.txt', 'w')

        dict_slice = 0
        while dict_slice<10:
            print(f"{score_dict[dict_slice][0]}:{score_dict[dict_slice][1]}")
            print(dict_slice)
            data_lines_write.write(f"{score_dict[dict_slice][0]}:{score_dict[dict_slice][1]}\n")
            dict_slice += 1
        data_lines_write.close()
        del(score_dict[-1])

    for i in score_dict:
        if rank_y < 6:
            if i[0] == name:
                draw_text(f"{i[0]} :: {i[1]}", 30, [80,90+rank_y*30], YELLOW)
            else:
                draw_text(f"{i[0]} :: {i[1]}", 30, [80,90+rank_y*30], WHITE)
            rank_y += 1
        else:
            if i[0] == name:
                draw_text(f"{i[0]} :: {i[1]}", 30, [270,rank_y*30-60], YELLOW)
            else:
                draw_text(f"{i[0]} :: {i[1]}", 30, [270,rank_y*30-60], WHITE)
            rank_y += 1

    draw_text("THANK YOU FOR ENJOY!", 25, [85,360], WHITE)
    pygame.display.update()
     
#게임 기본정보
pygame.init()
WIDTH, HEIGHT = 500, 400
pygame.display.set_caption("dodge2023")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player(screen)
user_name = ""

#효과음 목록
bgm = pygame.mixer.Sound("dodge_src/bgm.wav")
collisionBgm = pygame.mixer.Sound("dodge_src/collision.wav")
bgm.play(-1)

#그림 불러오기 및 크기조절
image = pygame.image.load("dodge_src/player.png")
image = pygame.transform.scale(image, (32, 32))
explosionImg = pygame.image.load("dodge_src/explosion.png")
explosionImg = pygame.transform.scale(explosionImg, (64, 64))
bg_image = pygame.image.load("dodge_src/bg.jpg")
bg_image = pygame.transform.scale(bg_image, (1000, 800))

#배경 위치
bg_x = -300
bg_y = -200

#시간
clock = pygame.time.Clock()
FPS = 60
start_time = 0      #게임 시작시간
colli_time = 0      #비행기가 총알에 맞은 시간

#총알 생성 
bullets = []
time_for_adding_bullets = 0

#게임 점수 및 게임오버 여부
gameover = True
main_menu = True
score = 0

#game Loop, 생명이 0 이하면 게임 종료
running = True

while running:
    if main_menu == True:
        draw_main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #X눌렀을때 게임닫기
                running = False
            if event.type == pygame.KEYDOWN:    #아무 키나 누르면 시작
                if event.key == pygame.K_RETURN:
                    main_menu = False
                    start_time = time.time()

    elif player.life > 0:
        dt = clock.tick(FPS)
        after_collision_time = time.time() - start_time - colli_time

        time_for_adding_bullets += dt

        if time_for_adding_bullets >= 1000:
            bullets.append(Bullet1(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
            bullets.append(Bullet2(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
            bullets.append(Bullet3(0, rnd.random()*HEIGHT, 2*(rnd.random()-0.5), 2*(rnd.random()-0.5)))
            time_for_adding_bullets -= 1000
        #게임 내 작동 버튼
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

        #미션 3 : 배경그림이 비행기의 움직임에 반응하여 같이 움직이도록 한다.
        bg_x -= 0.5 * player.to[0]
        bg_y -= 0.5 * player.to[1]
        screen.blit(bg_image, (bg_x, bg_y))

        player.update(dt, screen)
        player.draw(screen)

        for b in bullets:
            b.update_and_draw(dt, screen)

        for b in bullets:
            if collision(player, b):
                if after_collision_time < 3: #3초간 무적
                    pass
                else:
                    #시간이 지날수록 총알이 너무 많아지는 문제가 생겨 죽을 때마다 총알의 갯수를 초기화시킴 = 쾌적한 게임환경
                    bullets = []
                    #미션 1 : 비행기가 총알에 맞았을 때 효과음이 발생하도록 한다.
                    #충돌 시 배경음악 꺼짐, 충돌 BGM 켜짐
                    bgm.stop()
                    collisionBgm.set_volume(0.4)    #기본 효과음이 너무 시끄러워서 조용히 만들었습니다..
                    collisionBgm.play()
                    #미션 2 : 비행기가 총알에 맞았을 때 터지는 그림 효과가 나타나도록 한다.
                    draw_img(explosionImg, player.pos[0]-32, player.pos[1]-32)
                    pygame.display.update()
                    
                    colli_time = time.time() - start_time#충돌했을때 시
                    score += after_collision_time
                    score = round(score , 1)
                    #1초 기다리고 게임 재시작
                    time.sleep(1)
                    bgm.play(-1)
                    #미션 7 : 총알을 여러 종류로 만들고, 종류별로 크기와 색깔을 다르게 표현한다. (bullet.py)
                    #미션 8 : 총알의 종류마다 플레이어와 충돌했을 때 차감되는 생명력을 다르게 한다.
                    if b.name == Bullet1.name:
                        player.life -= 1
                    elif b.name == Bullet2.name:
                        player.life -= 2
                    elif b.name == Bullet3.name:
                        player.life -= 3

        #미션 4 : 총알에 맞으면 일정시간동안 무적이 되어야 정상적으로 작동한다 - 무적모드 3초                
        #미션 5 : 무적시간동안 비행기가 반짝거리도록 한다. (시작 후 3초간, 0.3초 간격으로 비행기 깜빡임)
        #set_alpha(128) = 반투명, set_alpha(255) = 평소와 동일
        if after_collision_time < 3:
            if after_collision_time < 0.3:
                player.image.set_alpha(128)
            elif after_collision_time>0.6 and after_collision_time<0.9:
                player.image.set_alpha(128)
            elif after_collision_time>1.2 and after_collision_time<1.5:
                player.image.set_alpha(128)
            elif after_collision_time>1.8 and after_collision_time<2.1:
                player.image.set_alpha(128)
            elif after_collision_time>2.4 and after_collision_time<2.7:
                player.image.set_alpha(128)
            else:
                player.image.set_alpha(255)  
        else:
            player.image = image
        #경과 시간과 총알의 갯수를 표시
        draw_text(f"Time: {time.time() - start_time:.1f}, Bullets: {len(bullets)}", 16, (10, 10), WHITE)
        draw_text(f"Pilot: {user_name}", 16, (405, 10), WHITE)
        #미션 6 : 남은 생명력을 막대기와 숫자로 표시한다.
        draw_player_health(screen, 10, 370, player.life / 5)        #미션 6 - 생명력막대기
        draw_text(f"Life : {player.life}", 16, (10, 350), WHITE)    #미션 6 - 생명력텍스트(숫자)
        pygame.display.update()         #이걸 작성해야 화면이 바뀜!

    #player의 체력이 0 이하가 되었을 때 게임을 종료하고 draw_game_over(), write_score() 함수를 실행
    elif player.life <= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #X눌렀을때 게임닫기
                running = False

        if gameover == True:
            draw_game_over(user_name, score)
            write_score(user_name, score)
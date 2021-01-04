import pygame
import json
import highscore
import os
# import threading
import random
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "done"
print(os.environ)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    
    base_path = ""
    #A:\py_game
    return os.path.join(base_path, relative_path)


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("himansh")
icon= pygame.image.load(resource_path("Untitled.png"))
pygame.display.set_icon(icon)
running = True
stop=False
r=False

score=0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 60)
playerico= pygame.image.load(resource_path("main_player.png"))
playericox=336
playericoy=500
playerX_change=0


#gameoverpic= pygame.image.load(resource_path("gameover.png"))

fireico= pygame.image.load(resource_path("fire1.png"))
fireicox=0
fireicoy=500
fireY_change= 13
fire_condision="ready"


background = pygame.image.load(resource_path('mybackgroung.png'))



enemyImg = []
enemyicox = []
enemyicoy = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemy_speed_control=0

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(resource_path('enemy.png')))
    enemyicox.append(random.randint(0+64,800-64))
    enemyicoy.append(random.randint(50, 120))
    enemyX_change.append(5)
    enemyY_change.append(40)
def player(x,y):
    screen.blit(playerico,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global fire_condision
    fire_condision="fire"
    screen.blit(fireico,(x+23,y+10))







def isCollision_done(enemyX1, enemyY1, bulletX1, bulletY1):
    distance = ((enemyX1 - bulletX1)*(enemyX1 - bulletX1)) + ((enemyY1 - bulletY1)*(enemyY1 - bulletY1))
    if distance < 64*10:
        return True
    else:
        return False

def game_over_display():
    over_text = over_font.render(" GAME OVER  BY HIMANSH", True, (255, 255, 255))
    screen.blit(over_text, (0, 250))
def scoreviewer():
    score_txt = font.render(f"Score : {score}",True,(255,255,255))
    screen.blit(score_txt,(10,10))
def highscoreviewer():
    main=highscore.highscore()
    get_score=main.main(score)
    score_txt = font.render(f"High Score : {str(get_score)}",True,(255,255,255))
    screen.blit(score_txt,(800-300,10))
# def speed_fast(i):
#     main_speed=enemyX_change[i]+enemy_speed_control
#     return main_speed






while running:
    speed_enhencer=score//50
    screen.fill((255,255,255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            print("game has shut down")

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if fire_condision == "ready":
                    # bulletSound = mixer.Sound("laser.wav")
                    # bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    fireicox = playericox 
                    fire_bullet(fireicox,fireicoy)
            if event.key== pygame.K_r:
                r=True
                stop=False
                playericox=336
                score=0
                
            if event.key==pygame.K_q : 
                running = False
                pygame.quit()
                print("game has shut down")
                sys.exit()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game has shut down")
            sys.exit()
    # if True:
    #     speed=score//10       
    #     if speed<=0:
    #         enemy_speed_control=0
    #     if speed>=1:
    #         enemy_speed_control=speed
        
    for i in range(num_of_enemies):
        speed=0
        enemyicox[i] += enemyX_change[i] 
        speed=enemyicox[i]+speed_enhencer
        if enemyicox[i] <= 0:
            enemyX_change[i] = 6
            enemyicoy[i] += enemyY_change[i]
        elif enemyicox[i] >= 736:
            enemyX_change[i] = -4
            enemyicoy[i] += enemyY_change[i]
        if r==True:
            enemyicoy[i]=random.randint(50,120)
            if i==5:
                r=False

        if enemyicoy[i] >= playericoy -64:
            game_over_display()
            stop=True
            break



        colide=isCollision_done(enemyicox[i],enemyicoy[i],fireicox,fireicoy)
        if colide:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyicox[i] = random.randint(0, 736)
            enemyicoy[i] = random.randint(50, 150)
            enemy(enemyicox[i], enemyicoy[i],i)
        if stop==False:
            enemy(speed,enemyicoy[i],i)

    playericox += playerX_change
    if playericox <= 0:
        playericox = 0
    elif playericox >= 736:
        playericox = 736

    if fireicoy <= 0:
        fireicoy = 480
        fire_condision = "ready"

    if fire_condision == "fire":
        fire_bullet(fireicox, fireicoy)
        fireicoy -= fireY_change

    player(playericox,playericoy)
    
    scoreviewer()
    highscoreviewer()
    pygame.display.update()

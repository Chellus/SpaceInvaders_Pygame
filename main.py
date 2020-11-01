import pygame
import random
import math

from pygame import mixer

#initialize pygame
pygame.init()
pygame.mixer.init()

window_w = 800 #width
window_h = 600 #height

spaceship_w = 64
enemy_w = 64

#create the window
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

#Background
background = pygame.image.load('resources/background.png')

#Background music
mixer.music.load('resources/background.wav')
mixer.music.play(-1) #play on loop

#Title and Icon
pygame.display.set_caption("Space Invaders - pygame")
icon = pygame.image.load('resources/ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('resources/player.png')
playerX = 370
playerY = 530
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('resources/enemy.png'))
    enemyX.append(random.randint(5, 750))
    enemyY.append(random.randint(25, 125))
    enemyX_change.append(3.5)

#Bullet
#if bullet_state = ready, you can't see the bullet
#if bullet_state = fire, the bullet is currently moving
bulletImg = pygame.image.load('resources/bullet.png')
bulletX = 0
bulletY = 530
bulletY_change = 15
bullet_state = 'ready'

#Score
score_value = 0
font = pygame.font.SysFont('comicsansms', 32)

textX = 10
textY = 10

#Game over text
over_font = pygame.font.SysFont('comicsansms', 64)

def textObjects(text, font):
    textSurface = font.render(text, True, (255, 255, 255)) #render the text with the font in white color
    return textSurface, textSurface.get_rect()

def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (0xFF, 0xFF, 0xFF))
    window.blit(score, (x, y))

def gameOverText():
    over_text = over_font.render("GAME OVER", True, (0xFF, 0xFF, 0xFF))
    window.blit(over_text, (200, 250))

def player(x, y):
    window.blit(playerImg, (x, y))

def enemy(x, y, i):
    window.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    window.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(((enemyX - bulletX) ** 2) + ((enemyY - bulletY) ** 2))
    if distance < 27:
        return True
    return False

def resetGameState():
    #Player
    global playerImg
    global playerX
    global playerY
    global playerX_change
    global player
    #Enemy
    global enemyImg
    global enemyX
    global enemyY
    global enemyX_change
    #Bullet
    global bulletImg
    global bulletX
    global bulletY
    global bulletY_change
    global bullet_state
    #Score
    global score_value
    #Reseting values
    playerImg = pygame.image.load('resources/player.png')
    playerX = 370
    playerY = 530
    playerX_change = 0
    #Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('resources/enemy.png'))
        enemyX.append(random.randint(5, 750))
        enemyY.append(random.randint(25, 125))
        enemyX_change.append(3.5)
    #Bullet
    bulletImg = pygame.image.load('resources/bullet.png')
    bulletX = 0
    bulletY = 530
    bulletY_change = 15
    bullet_state = 'ready'
    #score
    score_value = 0

intro = True
running = False
playing = False

if __name__ == "__main__":
    #start menu
    while intro:
        window.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False

        #space invaders text in screen
        largeText = pygame.font.SysFont('comicsansms', 50)
        textSurf, textRect = textObjects("Space Invaders", largeText)
        textRect.center = ((window_w/2), (window_h/2)-80)
        window.blit(textSurf, textRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #green play button
        if 180 + 200 > mouse[0] > 180 and 300 + 100 > mouse[1] > 300:
            pygame.draw.rect(window, (40, 240, 40), (180, 300, 200, 100))
            if click[0] == 1:
                playing = True
                running = True
                break
        else:
            pygame.draw.rect(window, (40, 180, 40), (180, 300, 200, 100))

        #red quit button
        if 420 + 200 > mouse[0] > 420 and 300 + 100 > mouse[1] > 300:
            pygame.draw.rect(window, (220, 40, 40), (420, 300, 200, 100))
            if click[0] == 1:
                break
        else:
            pygame.draw.rect(window, (180, 40, 40), (420, 300, 200, 100))

        playText = pygame.font.SysFont('comicsansms', 50)
        playSurf, playRect = textObjects("Play", playText)
        playRect.center = ((180 + (200 / 2)), (300 + (100 / 2)))
        window.blit(playSurf, playRect)

        quitText = pygame.font.SysFont('comicsansms', 50)
        quitSurf, quitRect = textObjects("Quit", quitText)
        quitRect.center = ((420 + (200 / 2)), (300 + (100 / 2)))
        window.blit(quitSurf, quitRect)

        pygame.display.update()
        clock.tick(30)

    #main game
    while running:
        while playing:

            window.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    playing = False
                    break

                #controlling movement of the spaceship
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -5
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 5
                    if event.key == pygame.K_SPACE:
                        if bullet_state is 'ready':
                            bullet_sound = mixer.Sound('resources/laser.wav') #load sound and play it
                            bullet_sound.play()
                            bulletX = playerX
                            bullet_state = 'fire'

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0

            #controlling boundaries of the window for the player
            if playerX + playerX_change > window_w - spaceship_w or playerX + playerX_change < 0:
                playerX_change = 0

            #controlling boundaries of the window for the enemy on the X axis
            for i in range(num_of_enemies):
                enemyX[i] += enemyX_change[i]
                if enemyX[i] + enemyX_change[i] > window_w - enemy_w:
                    enemyX_change[i] = -3.5
                    enemyY[i] += enemy_w #the width of the enemy is the same as the enemy height
                elif enemyX[i] + enemyX_change[i] < 0:
                    enemyX_change[i] = 3.5
                    enemyY[i] += enemy_w

                #Collision
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    explosion_sound = mixer.Sound('resources/explosion.wav')
                    explosion_sound.play()
                    bulletY = 480
                    enemyX[i] = random.randint(5, 750)  #reposition enemy
                    enemyY[i] = random.randint(25, 125)
                    enemyX_change[i] = 3.5
                    bullet_state = 'ready'
                    score_value += 1

                if enemyY[i] + enemy_w >= window_h - enemy_w:
                    playing = False
                    window.blit(background, (0, 0))
                    gameOverText()
                    gameOver = True

                    while gameOver:

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                break

                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()

                        #green play button
                        if 180 + 200 > mouse[0] > 180 and 400 + 100 > mouse[1] > 400:
                            pygame.draw.rect(window, (40, 240, 40), (180, 400, 200, 100))
                            if click[0] == 1:
                                playing = True
                                running = True
                                resetGameState()
                                break
                        else:
                            pygame.draw.rect(window, (40, 180, 40), (180, 400, 200, 100))

                        #red quit button
                        if 420 + 200 > mouse[0] > 420 and 400 + 100 > mouse[1] > 400:
                            pygame.draw.rect(window, (220, 40, 40), (420, 400, 200, 100))
                            if click[0] == 1:
                                playing = False
                                running = False
                                break
                        else:
                            pygame.draw.rect(window, (180, 40, 40), (420, 400, 200, 100))

                        playText = pygame.font.SysFont('comicsansms', 50)
                        playSurf, playRect = textObjects("Play", playText)
                        playRect.center = ((180 + (200 / 2)), (400 + (100 / 2)))
                        window.blit(playSurf, playRect)

                        quitText = pygame.font.SysFont('comicsansms', 50)
                        quitSurf, quitRect = textObjects("Quit", quitText)
                        quitRect.center = ((420 + (200 / 2)), (400 + (100 / 2)))
                        window.blit(quitSurf, quitRect)
                        pygame.display.update()
                        clock.tick(30)
                    break

                enemy(enemyX[i], enemyY[i], i) #show enemy

            playerX += playerX_change

            #Bullet movement
            if bulletY <= -20:
                bulletY = 530
                bullet_state = 'ready'

            if bullet_state is 'fire':
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change

            player(playerX, playerY) #show the player
            showScore(textX, textY)
            pygame.display.update()
            clock.tick(120)

        pygame.display.update()
        clock.tick(30)

    pygame.mixer.quit()
    pygame.quit()
    quit()

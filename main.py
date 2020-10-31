import pygame
import random
import math

#initialize pygame
pygame.init()

window_w = 800 #width
window_h = 600 #height

spaceship_w = 64
enemy_w = 64

#create the window
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

#Background
background = pygame.image.load('resources/background.png')

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
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('resources/enemy.png'))
    enemyX.append(random.randint(5, 750))
    enemyY.append(random.randint(25, 125))
    enemyX_change.append(4.5)

#Bullet
#if bullet_state = ready, you can't see the bullet
#if bullet_state = fire, the bullet is currently moving
bulletImg = pygame.image.load('resources/bullet.png')
bulletX = 0
bulletY = 530
bulletY_change = 15
bullet_state = 'ready'

score = 0

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

running = True

if __name__ == "__main__":
    while running:

        window.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #controlling movement of the spaceship
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is 'ready':
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
                enemyX_change[i] = -2.5
                enemyY[i] += enemy_w #the width of the enemy is the same as the enemy height
            elif enemyX[i] + enemyX_change[i] < 0:
                enemyX_change[i] = 2.5
                enemyY[i] += enemy_w

            #Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                enemyX[i] = random.randint(5, 750)  #reposition enemy
                enemyY[i] = random.randint(25, 125)
                enemyX_change[i] = 4.5
                bullet_state = 'ready'
                score += 1
                print(score)

            if enemyY[i] + enemy_w >= window_h - enemy_w:
                running = False
                
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

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

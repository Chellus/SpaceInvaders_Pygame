import pygame
import random

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
enemyImg = pygame.image.load('resources/enemy.png')
enemyX = random.randint(5, 730)
enemyY = 50
enemyX_change = 4.5
enemyY_change = 1.5 #the enemy goes down

def player(x, y):
    window.blit(playerImg, (x, y))

def enemy(x, y):
    window.blit(enemyImg, (x, y))

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
                elif event.key == pygame.K_RIGHT:
                    playerX_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        #controlling boundaries of the window for the player
        if playerX + playerX_change > window_w - spaceship_w or playerX + playerX_change < 0:
            playerX_change = 0

        #controlling boundaries of the window for the enemy on the X axis
        if enemyX + enemyX_change > window_w - enemy_w:
            enemyX_change = -2.5
            enemyY += enemy_w #the width of the enemy is the same as the enemy height
        elif enemyX + enemyX_change < 0:
            enemyX_change = 2.5
            enemyY += enemy_w

        if enemyY + enemyY_change >= window_h - enemy_w:
            running = False

        playerX += playerX_change
        enemyX += enemyX_change

        player(playerX, playerY) #show the player
        enemy(enemyX, enemyY) #show enemy

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

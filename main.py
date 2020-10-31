import pygame

#initialize pygame
pygame.init()

window_w = 800 #width
window_h = 600 #height

spaceship_w = 64

#create the window
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

#Title and Icon
pygame.display.set_caption("Space Invaders - pygame")
icon = pygame.image.load('resources/ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('resources/player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    window.blit(playerImg, (x, y))

running = True

if __name__ == "__main__":
    while running:
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

        #controlling boundaries of the window
        if playerX + playerX_change > window_w - spaceship_w or playerX + playerX_change < 0:
            playerX_change = 0

        playerX += playerX_change
        
        window.fill((0, 100, 0)) #RGB values to fill screen

        player(playerX, playerY) #show the player

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

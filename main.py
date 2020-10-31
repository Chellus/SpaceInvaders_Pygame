import pygame

#initialize pygame
pygame.init()

window_width = 800
window_height = 600

#create the window
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

#Title and Icon
pygame.display.set_caption("Space Invaders - pygame")
icon = pygame.image.load('resources/ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('resources/player.png')
playerX = 370
playerY = 480

def player():
    window.blit(playerImg, (playerX, playerY))

running = True

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            print(event)

        window.fill((0, 100, 0)) #RGB values to fill screen

        player() #show the player

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

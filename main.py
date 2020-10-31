import pygame

#initialize pygame
pygame.init()

window_height = 800
window_width = 600

#create the window
window = pygame.display.set_mode((window_height, window_width))
clock = pygame.time.Clock()

#Title and Icon
pygame.display.set_caption("Space Invaders - pygame")
icon = pygame.image.load('resources/ufo.png')
pygame.display.set_icon(icon)

running = True

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            print(event)

        window.fill((0, 0xFF, 0)) #RGB values to fill screen

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

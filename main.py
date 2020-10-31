import pygame

#initialize pygame
pygame.init()

window_height = 800
window_width = 600

#create the window
window = pygame.display.set_mode((window_height, window_width))

clock = pygame.time.Clock()

running = True

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            print(event)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

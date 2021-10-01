import pygame


# display window size
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation")

# global declarations

default_red = 150
default_yellow = 5
default_green = 20
default_minimum = 10
default_maximum = 60

truck_width = 12
truck_height = 45


BG_IMG = pygame.image.load("Assets/BG.png")


# draw window

def drawWindow():
    WIN.fill((255, 255, 255))
    WIN.blit(BG_IMG, (0, 0))
    WIN.blit(TRUCK, (0, 0))
    pygame.display.update()


# main
def main():
    clock = pygame.time.Clock()
    run = True
    while run:

        # FPS
        clock.tick(60)

        # event handler
        for event in pygame.event.get():

            # exit
            if event.type == pygame.QUIT:
                run = False

        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()

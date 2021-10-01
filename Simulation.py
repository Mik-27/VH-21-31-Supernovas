import pygame


# display window size
WIDTH, HEIGHT = 1400, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation")

# global declarations

default_red = 150
default_yellow = 5
default_green = 20
default_minimum = 10
default_maximum = 60

truck_width = 24
truck_height = 90


BG_IMG = pygame.image.load("Assets/BG.png")
TRUCK_IMG = pygame.image.load("Assets/Truck.png")
POLICE_IMG = pygame.image.load("Assets/Police.png")
BIKE_IMG = pygame.image.load("Assets/Bike.png")

# Truck initialization


def truck(value):
    if value == 1:
        angle = 0
        # position

    if value == 2:
        angle = 90
        # position

    if value == 3:
        angle = 180
        # position

    if value == 4:
        angle = 270
        # position

    return pygame.transform.rotate(pygame.transform.scale(TRUCK_IMG, (truck_width, truck_height)), angle)


# draw window

def drawWindow(rect_truck):
    WIN.fill((255, 255, 255))
    WIN.blit(BG_IMG, (0, 0))
    WIN.blit(truck(4), (rect_truck.x, rect_truck.y))
    pygame.display.update()


# main
def main():

    rect_truck = pygame.Rect(100, 100, truck_width, truck_height)

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
        rect_truck.x += 1

        drawWindow(rect_truck)

    pygame.quit()


if __name__ == "__main__":
    main()

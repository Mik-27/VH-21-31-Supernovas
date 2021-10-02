import random
import pygame
import time


junctions = ["j1", "j2", "j3", "j4", "j5", "j6"]

# Junction class definition


class Junction:

    def __init__(self, position):
        self.pos = position
        self.e_node = 0
        self.w_node = 0
        self.n_node = 0
        self.s_node = 0
        self.east = 0
        self.west = 0
        self.north = 0
        self.south = 0
        self.n_time = 0
        self.s_time = 0
        self.e_time = 0
        self.w_time = 20
        self.counter = 20
        self.signal = "w"
        self.checker = True
        if position == 1:
            self.s_node = 2
            self.e_node = 3
        elif position == 2:
            self.n_node = 1
            self.e_node = 4
        elif position == 3:
            self.w_node = 1
            self.s_node = 4
            self.e_node = 5
        elif position == 4:
            self.w_node = 2
            self.n_node = 3
            self.e_node = 6
        elif position == 5:
            self.s_node = 6
            self.w_node = 3
        elif position == 6:
            self.n_node = 5
            self.w_node = 4

    def randomize(self, value):  # left,center,right = randomize()
        l = 0
        r = 0
        c = 0
        if value > 30:
            value = 30
        for i in range(value):
            temp = random.randrange(0, 3)
            if temp == 0:
                l += 1
            elif temp == 1:
                r += 1
            elif temp == 2:
                c += 1
        return l, c, r

    def calcTime(self, value):
        # left,center,right = randomize()
        if value <= 10:
            return 10
        elif value >= 30:
            return 30
        else:
            return 20

    def countDown(self):
        self.counter -= 1
        if self.counter == 0:
            if self.signal == "w":
                self.signal = "n"
                self.counter = self.calcTime(self.north)
            elif self.signal == "n":
                self.signal = "e"
                self.counter = self.calcTime(self.east)
            elif self.signal == "e":
                self.signal = "s"
                self.counter = self.calcTime(self.south)
            elif self.signal == "s":
                self.signal = "w"
                self.counter = self.calcTime(self.west)
            print(self.signal)

    def feed(self, node, value, direction):
        if node == 0:
            return
        elif node == 1 and direction == "north":
            j1.north += value
        elif node == 1 and direction == "south":
            j1.south += value
        elif node == 1 and direction == "east":
            j1.east += value
        elif node == 1 and direction == "west":
            j1.west += value
        elif node == 2 and direction == "north":
            j2.north += value
        elif node == 2 and direction == "south":
            j2.south += value
        elif node == 2 and direction == "east":
            j2.east += value
        elif node == 2 and direction == "west":
            j2.west += value
        elif node == 3 and direction == "north":
            j3.north += value
        elif node == 3 and direction == "south":
            j3.south += value
        elif node == 3 and direction == "east":
            j3.east += value
        elif node == 3 and direction == "west":
            j3.west += value
        elif node == 4 and direction == "north":
            j4.north += value
        elif node == 4 and direction == "south":
            j4.south += value
        elif node == 4 and direction == "east":
            j4.east += value
        elif node == 4 and direction == "west":
            j4.west += value
        elif node == 5 and direction == "north":
            j5.north += value
        elif node == 5 and direction == "south":
            j5.south += value
        elif node == 5 and direction == "east":
            j5.east += value
        elif node == 5 and direction == "west":
            j5.west += value
        elif node == 6 and direction == "north":
            j6.north += value
        elif node == 6 and direction == "south":
            j6.south += value
        elif node == 6 and direction == "east":
            j6.east += value
        elif node == 6 and direction == "west":
            j6.west += value

    # value = no of cars on lane direction is initial direction
    def distribute(self, value, direction):
        time = self.calcTime(value)
        if direction == "e":
            s, w, n = self.randomize(value)
            self.east -= time
            if self.east < 0:
                self.east = 0
            self.feed(self.s_node, s, "north")
            self.feed(self.n_node, n, "south")
            self.feed(self.w_node, w, "east")
        if direction == "w":
            n, e, s = self.randomize(value)
            self.west -= time
            if self.west < 0:
                self.west = 0
            self.feed(self.s_node, s, "north")
            self.feed(self.n_node, n, "south")
            self.feed(self.e_node, e, "west")
        if direction == "n":
            e, s, w = self.randomize(value)
            self.north -= time
            if self.north < 0:
                self.north = 0
            self.feed(self.s_node, s, "north")
            self.feed(self.w_node, w, "east")
            self.feed(self.e_node, e, "west")
        if direction == "s":
            w, n, e = self.randomize(value)
            self.south -= time
            if self.south < 0:
                self.south = 0
            self.feed(self.n_node, n, "south")
            self.feed(self.w_node, w, "east")
            self.feed(self.e_node, e, "west")

    def loop(self):
        if self.checker != self.signal:
            self.checker = self.signal
            if self.signal == "n":
                self.distribute(self.north, self.signal)
            if self.signal == "e":
                self.distribute(self.east, self.signal)
            if self.signal == "w":
                self.distribute(self.west, self.signal)
            if self.signal == "s":
                self.distribute(self.south, self.signal)

        self.countDown()


j1 = Junction(1)
j2 = Junction(2)
j3 = Junction(3)
j4 = Junction(4)
j5 = Junction(5)
j6 = Junction(6)

j1.west = 30
j1.north = 60
j1.east = 20
j1.south = 38
j1.loop()


'''
# pygame

SIGNAL_WIDTH, SIGNAL_HEIGHT = 15, 45

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation")


BG_IMG = pygame.image.load("Assets/BG.png")
RED_IMG = pygame.image.load("Assets/Red.png")
YELLOW_IMG = pygame.image.load("Assets/Yellow.png")
GREEN_IMG = pygame.image.load("Assets/Green.png")
RED = pygame.transform.scale(RED_IMG, (SIGNAL_WIDTH, SIGNAL_HEIGHT))
YELLOW = pygame.transform.scale(YELLOW_IMG, (SIGNAL_WIDTH, SIGNAL_HEIGHT))
GREEN = pygame.transform.scale(GREEN_IMG, (SIGNAL_WIDTH, SIGNAL_HEIGHT))


def drawWindow():
    WIN.fill((255, 255, 255))
    WIN.blit(BG_IMG, (0, 0))
    pygame.draw.circle(WIN, (255, 0, 0), (345, 200), 15)  # j1 north
    pygame.draw.circle(WIN, (255, 0, 0), (665, 200), 15)  # j2 north
    pygame.draw.circle(WIN, (255, 0, 0), (985, 200), 15)  # j3 north
    pygame.draw.circle(WIN, (255, 0, 0), (345, 440), 15)  # j4 north
    pygame.draw.circle(WIN, (255, 0, 0), (665, 440), 15)  # j5 north
    pygame.draw.circle(WIN, (255, 0, 0), (985, 440), 15)  # j6 north
    pygame.draw.circle(WIN, (255, 0, 0), (360, 265), 15)  # j1 east
    pygame.draw.circle(WIN, (255, 0, 0), (680, 265), 15)  # j2 east
    pygame.draw.circle(WIN, (255, 0, 0), (1000, 265), 15)  # j3 east
    pygame.draw.circle(WIN, (255, 0, 0), (360, 505), 15)  # j4 east
    pygame.draw.circle(WIN, (255, 0, 0), (680, 505), 15)  # j5 east
    pygame.draw.circle(WIN, (255, 0, 0), (1000, 505), 15)  # j6 east
    pygame.draw.circle(WIN, (255, 0, 0), (280, 217), 15)  # j1 south
    pygame.draw.circle(WIN, (255, 0, 0), (600, 217), 15)  # j2 south
    pygame.draw.circle(WIN, (255, 0, 0), (920, 217), 15)  # j3 south
    pygame.draw.circle(WIN, (255, 0, 0), (280, 457), 15)  # j4 south
    pygame.draw.circle(WIN, (255, 0, 0), (600, 457), 15)  # j5 south
    pygame.draw.circle(WIN, (255, 0, 0), (920, 457), 15)  # j6 south
    pygame.draw.circle(WIN, (255, 0, 0), (295, 280), 15)  # j1 west
    pygame.draw.circle(WIN, (255, 0, 0), (615, 280), 15)  # j2 west
    pygame.draw.circle(WIN, (255, 0, 0), (935, 280), 15)  # j3 west
    pygame.draw.circle(WIN, (255, 0, 0), (295, 520), 15)  # j4 west
    pygame.draw.circle(WIN, (255, 0, 0), (615, 520), 15)  # j5 west
    pygame.draw.circle(WIN, (255, 0, 0), (935, 520), 15)  # j6 west
    pygame.display.update()

    # main


def main():

    clock = pygame.time.Clock()
    run = True
    while run:

        # FPS
        clock.tick(1)

        # event handler
        for event in pygame.event.get():

            # exit
            if event.type == pygame.QUIT:
                run = False
        j1.loop()
        j2.loop()
        j3.loop()

        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
'''

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
        self.w_time = 0
        self.maximum = 0
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

    # distribution randomizer

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

    # Traffic Signal Time Function

    def calcTime(self, value):
        # left,center,right = randomize()
        if value <= 10:
            return 10
        elif value >= 30:
            return 30
        else:
            return 20

    # Traffic Signal time countdown function

    def countDown(self):
        print(self.counter)
        self.counter -= 1
        if self.counter == 0:

            # old circular rotation code

            '''if self.signal == "w":
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
                self.counter = self.calcTime(self.west)'''

            # weighted approach

            # penalty logic

            if self.n_time >= 120:
                self.signal = "n"
                self.counter = self.calcTime(self.north)
                self.n_time = 0
                self.s_time += self.counter
                self.e_time += self.counter
                self.w_time += self.counter
            elif self.e_time >= 120:
                self.signal = "e"
                self.counter = self.calcTime(self.east)
                self.n_time += self.counter
                self.s_time += self.counter
                self.e_time = 0
                self.w_time += self.counter
            elif self.s_time >= 120:
                self.signal = "s"
                self.counter = self.calcTime(self.south)
                self.n_time += self.counter
                self.s_time = 0
                self.e_time += self.counter
                self.w_time += self.counter
            elif self.w_time >= 120:
                self.signal = "w"
                self.counter = self.calcTime(self.west)
                self.n_time += self.counter
                self.s_time += self.counter
                self.e_time += self.counter
                self.w_time = 0
            else:

                # Weight comparison
                dict2 = {}
                dict2["n"] = self.north
                dict2["s"] = self.south
                dict2["e"] = self.east
                dict2["w"] = self.west

                a = sorted(dict2.items(), key=lambda dict2: dict2[1])
                self.maxmimum = a[-1][1]
                if self.maximum == 0:
                    if self.signal == "w":
                        self.signal = "n"
                    elif self.signal == "n":
                        self.signal = "e"
                    elif self.signal == "e":
                        self.signal = "s"
                    elif self.signal == "s":
                        self.signal = "w"
                else:
                    self.signal = a[-1][0]
                if self.signal == "n":
                    #print(self.north, "adghj")
                    self.counter = self.calcTime(self.north)
                    self.n_time = 0
                    self.s_time += self.counter
                    self.e_time += self.counter
                    self.w_time += self.counter
                elif self.signal == "e":
                    self.counter = self.calcTime(self.east)
                    self.n_time += self.counter
                    self.s_time += self.counter
                    self.e_time = 0
                    self.w_time += self.counter
                elif self.signal == "s":
                    self.counter = self.calcTime(self.south)
                    self.n_time += self.counter
                    self.s_time = 0
                    self.e_time += self.counter
                    self.w_time += self.counter
                elif self.signal == "w":
                    self.counter = self.calcTime(self.west)
                    self.n_time += self.counter
                    self.s_time += self.counter
                    self.e_time += self.counter
                    self.w_time = 0

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

    # lane traffic distribution

    def distribute(self, value, direction):
        time = self.calcTime(value)
        if direction == "e":
            if value == 0:
                return
            s, w, n = self.randomize(value)
            self.east -= time
            if self.east < 0:
                self.east = 0
            self.feed(self.s_node, s, "north")
            self.feed(self.n_node, n, "south")
            self.feed(self.w_node, w, "east")
        if direction == "w":
            if value == 0:
                return
            n, e, s = self.randomize(value)
            self.west -= time
            if self.west < 0:
                self.west = 0
            self.feed(self.s_node, s, "north")
            self.feed(self.n_node, n, "south")
            self.feed(self.e_node, e, "west")
        if direction == "n":
            if value == 0:
                return
            e, s, w = self.randomize(value)
            self.north -= time
            if self.north < 0:
                self.north = 0
            self.feed(self.s_node, s, "north")
            self.feed(self.w_node, w, "east")
            self.feed(self.e_node, e, "west")
        if direction == "s":
            if value == 0:
                return
            w, n, e = self.randomize(value)
            self.south -= time
            if self.south < 0:
                self.south = 0
            self.feed(self.n_node, n, "south")
            self.feed(self.w_node, w, "east")
            self.feed(self.e_node, e, "west")

    def getSignal(self):
        return self.signal

    # function to be called in a loop

    def loop(self):
        self.countDown()
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


# obj init

j1 = Junction(1)
j2 = Junction(2)
j3 = Junction(3)
j4 = Junction(4)
j5 = Junction(5)
j6 = Junction(6)


# demo
'''
j1.west = 30
j1.north = 40
j1.east = 50
j1.south = 60

while True:
    j1.loop()
    time.sleep(1)
'''

j1.west = 10
j1.north = 20
j1.east = 20
j1.south = 60

j2.west = 10
j2.north = 20
j2.east = 20
j2.south = 60

j3.west = 10
j3.north = 20
j3.east = 20
j3.south = 60

j4.west = 10
j4.north = 20
j4.east = 20
j4.south = 60

j5.west = 10
j5.north = 20
j5.east = 20
j5.south = 60

j6.west = 10
j6.north = 20
j6.east = 20
j6.south = 60

# pygame
pygame.init()
SIGNAL_WIDTH, SIGNAL_HEIGHT = 15, 45

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation")
font = pygame.font.Font(None, 30)
black = (0, 0, 0)
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BG_IMG = pygame.image.load("Assets/BG.png")
RED_IMG = pygame.image.load("Assets/Red.png")
YELLOW_IMG = pygame.image.load("Assets/Yellow.png")
GREEN_IMG = pygame.image.load("Assets/Green.png")


def drawWindow(dict, vehicle, timer):
    WIN.fill((255, 255, 255))
    WIN.blit(BG_IMG, (0, 0))
    dict1 = {}
    dict1["j1n"] = RED
    dict1["j2n"] = RED
    dict1["j3n"] = RED
    dict1["j4n"] = RED
    dict1["j5n"] = RED
    dict1["j6n"] = RED
    dict1["j1s"] = RED
    dict1["j2s"] = RED
    dict1["j3s"] = RED
    dict1["j4s"] = RED
    dict1["j5s"] = RED
    dict1["j6s"] = RED
    dict1["j1w"] = RED
    dict1["j2w"] = RED
    dict1["j3w"] = RED
    dict1["j4w"] = RED
    dict1["j5w"] = RED
    dict1["j6w"] = RED
    dict1["j1e"] = RED
    dict1["j2e"] = RED
    dict1["j3e"] = RED
    dict1["j4e"] = RED
    dict1["j5e"] = RED
    dict1["j6e"] = RED

    for i in range(6):
        if i == 0:
            if dict["j1"] == "n":
                dict1["j1n"] = GREEN
            if dict["j1"] == "s":
                dict1["j1s"] = GREEN
            if dict["j1"] == "e":
                dict1["j1e"] = GREEN
            if dict["j1"] == "w":
                dict1["j1w"] = GREEN

        if i == 1:
            if dict["j2"] == "n":
                dict1["j2n"] = GREEN
            if dict["j2"] == "s":
                dict1["j2s"] = GREEN
            if dict["j2"] == "e":
                dict1["j2e"] = GREEN
            if dict["j2"] == "w":
                dict1["j2w"] = GREEN

        if i == 2:
            if dict["j3"] == "n":
                dict1["j3n"] = GREEN
            if dict["j3"] == "s":
                dict1["j3s"] = GREEN
            if dict["j3"] == "e":
                dict1["j3e"] = GREEN
            if dict["j3"] == "w":
                dict1["j3w"] = GREEN

        if i == 3:
            if dict["j4"] == "n":
                dict1["j4n"] = GREEN
            if dict["j4"] == "s":
                dict1["j4s"] = GREEN
            if dict["j4"] == "e":
                dict1["j4e"] = GREEN
            if dict["j4"] == "w":
                dict1["j4w"] = GREEN

        if i == 4:
            if dict["j5"] == "n":
                dict1["j5n"] = GREEN
            if dict["j5"] == "s":
                dict1["j5s"] = GREEN
            if dict["j5"] == "e":
                dict1["j5e"] = GREEN
            if dict["j5"] == "w":
                dict1["j5w"] = GREEN

        if i == 5:
            if dict["j6"] == "n":
                dict1["j6n"] = GREEN
            if dict["j6"] == "s":
                dict1["j6s"] = GREEN
            if dict["j6"] == "e":
                dict1["j6e"] = GREEN
            if dict["j6"] == "w":
                dict1["j6w"] = GREEN

    pygame.draw.circle(WIN, dict1["j1n"], (345, 200), 15)  # j1 north
    pygame.draw.circle(WIN, dict1["j2n"], (665, 200), 15)  # j2 north
    pygame.draw.circle(WIN, dict1["j3n"], (985, 200), 15)  # j3 north
    pygame.draw.circle(WIN, dict1["j4n"], (345, 440), 15)  # j4 north
    pygame.draw.circle(WIN, dict1["j5n"], (665, 440), 15)  # j5 north
    pygame.draw.circle(WIN, dict1["j6n"], (985, 440), 15)  # j6 north
    pygame.draw.circle(WIN, dict1["j1e"], (360, 265), 15)  # j1 east
    pygame.draw.circle(WIN, dict1["j2e"], (680, 265), 15)  # j2 east
    pygame.draw.circle(WIN, dict1["j3e"], (1000, 265), 15)  # j3 east
    pygame.draw.circle(WIN, dict1["j4e"], (360, 505), 15)  # j4 east
    pygame.draw.circle(WIN, dict1["j5e"], (680, 505), 15)  # j5 east
    pygame.draw.circle(WIN, dict1["j6e"], (1000, 505), 15)  # j6 east
    pygame.draw.circle(WIN, dict1["j1w"], (280, 217), 15)  # j1 west
    pygame.draw.circle(WIN, dict1["j2w"], (600, 217), 15)  # j2 west
    pygame.draw.circle(WIN, dict1["j3w"], (920, 217), 15)  # j3 west
    pygame.draw.circle(WIN, dict1["j4w"], (280, 457), 15)  # j4 west
    pygame.draw.circle(WIN, dict1["j5w"], (600, 457), 15)  # j5 west
    pygame.draw.circle(WIN, dict1["j6w"], (920, 457), 15)  # j6 west
    pygame.draw.circle(WIN, dict1["j1s"], (295, 280), 15)  # j1 south
    pygame.draw.circle(WIN, dict1["j2s"], (615, 280), 15)  # j2 south
    pygame.draw.circle(WIN, dict1["j3s"], (935, 280), 15)  # j3 south
    pygame.draw.circle(WIN, dict1["j4s"], (295, 520), 15)  # j4 south
    pygame.draw.circle(WIN, dict1["j5s"], (615, 520), 15)  # j5 south
    pygame.draw.circle(WIN, dict1["j6s"], (935, 520), 15)  # j6 south

    # Vehicle Count
    WIN.blit(font.render(str(vehicle["j1n"]), True, black, None), (334, 191))
    WIN.blit(font.render(str(vehicle["j3n"]), True, black, None), (654, 191))
    WIN.blit(font.render(str(vehicle["j5n"]), True, black, None), (974, 191))
    WIN.blit(font.render(str(vehicle["j2n"]), True, black, None), (334, 431))
    WIN.blit(font.render(str(vehicle["j4n"]), True, black, None), (654, 431))
    WIN.blit(font.render(str(vehicle["j6n"]), True, black, None), (974, 431))
    WIN.blit(font.render(str(vehicle["j1e"]), True, black, None), (349, 256))
    WIN.blit(font.render(str(vehicle["j3e"]), True, black, None), (669, 256))
    WIN.blit(font.render(str(vehicle["j5e"]), True, black, None), (989, 256))
    WIN.blit(font.render(str(vehicle["j2e"]), True, black, None), (349, 496))
    WIN.blit(font.render(str(vehicle["j4e"]), True, black, None), (669, 496))
    WIN.blit(font.render(str(vehicle["j6e"]), True, black, None), (989, 496))
    WIN.blit(font.render(str(vehicle["j1w"]), True, black, None), (269, 208))
    WIN.blit(font.render(str(vehicle["j3w"]), True, black, None), (589, 208))
    WIN.blit(font.render(str(vehicle["j5w"]), True, black, None), (909, 208))
    WIN.blit(font.render(str(vehicle["j2w"]), True, black, None), (269, 458))
    WIN.blit(font.render(str(vehicle["j4w"]), True, black, None), (589, 458))
    WIN.blit(font.render(str(vehicle["j6w"]), True, black, None), (909, 458))
    WIN.blit(font.render(str(vehicle["j1s"]), True, black, None), (284, 281))
    WIN.blit(font.render(str(vehicle["j3s"]), True, black, None), (604, 281))
    WIN.blit(font.render(str(vehicle["j5s"]), True, black, None), (924, 281))
    WIN.blit(font.render(str(vehicle["j2s"]), True, black, None), (284, 511))
    WIN.blit(font.render(str(vehicle["j4s"]), True, black, None), (589, 511))
    WIN.blit(font.render(str(vehicle["j6s"]), True, black, None), (909, 511))

    # Timer
    WIN.blit(font.render(str(timer["j1"]), True, black, None), (250, 180))
    WIN.blit(font.render(str(timer["j3"]), True, black, None), (560, 180))
    WIN.blit(font.render(str(timer["j5"]), True, black, None), (895, 180))
    WIN.blit(font.render(str(timer["j2"]), True, black, None), (250, 411))
    WIN.blit(font.render(str(timer["j4"]), True, black, None), (560, 411))
    WIN.blit(font.render(str(timer["j6"]), True, black, None), (895, 411))

    pygame.display.update()

#     # main
# def changeSignal(color, node, position):
#     if color == 'red':
#         pygame.draw.circle(WIN, (0, 255, 0), position, 15)
#     elif color == 'green':
#         pygame.draw.circle(WIN, (255, 0, 0), position, 15)


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
        j4.loop()
        j5.loop()
        j6.loop()

        dict = {}
        dict["j1"] = j1.getSignal()
        dict["j2"] = j2.getSignal()
        dict["j3"] = j3.getSignal()
        dict["j4"] = j4.getSignal()
        dict["j5"] = j5.getSignal()
        dict["j6"] = j6.getSignal()
        # print(j1.getSignal())

        vehicle = {}
        vehicle["j1n"] = j1.north
        vehicle["j1s"] = j1.south
        vehicle["j1e"] = j1.east
        vehicle["j1w"] = j1.west

        vehicle["j2n"] = j2.north
        vehicle["j2s"] = j2.south
        vehicle["j2e"] = j2.east
        vehicle["j2w"] = j2.west

        vehicle["j3n"] = j3.north
        vehicle["j3s"] = j3.south
        vehicle["j3e"] = j3.east
        vehicle["j3w"] = j3.west

        vehicle["j4n"] = j4.north
        vehicle["j4s"] = j4.south
        vehicle["j4e"] = j4.east
        vehicle["j4w"] = j4.west

        vehicle["j5n"] = j5.north
        vehicle["j5s"] = j5.south
        vehicle["j5e"] = j5.east
        vehicle["j5w"] = j5.west

        vehicle["j6n"] = j6.north
        vehicle["j6s"] = j6.south
        vehicle["j6e"] = j6.east
        vehicle["j6w"] = j6.west

        timer = {}
        timer["j1"] = j1.counter
        timer["j2"] = j2.counter
        timer["j3"] = j3.counter
        timer["j4"] = j4.counter
        timer["j5"] = j5.counter
        timer["j6"] = j6.counter

        drawWindow(dict, vehicle, timer)

    pygame.quit()


if __name__ == "__main__":
    main()

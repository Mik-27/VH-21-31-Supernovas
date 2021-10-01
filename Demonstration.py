import pygame
import random
import os
import sys


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
        if position == 1:
            s_node = 2
            e_node = 3
        elif position == 2:
            n_node = 1
            e_node = 4
        elif position == 3:
            w_node = 1
            s_node = 4
            e_node = 5
        elif position == 4:
            w_node = 2
            n_node = 3
            e_node = 6
        elif position == 5:
            s_node = 6
            w_node = 3
        elif position == 6:
            n_node = 5
            w_node = 4

    def randomize(self, value):  # left,center,right = randomize()
        for i in range(value):
            l = 0
            r = 0
            c = 0
            temp = random.randrange(0, 2)
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

    def feed(self, node, value, direction):
        if node == 0:
            return
        elif node == 1:
            j1.direction += value
        elif node == 2:
            j2.direction += value
        elif node == 3:
            j3.direction += value
        elif node == 4:
            j4.direction += value
        elif node == 5:
            j5.direction += value
        elif node == 6:
            j6.direction += value

    # value = no of cars on lane direction is initial direction
    def distribute(self, value, direction):
        time = calcTime(value)
        if direction == "e":
            s, w, n = randomize(value)
            self.east -= time
            if self.east < 0:
                self.east = 0
            feed(self.s_node, s, "north")
            feed(self.n_node, n, "south")
            feed(self.w_node, w, "east")
        if direction == "w":
            n, e, s = randomize(value)
            self.west -= time
            if self.west < 0:
                self.west = 0
            feed(self.s_node, s, "nouth")
            feed(self.n_node, n, "south")
            feed(self.e_node, e, "west")
        if direction == "n":
            e, s, w = randomize(value)
            self.north -= time
            if self.north < 0:
                self.north = 0
            feed(self.s_node, s, "north")
            feed(self.w_node, w, "east")
            feed(self.e_node, e, "west")
        if direction == "s":
            w, n, e = randomize(value)
            self.south -= time
            if self.south < 0:
                self.south = 0
            feed(self.n_node, n, "south")
            feed(self.w_node, w, "east")
            feed(self.e_node, e, "west")


j1 = Junction(1)
j2 = Junction(2)
j3 = Junction(3)
j4 = Junction(4)
j5 = Junction(5)
j6 = Junction(6)

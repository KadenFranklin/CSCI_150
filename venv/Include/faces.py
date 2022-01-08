from typing import *
from graphics import *
import random
import math

class Face:

    def __init__(self, x:int, y:int, size: float):
        self.x = x
        self.y = y
        self.size = size
        #vel_x = (random.randint(-100, 100)) / 100
        #vel_y = (random.randint(-100, 100)) / 100
        vel_x = 0
        vel_y = 0
        self.vx = vel_x
        self.vy = vel_y
        self.outline = Circle(Point(self.x, self.y), 50 * size)
        self.eye1 = Circle(Point(self.x - 20 * size, self.y - 25 * size)\
                           , 10 * size)
        self.eye2 = Circle(Point(self.x + 20 * size, self.y - 25 * size)\
                           , 10 * size)
        self.ear1 = Rectangle(Point(self.x - 49 * size, self.y - 10 * size), \
                              Point(self.x - 45 * size, self.y + 5 * size))
        self.ear2 = Rectangle(Point(self.x + 45 * size, self.y - 10 * size), \
                              Point(self.x + 49 * size, self.y + 5 * size))
        self.mouth = Rectangle(Point(self.x - 20 * size, self.y + 30 * size)\
                               , Point(self.x + 20 * size, self.y + 40 * size\
                                       ))
        self.nose1 = Line(Point(self.x + 5 * size, self.y - 10 * size), \
                          Point(self.x - 5 * size, self.y + 10 * size))
        self.nose2 = Line(Point(self.x - 5 * size, self.y + 10 * size), \
                          Point(self.x + 5 * size, self.y + 10 * size))

    def draw(self, win:GraphWin):
        self.outline.draw(win)
        self.eye1.draw(win)
        self.eye2.draw(win)
        self.ear1.draw(win)
        self.ear2.draw(win)
        self.mouth.draw(win)
        self.nose1.draw(win)
        self.nose2.draw(win)

        self.outline.setFill("#FFE39F")
        self.eye1.setFill("#0000FF")
        self.eye2.setFill("#0000FF")
        self.ear1.setFill("#FFE39F")
        self.ear2.setFill("#FFE39F")
        self.mouth.setFill("#E35D6A")

    def update(self, win: GraphWin):
        key_press = win.checkKey()
        if key_press == "w":
            self.vy -= 3
        if key_press == "a":
            self.vx -= 3
        if key_press == "s":
            self.vy += 3
        if key_press == "d":
            self.vx += 3

        self.x += self.vx
        if (self.x - self.outline.radius <= 0) \
                or (self.x + self.outline.radius >= 640):
            self.vx = 0
        self.y += self.vy
        if (self.y - self.outline.radius <= 0) or (self.y + self.outline.radius >= 480):
            self.vy = 0

        self.outline.move(self.vx, self.vy)
        self.eye1.move(self.vx, self.vy)
        self.eye2.move(self.vx, self.vy)
        self.ear1.move(self.vx, self.vy)
        self.ear2.move(self.vx, self.vy)
        self.mouth.move(self.vx, self.vy)
        self.nose1.move(self.vx, self.vy)
        self.nose2.move(self.vx, self.vy)
        self.vx = 0
        self.vy = 0

    def collision_det(self, faces : list):
        for f in faces:
            other: Face = f
            if math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)\
                    <= (self.outline.radius + other.outline.radius)\
                    and self.size < other.size:
                self.outline.undraw()
                self.eye1.undraw()
                self.eye2.undraw()
                self.ear1.undraw()
                self.ear2.undraw()
                self.mouth.undraw()
                self.nose1.undraw()
                self.nose2.undraw()

            if math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)\
                    <= self.outline.radius + other.outline.radius and\
                    other.size < self.size:
                other.outline.undraw()
                other.eye1.undraw()
                other.eye2.undraw()
                other.ear1.undraw()
                other.ear2.undraw()
                other.mouth.undraw()
                other.nose1.undraw()
                other.nose2.undraw()

def main():
    win = GraphWin("Making Faces", 640, 480, autoflush = False)
    faces = []
    a = random.randint(1, 10)
    a = 1
    for num in range(a):
        size_val = (random.randint(25, 200)) / 100
        x_val = random.randint(101, 539)
        y_val = random.randint(101, 379)
        faces.append(Face(x_val, y_val, size_val))

    for f in faces:
        f.draw(win)

    for i in range(100000):
        a += 1
        print(a)
        for f in faces:
            f.collision_det(faces)
            f.update(win)
        update(120)

main()
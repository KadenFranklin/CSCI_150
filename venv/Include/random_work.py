from typing import *
from graphics import *
import random
import math

def main():

    main_menu_win = GraphWin("random", 400, 400, autoflush=False)
    main_menu_win.setBackground("#191919")

    polygon_1 = Polygon([Point(200 + 9, 200 - 25), Point(200 - 9, 200 - 25), Point(200 - 25, 200 - 9), Point(200 - 25, 200 + 9), Point(200 - 9, 200 + 25), Point(200 + 9, 200 + 25), Point(200 + 25, 200 + 9), Point(200 + 25, 200 - 9)])

    polygon_1.draw(main_menu_win)
    polygon_1.setFill("#FFFFFF")

    main_menu_win.getMouse()
    main_menu_win.close()

main()


from graphics import *


def circle():
    win = GraphWin(200, 200) 
    c = Circle(Point(100,100),10)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()


circle()
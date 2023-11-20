from graphics import *


# def circle():
#     win = GraphWin(200, 200) 
#     c = Circle(Point(100,100),10)
#     c.draw(win)
#     win.getMouse() # pause for click in window
#     win.close()

# circle()

def progress():
    win = GraphWin ("thinula",1000,600)
    rec = Rectangle(Point(100,200), Point(200,300))
    rec2 = Rectangle(Point(250,100),Point(350,300))
    rec3 = Rectangle(Point(400,100),Point(500,300))
    rec4 = Rectangle(Point(550,100),Point(650,300))
    #                      x ,y           x,y
    aline = Line(Point(100,300),Point(800,300))

    msg  = Text(Point(150,50),"histrogram Result")
    pro_msg = Text(Point(150,330),"Progress")
    tra_msg = Text(Point(300,330),"Trailer")
    ret_msg = Text(Point(450,330),"Retriver")
    exc_msg = Text(Point(600,330),"Exclude")

    rec.setFill("red")
    rec2.setFill("green")
    rec3.setFill("blue")
    rec4.setFill("pink")
    aline.setArrow("last")

    aline.setWidth(3)

    rec.draw(win)
    rec2.draw(win)
    rec3.draw(win)
    rec4.draw(win)
    
    aline.draw(win)
    msg.draw(win)
    pro_msg.draw(win)
    tra_msg.draw(win)
    ret_msg.draw(win)
    exc_msg.draw(win)

    win.getMouse()
    win.close()

progress()
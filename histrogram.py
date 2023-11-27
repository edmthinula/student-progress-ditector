from graphics import *

def histogram(num1,num2,num3,num4):

    win = GraphWin ("thinula",1000,650)

    large = max(num1,num2,num3,num4)

    pixel = 400

    #num1 percentage

    percentage_num1 = (pixel/large)*num1 
    # print(percentage_num1)
    percentage_num2 = (pixel/large)*num2  
    #print(percentage_num2)
    percentage_num3 = (pixel/large)*num3 
    #print(percentage_num3)
    percentage_num4 = (pixel/large)*num4 
    #print(percentage_num4)

    bar_num1 = 400 - percentage_num1 + 100
    bar_num2 = 400 - percentage_num2 + 100
    bar_num3 = 400 - percentage_num3 + 100
    bar_num4 = 400 - percentage_num4 + 100

    total_outcome = num4 + num3 + num2 + num3

    #rectangel for represent progress
    rec = Rectangle(Point(100,bar_num1), Point(200,500))
    rec.setFill("red")
    rec.draw(win)

    #rectangle for represent Trailer
    rec2 = Rectangle(Point(250,bar_num2),Point(350,500))
    rec2.setFill("green")
    rec2.draw(win)

    #rectangle for represent Retriever 
    rec3 = Rectangle(Point(400,bar_num3),Point(500,500))
    rec3.setFill("blue")
    rec3.draw(win)
    
    #rectangle for represent Excluded 
    rec4 = Rectangle(Point(550,bar_num4),Point(650,500))
    #                      x ,y           x,y
    rec4.setFill("pink")
    rec4.draw(win)

    # drawing line
    aline = Line(Point(100,500),Point(800,500))
    aline.setArrow("last")
    aline.setWidth(3)
    aline.draw(win)

    #Text
    top_text  = Text(Point(150,50),"histrogram Result")
    text_bottom = Text(Point(170,590),f"outcomes in total {total_outcome}")

    pro_bar = Text(Point(150,bar_num1-10),f"{num1}")
    pro_text = Text(Point(150,530),"Progress")
    tra_bar = Text(Point(300,bar_num2-10),f"{num2}")
    tra_text = Text(Point(300,530),"Trailer")
    ret_bar = Text(Point(450,bar_num3-10),f"{num3}")
    ret_text = Text(Point(450,530),"Retriver")
    exc_bar = Text(Point(600,bar_num4-10),f"{num4}")
    exc_text = Text(Point(600,530),"Exclude")

    top_text.setStyle("bold")
    text_bottom.setStyle("bold")

    pro_text.setStyle("bold")
    tra_text.setStyle("bold")
    ret_text.setStyle("bold")
    exc_text.setStyle("bold")

    pro_bar.setStyle("bold")
    tra_bar.setStyle("bold")
    ret_bar.setStyle("bold")
    exc_bar.setStyle("bold")    

    top_text.draw(win)
    text_bottom.draw(win)

    pro_text.draw(win)
    tra_text.draw(win)
    ret_text.draw(win)
    exc_text.draw(win)

    pro_bar.draw(win)
    tra_bar.draw(win)
    ret_bar.draw(win)
    exc_bar.draw(win)

    #closing graphic window
    win.getMouse()
    win.close()


# num1 = 0
# num2 = 30
# num3 = 50
# num4 = 100

# histogram(num1,num2,num3,num4)

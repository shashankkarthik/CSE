import turtle
import time
verticle = int(input("Enter the lenght of the two verticle sides: "))
 
horizontal = 2 * verticle

turtle.color(0,1,0)

turtle.begin_fill()
turtle.down()

turtle.forward(horizontal)
turtle.right(90)
turtle.forward(verticle)
turtle.right(90)
turtle.forward(horizontal)
turtle.right(90)
turtle.forward(verticle)


turtle.end_fill()

time.sleep(5)

turtle.bye()


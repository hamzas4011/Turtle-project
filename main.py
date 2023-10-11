

#Importing turtle libary, creating objects and making a circle

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(200)
timmy.left(410)
timmy.right(410)
timmy.backward(60)
timmy.circle(160,360)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

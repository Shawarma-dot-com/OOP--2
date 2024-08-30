from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
#tim.color("pink")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def left_turn():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right_turn():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left_turn)
screen.onkey(key="d", fun=right_turn)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

from turtle import Turtle,Screen
import random
screen=Screen()
turtle_color=["red","blue","green","orange","yellow","purple"]
screen.setup(width=500,height=400)
user_input=screen.textinput("Turtle Race","Guess which turtle will win? and enter is color:")
y_axis=100
all_turtles=[]
for i in range(0,6):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(turtle_color[i])
    tim.goto(x=-230,y=y_axis-(i*40))
    all_turtles.append(tim)
looping=True
while looping==True:
    for i in all_turtles:
        if i.xcor()>240:
            looping=False
            winner_color=i.pencolor()
            if user_input.lower==winner_color:
                print(f"Your guess is correct!{winner_color} turtle is the winner!")
            else:
                print(f"Sorry! Your guess is not correct!but the winner is {winner_color} turtle!")
        i.forward(random.randint(1, 10))
screen.exitonclick()
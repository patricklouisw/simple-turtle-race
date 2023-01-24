import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

color = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
turtles = []

user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win? (Red, Orange, Yellow, Green, Blue, indigo, purple)")
while user_bet not in color:
    user_bet = screen.textinput(title="Make Your Bet!",
                                prompt="Colour is not valid! Choose (Red, Orange, Yellow, Green, Blue, indigo, purple)")

for i in range(len(color)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[i])
    new_turtle.goto(x=-230, y=90 - i * 30)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            print("Winner: %s! \nYou %s" % (winner, "win" if user_bet.lower() == winner else "lose"))
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
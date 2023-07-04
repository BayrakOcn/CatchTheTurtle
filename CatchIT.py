import turtle
import random
import time

board = turtle.Screen()
board.bgcolor("white")
board.title("Catch IT!")
board.setup(700, 700)

# Starting score and time
score = 0
startTime = time.time()
totalTime = 30
last_time_update = totalTime

# Turtle
my_turtle = turtle.Turtle("turtle")
my_turtle.speed(0)
my_turtle.penup()

# Score turtle
score_display = turtle.Turtle()
score_display.speed(0)
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 310)
score_display.write(f"Score: {score}", align="center", font=("Courier", 15, "normal"))

# Time turtle
timeBoard = turtle.Turtle()
timeBoard.speed(0)
timeBoard.penup()
timeBoard.hideturtle()
timeBoard.goto(0, 280)
timeBoard.write(f"Time left: {totalTime}", align="center", font=("Courier", 15, "normal"))


def move_turtle(t):
    x = random.randint(-340, 340)
    y = random.randint(-340, 340)
    t.goto(x, y)


def click(x, y):
    global score
    if time.time() - startTime < totalTime:
        if my_turtle.distance(x, y) < 20:
            score += 1
            score_display.clear()  # Clear old score
            score_display.write(f"Score: {score}", align="center", font=("Courier", 15, "normal"))  # new score


def auto_move():
    if time.time() - startTime < totalTime:
        move_turtle(my_turtle)
        board.ontimer(auto_move, 1000)  # 1 second


board.onclick(click)

# Start auto move
auto_move()

while True:
    board.update()
    if time.time() - startTime > totalTime:
        timeBoard.clear()
        timeBoard.write(f"Time is UP!", align="center", font=("Courier", 15, "normal"))
        break

    timeLeft = int(totalTime - (time.time() - startTime))

    if timeLeft != last_time_update:
        last_time_update = timeLeft
        timeBoard.clear()  # Clear old time
        timeBoard.write(f"Time Left: {timeLeft}", align="center", font=("Courier", 15, "normal"))  # new time

turtle.done()

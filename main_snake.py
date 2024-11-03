from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor("dark green")
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.tracer(False) 
 
score = 0
best_score = 0

snake_head = Turtle("square")
snake_head.color("black")
snake_head.speed(0)
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

apple = Turtle("circle")
apple.color("Firebrick")
apple.penup()
apple.goto(100, 100)

score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write(f"Skore: 0 Nejvyšší score: 0", align="center")


body_parts = []

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")


# Hlavní cyklus
while True:
    screen.update()
    if snake_head.xcor() > 290 or snake_head. ycor() > 290 or snake_head.xcor() < - 290 or snake_head.ycor() < - 290:
        time.sleep(2)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        for body_part in body_parts:
            body_part.goto(1000, 1000)
        body_parts.clear()
        score = 0
        score_sign.clear()
        score_sign.write(f"Skore: {score} Nejvyšší score: {best_score}", align="center")

    # food
    if snake_head.distance(apple) < 20:
        x = random.randint(- 280, 280)
        y = random.randint(- 280, 280)
        apple.goto(x, y)

        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("DimGray")
        new_body_part.penup()
        body_parts.append(new_body_part)

        score += 10
        if score > best_score:
            best_score = score
        score_sign.clear()
        score_sign.write(f"Skore: {score} Nejvyšší score: {best_score}", align="center")    

    for index in range(len(body_parts)-1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)
        
    if len(body_parts) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        body_parts[0].goto(x,y)

    move()

    for one_body_part in body_parts:
        if one_body_part.distance(snake_head) < 20:
            time.sleep(2)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            for body_part in body_parts:
                body_part.goto(1000, 1000)
            body_parts.clear()
            score = 0
            score_sign.clear()
            score_sign.write(f"Skore: {score} Nejvyšší score: {best_score}", align="center")

    time.sleep(0.2)
    
screen.exitonclick()
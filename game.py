import turtle 
import time 
import random 

delay = 0.1 

#SCORE 

score = 0 
high_score = 0 

#SET UP THE SCREEN 

wn = turtle.Screen()
wn.title("Snake Game!")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0) #This will turn off the screen updates 

#SNAKE HEAD 

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction = "STOP"

#SNAKE FOOD 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

segements = []

# PEN 

pen = turtle.Turtle
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0     High Score:0", align="center", 
          font= ("Courier", 24 "normal"))


#FUNCTIONS 
def go_up(): 
    if head.direction != "down": 
        head.direction = "up"

def go_down(): 
    if head.direction != "up": 
        head.direction = "down"

def go_left(): 
    if head.direction != "right": 
        head.direction = "left"

def go_right(): 
    if head.direction != "left": 
        head.direction = "right"

def move(): 
     if head.direction == "up": 
          y = head.ycor()
          head.sety(y + 20)

     if head.direction == "down": 
          y = head.ycor()
          head.sety(y - 20)

     if head.direction == "left": 
          x = head.xcor()
          head.setx(x - 20)

     if head.direction == "right": 
        x = head.xcor()
        head.setx(x + 20)


#KEYBOARD BINDINGS 
wn.listen()
wn.onkeypress(go_up, "UP") 
wn.onkeypress(go_down, "DOWN")
wn.onkeypress(go_left, "LEFT")
wn.keypress(go_right, "RIGHT")

#MAIN GAME LOOP 

while True: 
    wn.update()

    #FOR COLLISION WITH BORDER 
    if ( 
        head.xcor() > 290 
        or head.xcor() < -290 
        or head.ycor() > 290 
        or head.ycor() < -290 
    ): 
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "STOP"

    #HIDE THE SEGMENTS 
    for segment in segments: 
        segment.goto(1000, 1000)

    #CLEAR THE SEGMENTS LIST 
    segements.clear()

    #RESET THE SCORE 
    score = 0 

    #RESET THE DELAY 
    delay = 0.1 

    pen.clear()
    pen.write("Score:{}     High Score:{}".format(score, high_score), align="center",
               font=("Courier", 24, "normal"))

    #CHECK FOR A COLLISION WITH FOOD 

    if head.distance(food) < 20: 
            #MOVE THE FOOD TO A RANDOM POSITION 
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            #ADD A SEGMENT TO THE SNAKE 
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segements.append(new_segment)

            #SHORTEN THE DELAY 

            delay -= 0.001 
            
            #INCREASE THE SCORE 
            score += 10 

            if score > high_score: 
                high_score = score

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            #MOVE THE END SEGMENTS FIRST IN REVERSE ORDER 

            for index in range(len(segements) -1, 0, -1): 
                x = segements[index - 1].xcor()
                y = segements[index - 1].ycor()
                segements[index].goto(x,y)

            #MOVE SEGMENT 0 TO WHERE THE HEAD IS 
            if len(segements) > 0: 
                x = head.xcor()
                y = head.ycor()
                segements[0].goto(x,y)

            move()

            #CHECK FOR A COLLIISION WITH THE BODY
            for segment in segements: 
                if segment.distance(head) < 20: 
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "STOP"

                    #HIDE THE SEGMENTS 
                    for segment in segements: 
                        segment.goto(1000,1000)

                    #CLEAR THE SEGMENT LIST 
                    segment.clear()

                    #RESET THE SCORE 
                    score = 0 

                    #RESET THE DELAY 
                    delay = 0.1 

                    pen.clear()
                    pen.write("Score:   {}  High Score: {}",format(score, high_score), align="center", font=("Courier", 24, "normal"))

                    time.sleep(delay)
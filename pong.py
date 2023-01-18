import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_left=turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.penup()
paddle_left.goto(-370,0)
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_right=turtle.Turtle()
paddle_right=turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.penup()
paddle_right.goto(370,0)
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx= 0.8
ball.dy= 0.8

pen=turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A :0 Player B :0", align="center",font=("cambria",24,"normal"))

score_left=0
score_right=0
def paddle_left_up():
    y=paddle_left.ycor()
    y+=30
    paddle_left.sety(y)

def paddle_left_down():
    y=paddle_left.ycor()
    y-=30
    paddle_left.sety(y)
    
    
def paddle_right_down():
    y=paddle_right.ycor()
    y-=30
    paddle_right.sety(y)
    
    

def paddle_right_up():
    y=paddle_right.ycor()
    y+=30
    paddle_right.sety(y)





  
wn.listen()
wn.onkeypress(paddle_left_up,"w")
wn.onkeypress(paddle_left_down,"s")
wn.onkeypress(paddle_right_up,"Up")
wn.onkeypress(paddle_right_down,"Down")

while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor()>280:
        ball.sety(280)
        ball.dy*=-1
        
    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy*=-1 

    if ball.xcor()>390:
        ball.goto(0,0)
        score_left+=1
        pen.clear()
        pen.write("Player A :{} Player B :{}".format(score_left,score_right), align="center",font=("cambria",24,"normal"))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        score_right+=1
        pen.clear()
        pen.write("Player A :{} Player B :{}" .format(score_left,score_right), align="center",font=("cambria",24,"normal"))
        
    if(ball.xcor()>340 and ball.xcor()<350)and(ball.ycor()<paddle_right.ycor()+70 and ball.ycor()>paddle_right.ycor()-70):
        ball.setx(340)
        ball.dx*=-1
        
        
    if(ball.xcor()<-340 and ball.xcor()>-350)and(ball.ycor()<paddle_left.ycor()+70 and ball.ycor()>paddle_left.ycor()-70):
        ball.setx(-340)
        ball.dx*=-1
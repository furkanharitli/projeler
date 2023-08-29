import turtle as tr
import time as tm
import random
hiz=0.05
pencere=tr.Screen()
pencere.title("yılanoyunu")
pencere.bgcolor("lightgreen")
pencere.setup(width=600,height=600)

kafa=tr.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("black")
kafa.penup()
kafa.goto(0,100)
kafa.direction="stop"

kuyruk=[]

yem=tr.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0,0)
yem.direction="stop"

def move ():
    if kafa.direction=="up":
        y=kafa.ycor()
        kafa.sety(y+20)
    if kafa.direction=="down":
        y=kafa.ycor()
        kafa.sety(y-20)
    if kafa.direction=="right":
        x=kafa.xcor()
        kafa.setx(x+20)
    if kafa.direction=="left":
        x=kafa.xcor()
        kafa.setx(x-20)

def goUp():
    if kafa.direction !="down":
        kafa.direction="up"
def goDown():
    if kafa.direction != "up":
        kafa.direction="down"
def goRight():
    if kafa.direction != "left":
        kafa.direction="right"
def goLeft():
    if kafa.direction!="right":
        kafa.direction="left"

pencere.listen()
pencere.onkey(goUp,"Up")
pencere.onkey(goDown,"Down")
pencere.onkey(goRight,"Right")
pencere.onkey(goLeft,"Left")


while True:
    pencere.update()
    
    tm.sleep(hiz)
    if kafa.distance(yem)<20:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        yem.goto(x,y)
        yenikuyruk=tr.Turtle()
        kuyruk.append(yenikuyruk)
        yenikuyruk.shape("square")
        yenikuyruk.color("white")
        yenikuyruk.penup()
        
    for i in range(len(kuyruk)-1,0,-1):
        x=kuyruk[i-1].xcor()
        y=kuyruk[i-1].ycor()
        kuyruk[i].goto(x,y)
    if len(kuyruk)>0:
        x=kafa.xcor()
        y=kafa.ycor()
        kuyruk[0].goto(x,y)
    move()
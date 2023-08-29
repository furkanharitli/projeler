import tkinter as tk
import random 
import time as tm 
import turtle as tr
#Başlat fonksiyonu başlat butonuna basılınca aktifleşen fonksiyondur yılan oyunu devreye girer
def baslat():
    hiz=0.01
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

def cikis():
    pencere.destroy()

pencere = tk.Tk()
pencere.title("Yılan Oyunu")
pencere.geometry("300x150+200+400")

ust_cerceve = tk.Frame(pencere, bg="#0066cc")
ust_cerceve.pack(side=tk.TOP, fill=tk.X)

alt_cerceve = tk.Frame(pencere, bg="#d9d9d9")
alt_cerceve.pack(side=tk.BOTTOM, fill=tk.X)


#Arayüzdeki mavi şeridi oluşturu
baslik = tk.Label(ust_cerceve, text="Yılan oyunu", font=("Arial", 14), fg="#ffffff", bg="#0066cc", padx=10, pady=10)
baslik.pack(side=tk.LEFT)

#arayüzdeki başlat butonu
baslat_butonu = tk.Button(alt_cerceve, text="Başlat", font=("Arial", 12), width=8, pady=5, command=baslat)
baslat_butonu.pack(side=tk.LEFT, padx=10, pady=10)

#ara yüzdeki çıkış butonu
cikis_butonu = tk.Button(alt_cerceve, text="Çıkış", font=("Arial", 12), width=8, pady=5, command=cikis)
cikis_butonu.pack(side=tk.RIGHT, padx=10, pady=10)

pencere.mainloop()
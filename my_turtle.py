from random import randint,choice
import turtle

def race(turtles):
    if turtles > 10:
        print('Черепах должно быть не больше 10')
        return

    turtle.mode("logo")
    trt= turtle.Turtle()
    scr= turtle.Screen()

    g_width,g_height= setgame(turtles,scr,trt)
    
    trts = setturtles(turtles,g_width,g_height)
    
    run(trts,trt,g_width)

    scr.mainloop()

#-------------------------------------

def setgame(turtles, scr,trt):
    scr.setup(900, 450 if turtles <=3 else turtles * 60)
    game_width, game_height = scr.window_width() * 0.8, scr.window_height() * 0.8

    trt.speed(0)
    trt.penup()
    trt.goto(-game_width / 2, game_height / 2) 
    trt.pendown()
    trt.color('silver')
    for i in range(2):
        trt.right(90)
        trt.forward(game_width)
        trt.right(90)
        trt.forward(game_height)

    trt.right(180)
    
    for i in range(11):
        for num in range(10):
            trt.penup()
            trt.forward(game_height / 20)
            trt.pendown()
            trt.forward(game_height / 20)
        trt.penup()
        trt.backward(game_height)
        trt.pendown()
        trt.left(90)
        trt.forward(game_width/11)
        trt.write(i*10, align='center')
        trt.right(90)

    trt.penup()
    return game_width, game_height

#-------------------------------------

def setturtles(turtles,g_width,g_height):
    trts=[]
    colors=['blue', 'red', 'green', 'orange','black', 'yellow','darkblue', 'indigo','seagreen', 'lime','aqua']
    for i in range(turtles):
        t=turtle.Turtle()
        t.color(choice(colors))
        t.shape('turtle')

        t.goto(-g_width / 2 + 30, g_height / 2 - g_height /2 / turtles - g_height / turtles * i )
        t.setheading(90)
        t.clear()
        trts.append(t)

    return trts

#-------------------------------------

def run(trts,trt,game_width):
    win =False
    while not win:
        for idx, t in enumerate(trts):
            t.forward(randint(1,10))
            if t.position()[0]>= game_width/2-10:
                #trt.penup()
                trt.home()
                trt.write(f'Победила черепыха  {idx +1}', align='center',font=("Arial", 28, "normal"))
                win=True
                break    

#-------------------------------------

if __name__ == "__main__":
    race(3)


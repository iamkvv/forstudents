import turtle

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "?".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string
        print(end_string)

    return end_string


def draw_l_system(t, instructions, angle, distance):
    t.color("red","yellow")
    t.begin_fill()

    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
           
        elif cmd == '-':
            t.left(angle)

    t.end_fill()
   

def main(iterations, axiom, rules, angle, length=5, size=1, y_offset=0,
        x_offset=0, offset_angle=0, width=650, height=650):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)

    
    draw_l_system(t, inst, angle, length)

    wn.bgcolor("orange")
    #t.hideturtle()


axiom = "F+F+F+F" #  "F+XF+F+XF-" #
rules =  {"F":"F+FF++F+F"}   #{"X":"XF-F+F-XF+F+XF-F+F-X"}  #
iterations = 3 # TOP: 10
angle = 90

#main(iterations,axiom,rules,angle,x_offset=-100, y_offset=-10)    

def qv():
    t = turtle.Turtle()
    wn = turtle.Screen()

    wn.setup(600,600)
    t.down()

    t.begin_fill()
    for i in range(4):
        t.forward(250)
        t.left(90)

    t.end_fill()
qv()

#https://trinket.io/python/9339862606 Turtle race

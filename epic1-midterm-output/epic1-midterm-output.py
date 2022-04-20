import turtle as t

screen = t.Screen()
screen.setup(width = 1.0, height = 1.0)
t.pensize(2)

def spiral_shape(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.speed(0)
    t.bgcolor('black')
    t.pencolor('red')
    for a in range (155):
        t.right(a)
        t.circle(125, a)
        t.forward(a)
        t.right(90)

def cicrle_pattern(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for i in range(36):
        t.speed(11)
        t.pencolor('blue')
        t.circle(100)
        t.pencolor('yellow')
        t.forward(200)
        t.pencolor('orange')
        t.left(120)
        t.forward(100)
        t.pencolor('yellow')
        t.right(120)
        t.pencolor('orange')
        t.left(170)
        t.pencolor('blue')
        t.left(20)
        t.forward(15)

spiral_shape(0, 0)
cicrle_pattern(35, -70)
t.done()



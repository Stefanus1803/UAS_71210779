import turtle

t = turtle.Turtle()
turtle.speed(0)
t.pensize(3)

# Mengatur warna background
turtle.bgcolor('pink')
t.penup()
t.goto(-100, 0)
t.pencolor('yellow')
t.pendown()
t.begin_fill()

# Menggambar bentuk
t.goto(100, 0)
t.goto(120, 40)
t.goto(120, 220)
t.goto(100, 260)
t.goto(-100, 260)
t.goto(-120, 220)
t.goto(-120, 40)
t.goto(-100, 0)

# Mengatur warna untuk mengisi bentuk
t.fillcolor('yellow')
t.end_fill()
t.penup()
t.goto(0, 0)
t.pencolor('brown')
t.pendown()
t.begin_fill()

# Menggambar bentuknya
t.goto(0, -50)
t.goto(10, -50)
t.goto(10, 0)
t.goto(0, 0)

# MEngatur warna untuk mengisi bentuk
t.fillcolor('brown')
t.end_fill()
t.penup()
t.goto(-30, 20)
t.pendown()

# Me Set Warna Pena
t.pencolor('red')

# Menggambar Huruf H
t.goto(-30, 60)
t.goto(-30, 40)
t.goto(-15, 40)
t.goto(-15, 60)
t.goto(-15, 20)
t.penup()
t.goto(-10, 20)
t.pendown()

# Menggambar Huruf I
t.goto(0, 20)
t.goto(-5, 20)
t.goto(-5, 60)
t.goto(-10, 60)
t.goto(0, 60)
t.penup()
t.goto(20, 20)
t.pendown()

t.dot(4)
t.penup()
t.goto(20, 25)
t.pendown()
t.goto(20, 60)
t.penup()
t.goto(0, 100)
t.pendown()
t.pencolor('blue')
t.circle(60)
t.penup()
t.goto(-25, 120)
t.pendown()
t.pencolor('red')

for i in range(10):
    t.forward(50)
    t.left(108)
    t.hideturtle()

turtle.done()
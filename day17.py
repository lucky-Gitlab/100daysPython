import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_line(color, x1, y1, x2, y2, width=2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.width(width)
    turtle.pencolor(color)
    turtle.goto(x2, y2)

def draw_ellipse(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y - height)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.circle(width, 90)
        turtle.circle(height, 90)
    turtle.end_fill()

def draw_doraemon():
    turtle.speed(0)
    turtle.bgcolor("white")
    
    # Face
    draw_circle("skyblue", 0, 50, 150)
    draw_circle("white", 0, 50, 140)
    
    # Eyes
    draw_circle("white", -50, 130, 30)
    draw_circle("white", 50, 130, 30)
    draw_circle("black", -50, 140, 10)
    draw_circle("black", 50, 140, 10)
    
    # Nose
    draw_circle("red", 0, 110, 15)
    draw_line("black", 0, 110, 0, 80)
    
    # Mouth
    turtle.penup()
    turtle.goto(-70, 60)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.width(2)
    turtle.circle(80, 120)
    
    # Whiskers
    draw_line("black", -100, 90, -50, 90)
    draw_line("black", 50, 90, 100, 90)
    draw_line("black", -100, 70, -50, 80)
    draw_line("black", 50, 80, 100, 70)
    draw_line("black", -100, 50, -50, 70)
    draw_line("black", 50, 70, 100, 50)
    
    # Body
    draw_circle("skyblue", 0, -100, 100)
    draw_circle("white", 0, -50, 80)
    
    # Bell
    draw_circle("yellow", 0, -50, 15)
    draw_line("black", -15, -65, 15, -65)
    
    # Arms
    draw_circle("skyblue", -120, -20, 30)
    draw_circle("skyblue", 120, -20, 30)
    
    # Legs
    draw_circle("skyblue", -60, -180, 40)
    draw_circle("skyblue", 60, -180, 40)
    draw_circle("white", -60, -180, 30)
    draw_circle("white", 60, -180, 30)
    
    # Pouch
    turtle.penup()
    turtle.goto(-40, -80)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.circle(40, 180)
    
    # Complete
    turtle.done()

draw_doraemon()

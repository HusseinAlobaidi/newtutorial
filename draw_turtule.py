import turtle

def draw_square(some_turtle):
    # degree =90
    # for i in range(1, 200):
    #     some_turtle.forward(100)
    #     some_turtle.right(degree)
    #     degree = 90
    #     if i % 4 == 0:
    #         degree += 10
    for i in range(2):
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)




def draw_art():
    window = turtle._getscreen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(0)
    draw_square(brad)

    # angi = turtle.Turtle()
    # angi.shape("arrow")
    # angi.color('blue')
    # angi.speed(2)
    # angi.circle(100)

    window.exitonclick()
draw_art()

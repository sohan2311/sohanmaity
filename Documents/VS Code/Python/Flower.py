import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("blue")
    flower.speed(100)

    for _ in range(36):
        flower.forward(130)
        flower.right(45)
        flower.forward(130)
        flower.right(135)
        flower.forward(130)
        flower.right(45)
        flower.forward(130)
        flower.right(135)
        flower.right(10)


    flower.right(90)
    flower.forward(300)

    window.exitonclick()

draw_flower()



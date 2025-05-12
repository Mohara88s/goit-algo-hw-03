import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake():
    order = int(input("Уведіть бажаний рівень рекурсії сніжинки?"))
    size=300
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    for _ in range(0, 3):
        koch_curve(t, order, size=300)
        t.left(-120)

    window.mainloop()


if __name__ == "__main__":
    draw_koch_snowflake()

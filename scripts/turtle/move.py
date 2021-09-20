import turtle

turt = turtle.Turtle()
screen = turtle.getscreen()
turt.speed(10)
f = open("turtle", "r")
color = ["red", "green", "blue", "grey", "black", "yellow"]
color_ind = 0
turt.pencolor("white")
turt.setheading(90)
while 1:
    for line in f:
        if line == "\n":
            if color_ind == 4:
                continue
            color_ind += 1
            turt.pencolor("white")
            turt.goto(100 * color_ind, 0)
            turt.setheading(90)
            # turt.up()
            continue
        turt.pencolor(color[color_ind])
        words = line.split()
        if words[0] == "Avance":
            turt.forward((float)(words[1]))
        elif words[0] == "Recule":
            turt.back((float)(words[1]))
        elif (words[0] == "Tourne") & (words[1] == "droite"):
            turt.right((float)(words[3]))
        elif (words[0] == "Tourne") & (words[1] == "gauche"):
             turt.left((float)(words[3]))

#



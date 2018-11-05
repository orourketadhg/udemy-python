import tkinter
import math


def parabola(plot_canvas, size):
    for x in range(size):
        # makes parabola smaller
        z = x * x / size
        plot(plot_canvas, x, z)
        plot(plot_canvas, -x, z)

    # return z


# generate circles
def circle(page, radius, g=0, h=0):
    for x in range(g, g + radius):
        y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        # create 4 parabolas each 1/4 of the circle
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


# move origin to center of canvas -- default is left top
def draw_axis(canvas_template):
    # canvas_template to be updated
    canvas_template.update()
    # find new origin points
    x_origin = canvas_template.winfo_width() / 2
    y_origin = canvas_template.winfo_height() / 2
    # gets the new outer edge points
    canvas_template.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    # draw lines on zero lines
    # (x1, y1) is the starting point, (x2, y2) is the end point - .create_line(x1, y1, x2, y2), fill="" is the colour
    canvas_template.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas_template.create_line(0, y_origin, 0, -y_origin, fill="black")
    # prints local variables
    print(locals())


def plot(canvas_template, x, y):
    canvas_template.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480,)
canvas.grid(row=0, column=0)

# # second canvas
# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background='blue')
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
draw_axis(canvas)
# draw_axis(canvas2)


# for i in range(-100, 100):
#     y = parabola(i)
#     # -y to invert
#     plot(canvas, i, -y)

# turned into a function that requires the
parabola(canvas, 300)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)
circle(canvas, 100)

mainWindow.mainloop()

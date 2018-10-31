import tkinter


def parabola(x):
    # makes parabola smaller
    z = x * x / 100
    return z


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
    canvas_template.create_line(0, -y_origin, 0, y_origin, fill="black")
    # prints local variables
    print(locals())


def plot(canvas_template, x, y):
    canvas_template.create_line(x, y, x + 1, y + 1, fill="white")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=320, height=480, background='red' )
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background='blue')
canvas2.grid(row=0, column=1)

print(repr(canvas), repr(canvas2))
draw_axis(canvas)
draw_axis(canvas2)


for i in range(-100, 100):
    y = parabola(i)
    # -y to invert
    plot(canvas, i, -y)

mainWindow.mainloop()

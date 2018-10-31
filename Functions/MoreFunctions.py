import tkinter


def parabola(x):
    # makes parabola smaller
    z = x * x / 100
    return z


# move origin to center of canvas -- default is left top
def draw_axis(canvas):
    # canvas to be updated
    canvas.update()
    # find new origin points
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    # gets the new outer edge points
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    # draw lines on zero lines
    # (x1, y1) is the starting point, (x2, y2) is the end point - .create_line(x1, y1, x2, y2), fill="" is the colour
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axis(canvas)


for i in range(-100, 100):
    y = parabola(i)
    # -y to invert
    plot(canvas, i, -y)

mainWindow.mainloop()

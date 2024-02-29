import turtle
from tancalc import TanCalc

cavity_diagram = "cavity_diagram.gif"


screen = turtle.Screen()
screen.setup(height=500, width=800)
screen.title("TOA Calculator For Valve Cavities")
screen.addshape(cavity_diagram)
turtle.shape(cavity_diagram)
screen.bgcolor("gray")
unit = "mm"
tancalc = TanCalc(unit)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

while True:
    diameter1 = float(screen.numinput(title="Enter Cavity Details", prompt="First Diameter:"))
    screen.tracer(1)
    diameter2 = float(screen.numinput(title="Enter Cavity Details", prompt="Second Diameter:"))
    screen.tracer(1)
    angle = float(screen.numinput(title="Enter Cavity Details", prompt="Angle:"))
    screen.tracer(1)
    bottom_depth = float(screen.numinput(title="Enter Cavity Details", prompt="BOA Depth:"))
    screen.tracer(1)
    tancalc.top_depth_calc(angle=angle, diameter1=diameter1, diameter2=diameter2, bottom_depth=bottom_depth)


turtle.mainloop()

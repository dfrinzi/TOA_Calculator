import turtle
from tancalc import TanCalc

tancalc = TanCalc()
screen = turtle.Screen()
screen.title("TOA Calculator For Valve Cavities")

while True:
    diameter1 = float(screen.textinput(title="Enter Cavity Details", prompt="First Diameter:"))
    screen.tracer(1)
    diameter2 = float(screen.textinput(title="Enter Cavity Details", prompt="Second Diameter:"))
    screen.tracer(1)
    angle = float(screen.textinput(title="Enter Cavity Details", prompt="Angle:"))
    screen.tracer(1)
    bottom_depth = float(screen.textinput(title="Enter Cavity Details", prompt="BOA Depth:"))
    screen.tracer(1)
    tancalc.top_depth_calc(angle=angle, diameter1=diameter1, diameter2=diameter2, bottom_depth=bottom_depth)


turtle.mainloop()

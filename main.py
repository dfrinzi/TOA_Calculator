import turtle
import pandas
from tancalc import TanCalc
from diameter_writer import DiameterWriter
from result_writer import ResultWriter

cavity_diagram = "cavity_diagram.gif"
DIA_REF = "Minor Dia Ref.csv"

screen = turtle.Screen()
screen.tracer(0)
screen.setup(height=500, width=900)
screen.title("TOA Calculator For Valve Cavities")
screen.addshape(cavity_diagram)
turtle.shape(cavity_diagram)
screen.bgcolor("gray")

diameter_writer = DiameterWriter()
diameter_writer.output_list(pandas.read_csv(DIA_REF))

unit = "mm"
tancalc = TanCalc(unit)
screen.update()
result_writer = ResultWriter()

while True:
    diameter1 = float(screen.numinput(title="Enter Cavity Details", prompt="First Diameter:"))
    result_writer.clear_output()
    screen.tracer(1)
    diameter2 = float(screen.numinput(title="Enter Cavity Details", prompt="Second Diameter:"))
    screen.tracer(1)
    angle = float(screen.numinput(title="Enter Cavity Details", prompt="Angle:"))
    screen.tracer(1)
    bottom_depth = float(screen.numinput(title="Enter Cavity Details", prompt="BOA Depth:"))
    screen.tracer(1)
    screen.tracer(0)

    output = tancalc.top_depth_calc(angle=angle, diameter1=diameter1, diameter2=diameter2, bottom_depth=bottom_depth)
    result_writer.output_list(output[0], output[1])
    screen.update()





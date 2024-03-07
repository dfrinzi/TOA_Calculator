from turtle import Turtle
INITIAL_X = 150
INITIAL_Y = 180


class DiameterWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(INITIAL_X, INITIAL_Y)

        self.vert_spacing = 35
        self.hor_spacing = 100

    def output_list(self, data_list):
        self.write("Minor Dia Ref", align="left", font=("Calibri", 24, "bold"))
        self.goto(self.xcor(), self.ycor() - self.vert_spacing)
        self.write("Cavity", align="left", font=("Calibri", 18, "bold"))
        for cavity in data_list["Cavity"]:
            self.goto(self.xcor(), self.ycor() - self.vert_spacing)
            self.write(f"{cavity}", align="left", font=("Calibri", 18, "normal"))

        self.goto(INITIAL_X + self.hor_spacing, INITIAL_Y - self.vert_spacing)
        self.write("Minor Dia (+.05)", align="left", font=("Calibri", 18, "bold"))
        for dia in data_list["Minor_Dia"]:
            self.goto(self.xcor(), self.ycor() - self.vert_spacing)
            self.write(f"{dia}", align="left", font=("Calibri", 18, "normal"))

    def goto_column_top(self):
        self.goto(self.xcor(), self.ycor() - self.vert_spacing)
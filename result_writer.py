from turtle import Turtle
INITIAL_X = -105
INITIAL_Y = -125


class ResultWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(INITIAL_X, INITIAL_Y)

        self.vert_spacing = 25
        self.hor_spacing_column = 140
        self.hor_spacing_section = 50

    def clear_output(self):
        self.clear()
        self.goto(INITIAL_X, INITIAL_Y)

    def output_list(self, entered_data, result_data):
        self.write("You Entered:", align="left", font=("Calibri", 14, "bold"))

        for key in entered_data:
            self.next_line()
            self.write(f"{key}", align="left", font=("Calibri", 14, "normal"))

        self.next_column_top()

        for key in entered_data:
            self.next_line()
            self.write(f"{entered_data[key]}", align="left", font=("Calibri", 14, "normal"))

        self.next_section()
        self.next_line()
        self.next_line()

        for key in result_data:
            self.next_line()
            self.write(f"{key}", align="left", font=("Calibri", 14, "bold"))

        self.next_column_top()
        self.next_line()
        self.next_line()
        for key in result_data:
            self.next_line()
            self.write(f"{result_data[key]}", align="left", font=("Calibri", 14, "normal"))

    def next_line(self):
        self.goto(self.xcor(), self.ycor() - self.vert_spacing)

    def next_section(self):
        self.goto(self.xcor() + self.hor_spacing_section, INITIAL_Y)

    def next_column_top(self):
        self.goto(self.xcor() + self.hor_spacing_column, INITIAL_Y)

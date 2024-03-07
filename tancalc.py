import math

# decimal places in result, mm/2 is default
MM_PRECISION = 2
IN_PRECISION = 3
PI = math.pi


class TanCalc:
    def __init__(self, unit):
        self.unit = unit
        self.precision = MM_PRECISION

    def top_depth_calc(self, angle, diameter1, diameter2, bottom_depth,):
        half_angle = abs(angle * .5)
        diameter1 = abs(diameter1)
        diameter2 = abs(diameter2)
        bottom_depth = abs(bottom_depth)

        if self.unit == "in":
            self.precision = IN_PRECISION

        tan_result = round(math.tan(half_angle * PI / 180), 10)
        radial_change = abs(diameter1 - diameter2) * .5
        depth_change = radial_change / tan_result
        top_depth = round(bottom_depth - depth_change, self.precision)

        # print(f"tan_result: {round(tan_result, 4)}")
        # print(f"radial_change: {round(radial_change, 4)}")
        # print(f"depth_change: {round(depth_change, 4)}")
        # print(f"top_depth: {round(top_depth, 4)}")

        entered_data = {
            "First Diameter:": diameter1,
            "Second Diameter:": diameter2,
            "Included Angle:": angle,
            "BOA Depth:": bottom_depth
        }

        result_data = {
            # "Depth Change to TOA:": depth_change,
            "TOA Depth:": top_depth
        }

        return entered_data, result_data




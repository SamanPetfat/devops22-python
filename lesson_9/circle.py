from math import pi
from turtle import circle, color

class Circle:
    def __init__(self,radie):
        self.radie = radie
        self.color = "gray"
        self.area_circle()
        self.diameter_circle()
        pass

    def diameter_circle(self):
        pass
        return 2 * self.radie

    def area_circle(self):
        pass
        return float(pi*self.radie **2)

    def circumference_circle(self):
        pass
        return float(2*pi*self.radie)

    def set_color(self,color):
        self.color = color ## no return ?



if __name__ == "__main__":
    mycircle = Circle(10)

    mycircle.set_color("red") # Does this change the color? DEfault is gray, because i set it in "innit"?
    print(f"Area: {mycircle.area_circle()}")
    print(f"Diameter: {mycircle.diameter_circle()}")
    print(f"Circumference: {mycircle.circumference_circle()}")
    print(f"Color: {mycircle.color}")







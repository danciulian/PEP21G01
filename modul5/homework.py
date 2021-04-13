""" Homework 5 - needs to be presented before exam day"""

# We want to create class for an object that behaves like a triangle, that has flexible sides and angles.
# Because of approximations in python the triangle will get distorted after some of the changes so this is not a
# perfect model

# 30P
#  - class constructor can receive 3 arguments for angles (with default value of 60) and 3 arguments for sides (with
# default value of 1)
# class variables for sides will be called A, B, C
# class variables for angles will be called AB, BC, CA (indicating sides)

# 30P
# - class implements method to modify_angle:
#   - modify_angle method takes two argument:
#       - "angle" and can be one of 3 string values 'AB', 'BC', 'CA'
#       - "degrees" that can be a positive or negative and represents the amount by which the angle will be modified
# If as a result of the change any of the angles will be outside interval (0, 180) then method should raise an exception
# When an angel is modifies you will need to recalculate the opposing side which can be done using the following
# example: angle AB is changed then C = (A**2 + B**2 - 2*A*B*cos(AB))**(1/2)
# Because angles in a triangle must sum up to 180 degrees unmodified angles need to be recalculated after we have
# recalculated the opposite side using the following example:
# angle AB is changed then BC = arccos((B**2+ C**2 - A**2) / 2*B*C), CA = arccos((C**2+ A**2 - B**2) / 2*C*A),


# 30P
# - class implements method to modify_side:
#   - modify_side method takes two argument:
#       - "side" and can be one of 3 string values 'A', 'B', 'C'
#       - "meters" that can be a positive or negative and represents the amount by which the side will be modified
# If as a result of the change sum of the unmodified sides is less than or equal to the changed side then method should
# throw an exception
# If as a result of the change side will be less than or equal to 0 then method should raise a different exception
# When a side is modified by some value all other sides need to be modified by the fraction of the change to maintain
# the same triangle angles. For example, if A increase by +1 then B = ((A+1)/A)*B and C = ((A+1)/A)*C

from math import cos, acos

#
# class Triangle():
#     pass  # <your code here>


# 10P
# Create an object from your class with default constructor values and modify angle AB by +30 degrees and side A by +1.5

# <your code here>
from math import cos, acos, radians, pi, sin

class Triangle():

    def __init__(self, a1 = 60, b1 = 60, c1 = 60, ab1 = 1, bc1 = 1, ca1 = 1):
        self.AB = c1 #unghi
        self.BC = a1 #unghi
        self.CA = b1 #unghi
        self.C = ab1 #latura
        self.A = bc1 #latura
        self.B = ca1 #latura


    def modify_angle(self, angle: str, degrees:int):
        self.angle = angle

        if self.angle == 'AB':
            self.AB = self.AB + degrees
            if (self.AB <= 0) or (self.AB >= 180):
                raise Exception("Not OK")
            else:
                self.C = (self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(90 * (pi /180)))**(1/2)
                self.BC = (180 / pi) * acos((self.B**2 + self.C**2 - self.A**2) / (2 * self.B * self.C))
                self.CA = 90 - self.BC

        elif self.angle == 'BC':
            self.BC = self.BC + degrees
            if (self.BC <= 0) or (self.BC >= 180):
                raise Exception("Not OK")
            else:
                self.A = (self.B ** 2 + self.C ** 2 - 2 * self.B * self.C * cos(90 * (pi /180)))**(1/2)
                self.CA = (180 / pi) * acos((self.C**2 + self.A**2 - self.B**2) / (2 * self.C * self.A))
                self.AB = 90 - self.CA

        elif self.angle == 'CA':
            self.CA = self.CA + degrees
            if (self.CA <= 0) or (self.CA >= 180):
                raise Exception("Not OK")
            else:
                self.B = (self.C ** 2 + self.A ** 2 - 2 * self.C * self.A * cos(90 * (pi /180)))**(1/2)
                self.AB = (180 / pi) * acos((self.A**2 + self.B**2 - self.C**2) / (2 * self.A * self.B))
                self.BC = 90 - self.AB

        else:
            return print("Please use the following format: AB, BC or CA")
        return print(f"Sides: {self.A, self.B, self.C}, angles: {self.BC, self.CA, self.AB}")

    def modify_side(self, side, meters):
        self.side = side

        if self.side == 'A':
            self.A = self.A + meters
            self.B = ((self.A + 1) / self.A) * self.B
            self.C = ((self.A + 1) / self.A) * self.C
            if (self.A + self.B < self.C) or (self.B + self.C < self.A) or (self.C + self.A < self.B):
                raise Exception("The length is not OK")
            elif (self.A <= 0) or (self.B <= 0) or (self.C <= 0):
                raise Exception("The lenght of the side should be greater than zero")

        elif self.side == 'B':
            self.B = self.B + meters
            self.C = ((self.B + 1) / self.B) * self.C
            self.A = ((self.B + 1) / self.B) * self.A
            if (self.B + self.C < self.A) or (self.C + self.A < self.B) or (self.A + self.B < self.C):
                raise Exception("The length is not OK")
            elif (self.B <= 0) or (self.C <= 0) or (self.A <= 0):
                raise Exception("The lenght of the side should be greater than zero")

        elif self.side == 'C':
            self.C = self.C + meters
            self.A = ((self.C + 1) / self.C) * self.A
            self.B = ((self.C + 1) / self.C) * self.B
            if (self.B + self.C < self.A) or (self.C + self.A < self.B) or (self.A + self.B < self.C):
                raise Exception("The length is not OK")
            elif (self.C <= 0) or (self.A <= 0) or (self.C <= 0):
                raise Exception("The lenght of the side should be greater than zero")

        return print("the newest lenght sides of the triangle are:", self.A, self.B, self.C)



triangle1 = Triangle(60, 60, 60, 1, 1, 1) # am creeat un obiect care a luat self.AB = 60;
triangle1.modify_angle("AB", 30)
triangle1.modify_side("A", 0.5)
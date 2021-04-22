# Law of Sines Calculator
# James Taddei
# 4/22/21

import math

class triangle:
    def __init__(self, a, b, c, A, B, C):
        # Sides (lowercase) and angles (caps) of a triangle
        self.a = a
        self.b = b
        self.c = c
        self.A = A
        self.B = B
        self.C = C
        
    # Returns whether or not there are more sides than angles and which attributes are filled
    def attr_filled(self):
        """
        Takes in a triangle object and returns a tuple with whether there are more sides or angles
        and a list of which attributes are filled
        """
        
        # Creates a list of which attributes are filled (true) and which aren't (false)
        attrList = [self.a, self.b, self.c, self.A, self.B, self.C]
        attrFilled = []
        for i in attrList:
            if (i == i): # Since unfilled attributes are NaN and NaN != NaN, this finds which segments are NaN (or unfilled)
                attrFilled.append(True)
            else:
                attrFilled.append(False)

        # Finds how many sides and how many angles have been inputted
        sidesIn = int(self.a == self.a) + int(self.b == self.b) + int(self.c == self.c)
        anglesIn = int(self.A == self.A) + int(self.B == self.B) + int(self.C == self.C)
        
        # Returns an error message if <3 measures inputted, and if not, whether or not there are more sides than angles and the list of filled attributes
        if (sidesIn + anglesIn > 3):
            return (True, attrFilled)
        elif (sidesIn > anglesIn):
            return (True, attrFilled)
        elif (sidesIn < anglesIn):
            return (False, attrFilled)
        else:
            return ("Error, only 3 measures (including at least one side) should have been entered.")

def main():
    """
    Takes user inputs of known sides and angles and solves a triangle with the Law of Sines
    """
    
    print("This is a program created by James Taddei which solves triangles that you would solve via the Law of Sines (LoS).")
    print("Enter the measure of an angle/side if you know it, otherwise leave it blank.\n")
    
    a = raw_input("Length of side a = ")
    b = raw_input("Length of side b = ")
    c = raw_input("Length of side c = ")
    A = raw_input("Measure of angle A = ")
    B = raw_input("Measure of angle B = ")
    C = raw_input("Measure of angle C = ")
    
    sidesPlusAngles = [a, b, c, A, B, C]
    addToTri1 = []
    
    # Creates a list of all of the starting values for tri1, filling in unknowns with NaN
    for i in range(len(sidesPlusAngles)):
        if sidesPlusAngles[i] != "": # Checks that values aren't blank
            addToTri1.append(float(sidesPlusAngles[i]))
        else:
            addToTri1.append(float("NaN"))
    
    tri1 = triangle(addToTri1[0], addToTri1[1], addToTri1[2], addToTri1[3], addToTri1[4], addToTri1[5])
    attrInfo = tri1.attr_filled()
    
    # Confirms that enough measures have been entered before moving on
    if (len(attrInfo) != 2):
        print(attrInfo)
        return (main())
        
    moreSidesThanAngles, attrFilled = attrInfo[0], attrInfo[1]
        
    # The program solves the problem 2 different ways based on if there are more known sides or angless
    if moreSidesThanAngles:
        ans = solve_with_more_sides(attrFilled, tri1)
    else:
        ans = solve_with_more_angles(attrFilled, tri1)

    return (final_print(ans))
    
def sine_value_and_given_angle(attrFilled, tri):
    """
    Takes in a list of a triangle's filled attributes and the triangle object and finds
    the sine value and a given angle of the triangle
    """
    
    # Finds the sine value of the triangle (x / sinX)
    if (attrFilled[0] and attrFilled[3]):
        sineValue = tri.a / math.sin(math.radians(tri.A))
        givenAngle = tri.A
    elif (attrFilled[1] and attrFilled[4]):
        sineValue = tri.b / math.sin(math.radians(tri.B))
        givenAngle = tri.B
    else:
        sineValue = tri.c / math.sin(math.radians(tri.C))
        givenAngle = tri.C
        
    return (sineValue, givenAngle)
    
def solve_with_more_sides(attrFilled, tri1):
    """
    Takes in a list of filled attributes in a triangle object and the triangle object
    (which must have at least 2 sides and 1 angle). Returns a 3 item tuple if there's 
    no valid triangle, a 2 item tuple with 2 triangle objects if there are 2 valid
    triangles, and a 1 item tuple with the 1 valid triangle object if there's 1 valid triangle
    """
    
    # Finds the sine value of the triangle (x / sinX)
    sineValue, givenAngle = sine_value_and_given_angle(attrFilled, tri1)
        
    tri2 = triangle(tri1.a, tri1.b, tri1.c, tri1.A, tri1.B, tri1.C) # Creates tri2 before new info is added
        
    # Finds the value of a second angle
    if (attrFilled[0] and not(attrFilled[3])):
        if (tri1.a / sineValue > 1 or tri1.a / sineValue < -1):
            return ("Print", "No", "Tri")
        tri1.A = math.degrees(math.asin(tri1.a / sineValue))
        findSuppOf = tri1.A
    elif (attrFilled[1] and not(attrFilled[4])):
        if (tri1.b / sineValue > 1 or tri1.b / sineValue < -1):
            return ("Print", "No", "Tri")
        tri1.B = math.degrees(math.asin(tri1.b / sineValue))
        findSuppOf = tri1.B
    else:
        if (tri1.c / sineValue > 1 or tri1.c / sineValue < -1):
            return ("Print", "No", "Tri")
        tri1.C = math.degrees(math.asin(tri1.c / sineValue))
        findSuppOf = tri1.C
        
    # Checks for a second tri and solves if necessary
    twoTriResults = two_triangles(findSuppOf, givenAngle, sineValue, attrFilled, tri2)
    if (len(twoTriResults) == 2):
        tri2 = twoTriResults[1]
        twoTri = True
    else:
        twoTri = False
        
    # Find the final angle of tri1
    attrInfo = tri1.attr_filled()
    if (attrInfo[1][3] == False):
        tri1.A = 180 - findSuppOf - givenAngle
    elif (attrInfo[1][4] == False):
        tri1.B = 180 - findSuppOf - givenAngle
    else:
        tri1.C = 180 - findSuppOf - givenAngle
        
    # Find the final side of tri1
    if not(attrInfo[1][0]):
        tri1.a = sineValue * math.sin(math.radians(tri1.A))
    elif not(attrInfo[1][1]):
        tri1.b = sineValue * math.sin(math.radians(tri1.B))
    else:
        tri1.c = sineValue * math.sin(math.radians(tri1.C))
    
    if (tri1.a < 0 or tri1.b < 0 or tri1.c < 0): # Returns that there are no valid triangles if a side has negative length
        return ("Print", "No", "Triangles")    
    elif twoTri:
        return (tri1, tri2)
    else:
        return (tri1,)
    
def solve_with_more_angles(attrFilled, tri1):
    """
    Takes in a list of filled attributes in a triangle object and the triangle object
    (which must have at least 2 angles and 1 side). Returns a 3 item tuple if there's 
    no valid triangle and a 1 item tuple with the 1 valid triangle object if there's 1 valid triangle
    """
    
    # Finds the sine value of the triangle (x / sinX)
    sineValue, _ = sine_value_and_given_angle(attrFilled, tri1)

    # Finds the value of the last angle
    if (attrFilled[3] and attrFilled[4]):
        tri1.C = 180 - (tri1.A + tri1.B)
    elif (attrFilled[3] and attrFilled[5]):
        tri1.B = 180 - (tri1.A + tri1.C)
    else:
        tri1.A = 180 - (tri1.B + tri1.C)
        
    # Finds the value of the second side
    if (attrFilled[0] and attrFilled[1]):
        tri1.c = sineValue * math.sin(math.radians(tri1.C))
    elif (attrFilled[0] and attrFilled[2]):
        tri1.b = sineValue * math.sin(math.radians(tri1.B))
    else:
        tri1.a = sineValue * math.sin(math.radians(tri1.A))
        
    # Finds the value of the last side
    _, attrFilled = tri1.attr_filled()
    if (not(attrFilled[0])):
        tri1.a = sineValue * math.sin(math.radians(tri1.A))
    elif (not(attrFilled[1])):
        tri1.b = sineValue * math.sin(math.radians(tri1.B))
    else:
        tri1.c = sineValue * math.sin(math.radians(tri1.C))
        
    if (tri1.a < 0 or tri1.b < 0 or tri1.c < 0): # Returns that there are no valid triangles if a side has negative length
        return ("Print", "No", "Triangles")    
    else:
        return (tri1,)
    
def two_triangles(suppOf, givenAngle, sineValue, attrFilled, tri2):
    """
    Takes in a angle to find the supplemental of, a given angle, the 
    triangle's sine vlaue, a list of filled objects in the triangle, and
    the triangle object itself. Returns a tuple just holding false if
    there's only 1 valid triangle and a 2 item tuple holding true and
    the second triangle object if there's 2 valid triangles.
    """
    
    supp = 180 - suppOf
    if (180 < supp + givenAngle): # If there's one tri, return false
        return (False,)
    else: # Return true and the second triangle
        return (True, solve_second_tri(supp, sineValue, givenAngle, attrFilled, tri2))
        
def solve_second_tri(supp, sineValue, givenAngle, attrFilled, tri2):
    """
    Solves the second triangle and returns it as an object.
    """
    
    # Find the second angle of tri2
    if ((attrFilled[0] == True) and (attrFilled[3] == False)):
        tri2.A = supp
    elif ((attrFilled[1] == True) and (attrFilled[4] == False)):
        tri2.B = supp
    else:
        tri2.C = supp
        
    # Find the final angle of tri2
    attrInfoTwo = tri2.attr_filled()
    if (attrInfoTwo[1][3] == False):
        tri2.A = 180 - supp - givenAngle
    elif (attrInfoTwo[1][4] == False):
        tri2.B = 180 - supp - givenAngle
    else:
        tri2.C = 180 - supp - givenAngle
        
    # Find the final side of tri2
    if not(attrInfoTwo[1][0]):
        tri2.a = sineValue * math.sin(math.radians(tri2.A))
    elif not(attrInfoTwo[1][1]):
        tri2.b = sineValue * math.sin(math.radians(tri2.B))
    else:
        tri2.c = sineValue * math.sin(math.radians(tri2.C))
    
    return tri2
    
def final_print(ans):
    """
    Returns the 1 or 2 valid triangles if there are any, a message saying
    that the user must use the law of cosines if there are any unfilled
    attributes, or a message saying that there is no valid triangle triangles
    if the entered tuple doesn't have enough values.
    """
    
    if (len(ans) > 2): # Checks if a valid triangle can be made (no valid tri if len(ans) = 3)
        return ("\nThis is not a valid triangle.")
    elif (len(ans) == 2): # Prints out the 2 valid triangles
        tri1, tri2 = ans[0], ans[1]
        
        attrInfo = tri1.attr_filled()
        # Checks for NaN to make sure that everything is filled in (if not, the user needs to use the law of cosines first)
        for i in attrInfo[1]:
            if not(i):
                return ("\nYou must use the law of cosines first.")
        
        final = "Triangle 1: a = " + str(tri1.a) + ", b = " + str(tri1.b) + ", c = " + str(tri1.c) + ", A = " + str(tri1.A) + ", B = " + str(tri1.B) + ", C = " + str(tri1.C)
        final += "\nTriangle 2: a = " + str(tri2.a) + ", b = " + str(tri2.b) + ", c = " + str(tri2.c) + ", A = " + str(tri2.A) + ", B = " + str(tri2.B) + ", C = " + str(tri2.C)
        return (final)
    else: # Returns the 1 valid triangle
        tri1 = ans[0]
        return ("Triangle: a = " + str(tri1.a) + ", b = " + str(tri1.b) + ", c = " + str(tri1.c) + ", A = " + str(tri1.A) + ", B = " + str(tri1.B) + ", C = " + str(tri1.C))
    
print(main())
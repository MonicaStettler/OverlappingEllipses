# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:02:26 2018

@author: Monica
"""
#MONICA STETTLER - DSC430 - 11-5-18

#ASSIGNMENT 4 - AREA OVERLAP OF ELLIPSES
#PROBLEM 1 - CREATING ELLIPSE CLASS (AND POINT CLASS)

#“I have not given or received any unauthorized assistance on this assignment.” 
#*********************************************************************************

import math

class Ellipse:
    'creates and defines an Ellipse'
    
    def __init__(self, x1=0, y1=0, x2=0, y2=0, w=1):
        self.x1 = x1
        if type(self.x1) ==str:
                raise TypeError("Must be integer or float. Please try again")
        self.y1 = y1
        if type(self.y1) ==str:
                raise TypeError("Must be integer or float. Please try again")

        self.x2 = x2
        if type(self.x2) ==str:
                raise TypeError("Must be integer or float. Please try again")

        self.y2 = y2
        if type(self.y2) ==str:
                raise TypeError("Must be integer or float. Please try again")

        self.w = w
        if self.w < max ( abs(self.x1 - self.x2), abs(self.y1 - self.y2) ):
                raise ValueError("Width must be greater than the largest distance on x or y axis.")
                
        self.F1 = Point(self.x1,self.y1)
        self.F2 = Point(self.x2,self.y2)
     
    def setF1(self, x1,y1):
        self.F1 = Point(self.x1,self.y1)
        
    def setF2(self, x2,y2):
        self.F2 = Point(self.x2,self.y2)
        
    def setW(self, w):
        self.w = w
        
    def getF1(self):
        return self.F1
    
    def getF2(self):
        return self.F2
    
    def getW(self):
        return self.w
    
    def getPair(self):
        return (self.F1, self.F2)
    
    def getSemiMajor(self):
        'calculates and returns the lenght of the semi major axis'
        self.semiMajor = self.F1.distance(self.F2)*.5 + (self.w - self.F1.distance(self.F2))*.5 #half the d between F1F2 plus half w-d
        return self.semiMajor
    
    def getSemiMinor(self):
        self.semiMinor = ( (0.5*self.w)**2 - ( (0.5*self.F1.distance(self.F2) )**2) )**0.5 #using geometry to solve for semiminor
        return self.semiMinor

    def getArea(self):
        'calculate the area of the Ellipse'
        semiMajor = self.getSemiMajor()
        semiMinor = self.getSemiMinor()
         
        return math.pi*semiMajor*semiMinor
     
    def getCircum(self):
        'circumference of the Ellipse using Ramanujan approximation formula'
        semiMajor = self.getSemiMajor()
        semiMinor = self.getSemiMinor()
         
        return math.pi*( 3*(semiMajor + semiMinor) - ( (3*semiMajor + semiMinor) *(semiMajor + 3*semiMinor) )**0.5)
     
    def isBoundary(self, otherXcoord, otherYcoord):    
        'determines is a given point is on the edge of the ellipse'
 
        otherPoint = Point(otherXcoord,otherYcoord)
        
        if self.F1.distance(otherPoint) + self.F2.distance(otherPoint) == self.w: #uses definition to determine if on boundary    
            return True
        else:
            return False
    
    def pointInside(self, other):
        'determines whether a given point is inside the boundary of the ellipse'
        
        if self.F1.distance(other) + self.F2.distance(other) < self.w: #if the distance to the point is less than to a point on the boundary, then it is inside
         
            return True
        
    def __repr__(self):
        'canonical string representation Point(x, y)'
        return 'Foci: ({}, {}), Width: {}.'.format(self.F1, self.F2, self.w)


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord= 0): 
        'initialize coordinates to (xcoord, ycoord)'
        self.x = xcoord
        if type(self.x) ==str:
                raise TypeError("Must be integer or float. Please try again")

        self.y = ycoord
        if type(self.y) ==str:
                raise TypeError("Must be integer or float. Please try again")        
        
        self.p = (xcoord,ycoord)

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord
        
    def setXY(self, xcoor, ycoord):
        self.p = (self.x, self.y)
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y     

    def getPair(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def distance(self, point2):
        'calculates the distance between 2 cartesian points'
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = (xdiff**2 + ydiff**2)**0.5 #using euclidean distance calculation
        return dist
    
    def __repr__(self):
        'canonical string representation Point(x, y)'
        return 'Point({}, {})'.format(self.x, self.y)
    
print('')
print('**********INSTRUCTIONS FOR TESTING SECTION: ************************')
print('Uncomment each section below to run it, the put back into #.')
print('When finished, return all code into comments(#)')    
print('')  
      
# =============================================================================
# print('TESTING CLASSES WITH AND WITHOUT CONSTRUCTORS ***********************')
# print('')
# print("Creating an Ellipse using constructors 'Ellipse(1,1,2,2,4)' :")
# e1 = Ellipse(1,1,2,2,4)
# print("Result of initializing an Ellipse with constructors: ", e1)
# print('')
# print("Creating an Ellipse without using constructors 'Ellipse()' :")
# e2 = Ellipse()
# print("Result of initializing an Ellipse without constructors: ", e2)
# 
# print('')
# print("Creating a Point using constructors 'Point(5,9)' :")
# p1 = Point(5,9)
# print("Result of initializing a Point with constructors: ", p1)
# print('')
# print("Creating a Point without using constructors 'Point()' :")
# p2 = Point()
# print("Result of initializing an Ellipse without constructors: ", p2)
# 
# print('')
# print("TESTING VALID INPUTS OF ELLIPSE ***********************************************")
# print('')
# print("Creating an Ellipse using string inputs 'Ellipse(cat,20,20,20,50) - uncomment to run test' :")
# e3 = Ellipse('cat',20,20,20,50) #UNCOMMENT TO RUN TEST
# print("Result of initializing an Ellipse with bad constructors: ", e3) #UNCOMMENT TO RUN TEST
# print('')
# print("Creating an Ellipse with bad inputs - width too small 'Ellipse(-5,10,2,-5,10)' :")
# e4 = Ellipse(-5,10,2,-5,10) #COMMENT THIS TO RUN TESTS BELOW
# print("Result of initializing an Ellipse with bad width: ", e4)
# 
# print('')
# print("TESTING VALID INPUTS OF POINT ***********************************************")
# print('')
# print("Creating a Poin using string inputs 'Point('cat',2) - uncomment to run test' :")
# p1 = Point('cat',2) #UNCOMMENT TO RUN TEST
# print("Result of initializing an Ellipse with bad constructors: ", p1) #UNCOMMENT TO RUN TEST
# print("Creating a Poin using string inputs 'Point(2,'cat') - uncomment to run test' :")
# p2 = Point(2,'cat') #UNCOMMENT TO RUN TEST
# print("Result of initializing an Ellipse with bad constructors: ", p2) #UNCOMMENT TO RUN TEST
# =============================================================================


print('******TESTING of CLASS METHODS IS IN A4P4 UNIT TESTING FILE***********************')
#TESTING OF ELLIPSE CLASS AREA AND CIRCUMFERENCE METHODS ARE IN A4P4
#TESTING OF POINT CLASS DISTANCE METHOD IS IN A4P4
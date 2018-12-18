# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 19:16:37 2018

@author: Monica
"""
#MONICA STETTLER - DSC430 - 11-5-18

#ASSIGNMENT 4 - AREA OVERLAP OF ELLIPSES
#PROBLEM 3 - IMPLEMENTATION OF FULL PROGRAM: RUNNING MONTE CARLO SIM TO CALC AREA OF OVERLAP OF 2 ELLIPSES

#“I have not given or received any unauthorized assistance on this assignment.” 
#******************************************************************************

from classEllipse import Ellipse
from classEllipse import Point
import random

def main(): 
    instructions()
    e1, e2 = get2Ellipses()
    x1,y1,x2,y2,x3,y3,x4,y4 = computeBox(e1,e2)
    area = simulation(e1,e2)
    printResults(area)

def instructions():
    print('')
    print("This program calculates the overlap area of 2 ellipses -if there is any.")
    print("To begin, you will be prompted to created 2 ellipses.")
    print("When promted, type 'Ellipse(num1,num2,num3,num4,num5)' providing your own numbers.")
    print("The numbers correspond to foucs1(num1,num2), focus2(num3,num4) and the width of the Ellipse.")
    print("The width has to be longer than distance between the 2 foci.")
   
    
def get2Ellipses():
    'creates and returns 2 Ellipses'
        
    ellipseList = []
    
    ellipse1 = input('Use the Elipse class and your 5 numbers for ellipse1 here: ')
    
    ellipseList.append(ellipse1)
    
    ellipse2 = input('Use the Ellipse class and your 5 numbers for ellipse2 here: ')
    
    ellipseList.append(ellipse2)
    
    return ellipse1, ellipse2

def simulation(ellipse1, ellipse2, bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy):
    'this calculates the area of the box, takes the percentage of points in overlap and calculates the area of overlap'
    
    #get each coordinate point of the box that surrounds the 2 ellipses    
    #bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy = computeBox(ellipse1, ellipse2)
    
    #create the 4 points of the box
    LR = Point(bLRx, bLRy)
    UR = Point(bURx, bURy)
    LL = Point(bLLx, bLLy)
    UL = Point(bULx, bULy)
    
    #calculate the lenght of the sides
    lenSide1 = LR.distance(UR)
    lenSide2 = LR.distance(LL)
    
    areaSquare = lenSide1*lenSide2  #calculate the area of the square surround the 2 ellipses
    
    #run the Monte Carlo simulation and get result
    percOverlap = simulateMany(ellipse1,ellipse2,bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy)
    
    areaOverlap = areaSquare*percOverlap 
    
    return areaOverlap #returns areaOverlap

def computeBox(ellipse1, ellipse2):
    'computes size of box big enough to surround both ellipses and returns the coordinates of the 4 corners'

    w1 = ellipse1.getW()
    w2 = ellipse2.getW()    
    #w1 = ellipse1.getW()
    #w2 = ellipse2.getW()
    
    if  w1 > w2 : # I am using 1/2width as my buffer and I want the longer width from the 2 ellipses
        wbuff = w1
    else:
        wbuff = w2
   
    #box coordinates for lower right corner of box
    bLRx = max(ellipse1.x1,ellipse1.x2,ellipse2.x1, ellipse2.x2) + 0.5*wbuff
    bLRy = min(ellipse1.y1,ellipse1.y2,ellipse2.y1, ellipse2.y2) - 0.5*wbuff
    
    #box coordinates for upper right corner of box
    bURx = max(ellipse1.x1,ellipse1.x2,ellipse2.x1, ellipse2.x2) + 0.5*wbuff
    bURy = max(ellipse1.y1,ellipse1.y2,ellipse2.y1, ellipse2.y2) + 0.5*wbuff
    
    #box coordinates for lower left corner of box
    bLLx = min(ellipse1.x1,ellipse1.x2,ellipse2.x1, ellipse2.x2) - 0.5*wbuff
    bLLy = min(ellipse1.y1,ellipse1.y2,ellipse2.y1, ellipse2.y2) - 0.5*wbuff
    
    #box coordinate for lower right corner of box
    bULx = min(ellipse1.x1,ellipse1.x2,ellipse2.x1, ellipse2.x2) - 0.5*wbuff
    bULy = max(ellipse1.y1,ellipse1.y2,ellipse2.y1, ellipse2.y2) + 0.5*wbuff
           
    return bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy  #coordinates for 4 corners of bx

def simulateMany(ellipse1, ellipse2, bLRx, bLRy, bURx, bURy, bLLx, bLLy, bULx, bULy):
    'uses for loop to run simulation of random points 10,000 times, counts successful results, calculates and returns percentage successful'
    
    count = 0
    n = 10000
    
    startX = int(min(bLRx, bURx, bLLx, bULx))
    endX = int(max(bLRx, bURx, bLLx, bULx))
    startY = int(min(bLRy, bURy, bLLy, bULy))
    endY = int(max(bLRy, bURy, bLLy, bULy))
    
    for i in range(0, n):
        x = random.randint(startX, endX)
        y = random.randint(startY, endY)
        
        point = Point(x,y)
        
        if simulateOnce(ellipse1, ellipse2, point) == True:
            count += 1   
            
    print("Count is {}, number of random points is {}".format(count,n))        
    return count/n

def simulateOnce(ellipse1, ellipse2, point):
    'runs one simulation at a time, if point is in both ellipse 1 and ellipse 2, then it returns True'
    
    if ellipse1.pointInside(point) == True and ellipse2.pointInside(point) == True:
        return True

def printResults(areaOverlap):
    'prints results of simlulation - total area of overlap of the 2 ellipses'

    print('The area of overlap is: ', areaOverlap)    

main()
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:07:34 2018

@author: Monica
"""
#MONICA STETTLER - DSC430 - 11-5-18

#ASSIGNMENT 4 - AREA OVERLAP OF ELLIPSES
#PROBLEM 4 - UNIT TESTING OF ALL CRITICAL FUNCTIONS

#“I have not given or received any unauthorized assistance on this assignment.” 
# =============================================================================
# A.	Print the name of the function.
# B.	Print the doctstring of the function.
# C.	Print the rationale for the test (e.g. “Testing when a point falls within an Ellipse.”)
# D.	Print the specific input used to evaluate that rationale.
# E.	Print the result.
# F.	Repeat C – E until all relevant cases are tested for that function.
# =============================================================================

import classEllipse
from A4P3 import computeBox
from A4P3 import simulateOnce
from A4P3 import simulateMany
from A4P3 import simulation


def main():
    print('')
    print('I recommend running this test a few times and comparing results.')
    print('')
    TestPointDistance()
    TestGetSemiMajor()
    TestGetSemiMinor()
    TestgetArea()
    TestgetCircum() 
    TestIsBoundary()    #didn't use this in program, but left it in
    TestPointInside()  
    TestComputeBox()
    TestSimulateOnce()   
    TestSimulateMany()
    TestSimulation()

def TestPointDistance():
    'run unit testing on point class distance method'
    
    print("FUNCTION NAME: 'distance()' method from class Point")
    print("")
    help(classEllipse.Point.distance)
    print("")
    print("Goal is to test that distance calculations are correct.")
    print('')
    
    #arbitrary points
    point1 = classEllipse.Point(1,4)
    point2 = classEllipse.Point(2,10)
    point3 = classEllipse.Point(-2,6)
    point4 = classEllipse.Point(0,0)
    point5 = classEllipse.Point(-2,-20)
    point6 = classEllipse.Point(-4,-1)
    
    print("The inputs are: ", point1, point2, point3, point4, point5, point6)
    print('')
    
    d = point1.distance(point2) #run the function
    
    #results
    print("The result for distance between {} and {} is {}. Actual is {}".format(point1,point2,d,4.49999))
    print("")
    d = point3.distance(point4)
    print("The result for distance between {} and {} is {}. Actual is {}".format(point3,point4,d,6.324555))
    d = point5.distance(point6)
    print("")
    print("The result for distance between {} and {} is {}. Actual is {}".format(point5,point6,d,19.104973))
    print("*******************************")
    print('')
    
def TestGetSemiMajor():
    'run unit testing on Ellipse class method that calculates the length of the semimajor axis'
    
    print("FUNCTION NAME: 'getSemiMajor()' method from class Ellipse.")
    print("")
    help(classEllipse.Ellipse.getSemiMajor)
    print("")
    print("Goal is to test that we got the semi major axis lenght correct.")
    print("")
    
    #arbitrary Ellipses
    e1 = classEllipse.Ellipse(1,4,5,6,9)
    e2 = classEllipse.Ellipse(2,-4,5,10,15)
    #e3 = classEllipse.Ellipse(-5,10,2,-5,10) #this one should give error message YOU NEED TO UNCOMMENT THIS TO SEE
    e4 = classEllipse.Ellipse(3,9,-4,6,22)
    
    print('')
    print("The inputs are: ", e1,e2,e4)
    print('')
    
    mj1 = e1.getSemiMajor()
    print("The function result for the length of the major axis is {}. Actual is {}.".format(mj1,6.082763))
    print("")
    mj2 = e2.getSemiMajor()
    print("The function result for the length of the major axis is {}. Actual is {}.".format(mj2,7.49999))
    print("")
    #mj3 = e3.getSemiMajor()
    #print("The function result for the length of the major axis is {}. Actual is {}.".format(mj3,00000000))
    print("")
    mj4 = e4.getSemiMajor()
    print("The function result for the length of the major axis is {}. Actual is {}.".format(mj4,7.50000))
    print("**************************************")
    print('')
    
def TestGetSemiMinor():
    'run unit testing on Ellipse class method that calculates the length of the semiminor axis'
    
    print("FUNCTION NAME: 'getSemiMinor() method from class Ellipse.")
    print("")
    help(classEllipse.Ellipse.getSemiMinor)
    print("")
    print("Goal is to test that we got the semi minor axis lenght correct.")
    print("")
    
    e1 = classEllipse.Ellipse(1,4,5,6,9)
    e2 = classEllipse.Ellipse(2,-4,5,10,15)
    #e3 = classEllipse.Ellipse(-5,10,2,-5,10) #this one should give error message, YOU MUST UNCOMMENT TO SEE/TEST
    e4 = classEllipse.Ellipse(3,9,-4,6,22)
    
    print('')
    print("The inputs are: ", e1,e2,e4)
    print('')

    mn1 = e1.getSemiMinor()
    print("The function result for the length of the minor axis is {}. Actual is {}.".format(mn1,3.905137))
    print("")
    mn2 = e2.getSemiMinor()
    print("The function result for the length of the minor axis is {}. Actual is {}.".format(mn2,2.236609))
    print("")
    #mn3 = e3.getSemiMajor()
    #print("The function result for the length of the minor axis is {}. Actual is {}".format(mn3,0000000))
    print("")
    mn4 = e4.getSemiMinor()
    print("The function result for the length of the minor axis is {}. Actual is {}.".format(mn4,10.31988))    
    print("********************************")
    print('')
    
def TestgetArea():
    'run unit testing on Ellipse class method that calculates the area of an ellipse'
    
    print("FUNCTION NAME: 'getArea()' method from class Ellipse.")
    print("")
    help(classEllipse.Ellipse.getArea)
    print("")
    print("Goal is to test that we got the area calculation correct.")
    print("")
    
    #using same Ellipses 
    e1 = classEllipse.Ellipse(1,4,5,6,9)
    e2 = classEllipse.Ellipse(2,-4,5,10,15)
    #e3 = classEllipse.Ellipse(-5,10,2,-5,10) #bad ellipse
    e4 = classEllipse.Ellipse(3,9,-4,6,22)
    
    print('')
    print("The inputs are: ", e1,e2,e4)
    print('')
    
    area1 = e1.getArea()
    print("The function result for the area of the ellipse is {}. Actual is {}.".format(area1,55.21))
    print("")
    area2 = e2.getArea()
    print("The function result for the area of the ellipse is {}. Actual is {}.".format(area2,52.69))
    print("")

    print("")
    area4 = e4.getArea()
    print("The function result for the area of the ellipse is {}. Actual is {}.".format(area4,356.63))    
    print("**********************************************")
    print('')
    
def TestgetCircum():
    'run unit testing on Ellipse class method that calculates the circumference of an ellipse'
    
    print("FUNCTION NAME: 'getCircum()' method from class Ellipse.")
    print("")
    help(classEllipse.Ellipse.getCircum)
    print("")
    print("Goal is to test that we got the circumference estimate correct.")
    print("")
    
    e1 = classEllipse.Ellipse(1,4,5,6,9)
    e2 = classEllipse.Ellipse(2,-4,5,10,15)
    #e3 = classEllipse.Ellipse(-5,10,2,-5,10)
    e4 = classEllipse.Ellipse(3,9,-4,6,22)
    
    print('')
    print("The inputs are: ", e1,e2,e4)
    print('')
    
    circum1 = e1.getCircum()
    print("The function result for the circumference of the ellipse is {}. Compare to estimate: {}.".format(circum1,26.44))
    print("")
    circum2 = e2.getCircum()
    print("The function result for the circumference of the ellipse is {}. Compare to estimate: {}.".format(circum2,32.87))
    print("")
 
    print("")
    circum4 = e4.getCircum()
    print("The function result for the circumference of the ellipse is {}. Compare to estimate: {}.".format(circum4,67.01))    
    print("*********************************************")
    print('')
    
def TestIsBoundary():
    'run unit testing on Ellipse class method that calculates whether a point is on the boundary'
    
    print("FUNCTION NAME: 'isBoundary()' method from class Ellipse.")
    print("")
    help(classEllipse.Ellipse.isBoundary)
    print("")
    print("Goal is to test whether a point is on the boundary of an ellipse.")
    print("")
    
    e1 = classEllipse.Ellipse(2,0,4,0,4)
    p1 = classEllipse.Point(1,0) #on boundary
    p2 = classEllipse.Point(5,0) #on boundary
    p3 = classEllipse.Point(5,2) # NOT on boundary
    p4 = classEllipse.Point(3,0) #NOT on boundary
    
    print('')
    print("The inputs are: ", e1,p1,p2,p3,p4)
    print('')
    
    b1 = e1.isBoundary(1,0)
    print("The result should be 'True'. The actual resulat is {}.".format(b1))
    print("")
    
    b2 = e1.isBoundary(5,0)
    print("The result should be 'True'. The actual resulat is {}.".format(b2))
    print("")
    
    b3 = e1.isBoundary(5,2)
    print("The result should be 'False'. The actual resulat is {}.".format(b3))
    print("")
    
    b4 = e1.isBoundary(3,0)
    print("The result should be 'False'. The actual resulat is {}.".format(b4))
    print("")
    print("********************************")
    print('')
    
def TestPointInside():
    'run unit testing on Ellipse class method that calculates whether a point is inside an ellipse'
    
    print("FUNCTION NAME: 'pointInside()' method from class Ellipse.")
    print("")
    help(classEllipse.Ellipse.pointInside)
    print("")
    print("Goal is to test whether a point is inside an ellipse.")
    print("")
    
    e1 = classEllipse.Ellipse(2,0,4,0,4)
    p1 = classEllipse.Point(1,0) #on boundary
    p2 = classEllipse.Point(5,0) #on boundary
    p3 = classEllipse.Point(5,2) # OUTSIDE
    p4 = classEllipse.Point(3,0) #INSIDE
    
    print('')
    print("The inputs are: ", e1,p1,p2,p3,p4)
    print('')
    
    b1 = e1.pointInside(p1)
    print("The result should be 'None'. The actual result is {}.".format(b1))
    print("")
    
    b2 = e1.pointInside(p2)
    print("The result should be 'None'. The actual result is {}.".format(b2))
    print("")
    
    b3 = e1.pointInside(p3)
    print("The result should be 'None'. The actual result is {}.".format(b3))
    print("")
    
    b4 = e1.pointInside(p4)
    print("The result should be 'True'. The actual result is {}.".format(b4))
    print("")
    print("********************************")
    print('')
    
def TestComputeBox():
    'run unit testing on function that creates a box that can enclose 2 ellipses'
    
    print("FUNCTION NAME: 'computeBox()' function from main program.")
    print("")
    help(computeBox)
    print("")
    print("Goal is to test that the box completely surrounds the 2 ellipses.")
    print("")

    #e1 fits inside e2
    e1 = classEllipse.Ellipse(1,4,5,6,9)
    e2 = classEllipse.Ellipse(2,-4,5,10,15)
    
    print('')
    print("The inputs are: ", e1,e2)
    print('')
    a,b,c,d,e,f,g,h, = computeBox(e1,e2)
    
    print("Test vs actual values. Actual values in () : {} (12.5), {} (-11.5), {} (12.5), {} (17.5), {} (-6.5), {} (-11.5), {} (-6.5), {} (17.5). ".format(a,b,c,d,e,f,g,h))
    
    #No overlap of ellipses
    e3 = classEllipse.Ellipse(-2,-2,-4,-4,5)
    e4 = classEllipse.Ellipse(2,-2,4,-4,5)
    
    print('')
    print("The inputs are: ", e3,e4)
    print('')
    a,b,c,d,e,f,g,h, = computeBox(e3,e4)
    
    print("Test vs actual values. Actual values in () : {} (6.5), {} (-6.5), {} (6.5), {} (0.5), {} (-6.5), {} (-6.5), {} (-6.5), {} (0.5). ".format(a,b,c,d,e,f,g,h))
    print("*************************************")
    print('')
    
def TestSimulateOnce():
    'run unit testing on function that tests whether a given point is inside both given ellipses'
    
    print("FUNCTION NAME 'simulateOnce()' function from main program.")
    print("")
    help(simulateOnce)
    print("")
    print("Goal is to test whether the function correctly determines whether a point is inside both ellipses.")
    print("")

    print("e1 FITS INSIDE e2 - /////////////////") 
    e1 = classEllipse.Ellipse(1,4,5,6,9)
    e2 = classEllipse.Ellipse(2,-4,5,10,15)
    
    p1 = classEllipse.Point(2,3) #True inside both
    p2 = classEllipse.Point(12, -5) #False outside both
    
    print('')
    print("The inputs are: ", e1,e2, p1)
    print('')
    t = simulateOnce(e1, e2, p1)
    
    print('')
    print("The inputs are: ", e1,e2, p2)
    print('')
    t2 = simulateOnce(e1, e2, p2)
    
    print('Test 1, result should be True. Actual was: {}'.format(t))
    print('Test 2, result should be None. Actual was: {}'.format(t2))
        
    print("THERE IS NO OVERLAP OF ELLIPSES - ///////////////")
    e3 = classEllipse.Ellipse(-2,-2,-4,-4,5)
    e4 = classEllipse.Ellipse(2,-2,4,-4,5)
    
    p3 = classEllipse.Point(3,-3) #In one but not both
    p4 = classEllipse.Point(-3,-3) #in the other but not both
    
    print('')
    print("The inputs are: ", e3,e4, p3)
    print('')
    t3 = simulateOnce(e3, e4, p3)
    
    print('')
    print("The inputs are: ", e3,e4, p4)
    print('')
    t4 = simulateOnce(e3, e4, p4)
    
    print('Test 3, result should be None. Actual was: {}'.format(t3))
    print('Test 4, result should be None. Actual was: {}'.format(t4))
    
    print("TWO OVERLAPING HORIZONTAL ELLIPSES - /////////////////////")
    e5 = classEllipse.Ellipse(2,0,4,0,4)
    e6 = classEllipse.Ellipse(4,0,6,0,4)
    
    p5 = classEllipse.Point(4,0) #In both
    p6 = classEllipse.Point(2,0) #in one but not both
    p7 = classEllipse.Point(2,5) #in neither
    
    print('')
    print("The inputs are: ", e5,e6, p5)
    print('')
    t5 = simulateOnce(e5, e6, p5)
    
    print('')
    print("The inputs are: ", e5,e6, p6)
    print('')
    t6 = simulateOnce(e5, e6, p6)
    
    print('')
    print("The inputs are: ", e5,e6, p7)
    print('')
    t7 = simulateOnce(e5, e6, p7)
    
    print('Test 5, result should be True. Actual was: {}'.format(t5)) #point is in both
    print('Test 6, result should be None. Actual was: {}'.format(t6)) #point is only in one
    print('Test 7, result should be None. Actual was: {}'.format(t7)) #point is in neither
    
    print("TWO OVERLAPPING VERTICAL ELLIPSES - ///////////////////")
    e7 = classEllipse.Ellipse(0,2,0,4,4)
    e8 = classEllipse.Ellipse(0,4,0,6,4)
    
    p8 = classEllipse.Point(0,4) #In both
    p9 = classEllipse.Point(0,2) #in one but not both
    p10 = classEllipse.Point(5,2) #in neither
    
    print('')
    print("The inputs are: ", e7,e8, p8)
    print('')
    t8 = simulateOnce(e7, e8, p8)
    
    print('')
    print("The inputs are: ", e7,e8, p9)
    print('')
    t9 = simulateOnce(e7, e8, p9)
    
    print('')
    print("The inputs are: ", e7,e8, p10)
    print('')
    t10 = simulateOnce(e7, e8, p10)
    
    print('Test 8, result should be True. Actual was: {}'.format(t8)) #point is in both
    print('Test 9, result should be None. Actual was: {}'.format(t9)) #point is only in one
    print('Test 10, result should be None. Actual was: {}'.format(t10)) #point is in neither
    print('')
    print("************************************")
    print('')
    
def TestSimulateMany():
    'run unit testing on function that generates random points and counts how many are in both of 2 given ellipses'
    
    print("FUNCTION NAME: 'simulateMany()' function from main program.")
    print("")
    help(simulateMany)
    print("")
    print("Goal is to test whether the function correctly creates random point within the box.")
    print("Also checking if it correctly runs the simulationOnce to see if point is in both ellipses.")
    print("And check if the function is counting the number of True occurances returned by simulateOnce.")
    print("*****************************************")
    print('')

    print("e1 FITS INSIDE e2 - /////////////////////")
    e1 = classEllipse.Ellipse(1,1,2,2,4)
    e2 = classEllipse.Ellipse(-2,-2,4,4,16)
    
    a,b,c,d,e,f,g,h = computeBox(e1,e2)
    
    result1 = simulateMany(e1,e2,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e1,e2)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")
    print('Test 1 result was: {}%'.format(result1*100))
    print("*****************************")
    print('')
 
    print("THERE IS NO OVERLAP BETWEEN THE 2 ELLIPSES - /////////////////////////")
    e3 = classEllipse.Ellipse(-2,-2,-4,-4,5)
    e4 = classEllipse.Ellipse(2,-2,4,-4,5)
    
    a,b,c,d,e,f,g,h = computeBox(e3,e4)
    
    result2 = simulateMany(e3,e4,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e3,e4)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")
    
    print('Test 2 result was: {}%. Should be 0%.'.format(result2*100))
    print("********************************")
    print('')
    
    print("TWO OVERLAPING HORIZONTAL ELLIPSES - /////////////////////")
    e5 = classEllipse.Ellipse(2,0,4,0,4)
    e6 = classEllipse.Ellipse(4,0,6,0,4)
    
    a,b,c,d,e,f,g,h = computeBox(e3,e4)
    
    result3 = simulateMany(e5,e6,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e5,e6)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")

    
    print('Test 3 result was: {}%'.format(result3*100))
    print("**********************************")
    print('')
    
    print("TWO OVERLAPPING VERTICAL ELLIPSES - ///////////////////")
    e7 = classEllipse.Ellipse(0,2,0,4,4)
    e8 = classEllipse.Ellipse(0,4,0,6,4)
    
    a,b,c,d,e,f,g,h = computeBox(e7,e8)
    
    result4 = simulateMany(e7,e8,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e7,e8)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")
    
    print('Test 4 result was {}%'.format(result4*100))
    print("")
    print("******************************************************")
    print('')

def TestSimulation():
    'unit testing on the function that calcuates are of the box, then calculates area of overlap and returns it'
    
    print("FUNCTION NAME: 'simulation()' function from main program.")
    print("")
    help(simulation)
    print("")
    print("Goal is to test whether function calculates correct area of overlap.")
    print("////////////////////////////////////////////")
    print('')

    #e1 fits inside e2 *****************************
    e1 = classEllipse.Ellipse(1,1,2,2,4)
    e2 = classEllipse.Ellipse(-2,-2,4,4,16)
    
    a,b,c,d,e,f,g,h = computeBox(e1,e2)
    
    result1 = simulation(e1,e2,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e1,e2)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")
    print('Test 1 result was: {}'.format(result1))
    print("///////////////////////////////////////////// ")
    print('')
 
    #No overlap of ellipses********************************
    e3 = classEllipse.Ellipse(-2,-2,-4,-4,5)
    e4 = classEllipse.Ellipse(2,-2,4,-4,5)
    
    a,b,c,d,e,f,g,h = computeBox(e3,e4)
    
    result2 = simulation(e3,e4,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e3,e4)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")

    
    print('Test 2 result was: {}. Should be 0.'.format(result2))
    print("/////////////////////////////////////////////")
    print('')
    
    #Overlap horizontal***********************************
    e5 = classEllipse.Ellipse(2,0,4,0,4)
    e6 = classEllipse.Ellipse(4,0,6,0,4)
    
    a,b,c,d,e,f,g,h = computeBox(e3,e4)
    
    result3 = simulation(e5,e6,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e5,e6)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")

    
    print('Test 3 result was: {}'.format(result3))
    print("////////////////////////////////////////")
    print('')
    
    #Overlap vertical****************************************
    e7 = classEllipse.Ellipse(0,2,0,4,4)
    e8 = classEllipse.Ellipse(0,4,0,6,4)
    
    a,b,c,d,e,f,g,h = computeBox(e7,e8)
    
    result4 = simulation(e7,e8,a,b,c,d,e,f,g,h)
    
    print('')
    print("The ellipse inputs are: ", e7,e8)
    print('')
    print('The box coordinate inputs are: ', a,b,c,d,e,f,g,h, sep=",")
    print("")
    
    print('Test 4 result was {}'.format(result4))
    print("/////////////////////////////////////////")
    print('')
    
    print("EXTRA CHECKING *****************")
    
    print("Area overlap of test 1 should equal area of e1.")
    print('')
    print("Area overlap of test 1 = {}. Area of e1 = {}.".format(result1, e1.getArea()))
    print('')
    print("Area overlap of test 2 should equal to 0.")
    print('')
    print("Area overlap of test 2 is {}".format(result2))
    print('')
    print("Area overlap of test 3 and test 4 should be almost equal.")
    print('')
    print("Overlap test 3 = {}. Overlap test 4 = {}.".format(result3,result4))

main()
  
  

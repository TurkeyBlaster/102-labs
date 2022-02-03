# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab5a_Act2
# Date: 30 September 2021
#

import numpy

#Functions

def range_check(bottom, top, check):
    return check >= bottom and check <= top

# Inputs

sex = input("Enter your sex (M/F): ")
if sex == "m" or sex == "M":
    sex = True
else:
    sex = False
age = int(input("Enter your age (years): "))
smoke = input("Do you smoke cigarettes (Y/N)? ")
if smoke == "y" or smoke == "Y":
    smoke = True
else:
    smoke = False
chol = int(input("Enter your total cholesterol (mg/dL): "))
hdl_chol = int(input("Enter your HDL cholesterol (mg/dL): "))
bp = int(input("Enter your systolic BP (mmHg): "))
med = input("Are you taking blood pressure medication (Y/N)? ")
if med == "y" or med == "Y":
    med = True
else:
    med = False
points = 0 

# Male

if sex:
    # Age Points
    if range_check(20, 34, age):
        points -= 9
    elif range_check(35, 39, age):
        points -= 4
    elif range_check(40, 44, age):
        points += 0
    elif range_check(45, 49, age):
        points += 3
    elif range_check(50, 54, age):
        points += 6
    elif range_check(55, 59, age):
        points += 8
    elif range_check(60, 64, age):
        points += 10
    elif range_check(65, 69, age):
        points += 11
    elif range_check(70, 74, age):
        points += 12
    elif range_check(75, 79, age):
        points += 13
        
    #Cholesterol and Smokers
    if range_check(20, 39, age):
        if range_check(160, 199, chol):
            points += 4
        elif range_check(200, 239, chol):
            points += 7
        elif range_check(240, 279, chol):
            points += 9
        elif range_check(280, numpy.inf, chol):
            points += 11
        if smoke:
            points += 8
    elif range_check(40, 49, age):
        if range_check(160, 199, chol):
            points += 3
        elif range_check(200, 239, chol):
            points += 5
        elif range_check(240, 279, chol):
            points += 6
        elif range_check(280, numpy.inf, chol):
            points += 8
        if smoke:
            points += 5
    elif range_check(50, 59, age):
        if range_check(160, 199, chol):
            points += 2
        elif range_check(200, 239, chol):
            points += 3
        elif range_check(240, 279, chol):
            points += 4
        elif range_check(280, numpy.inf, chol):
            points += 5
        if smoke:
            points += 3
    elif range_check(60, 69, age):
        if range_check(160, 199, chol):
            points += 1
        elif range_check(200, 239, chol):
            points += 1
        elif range_check(240, 279, chol):
            points += 2
        elif range_check(280, numpy.inf, chol):
            points += 3
        if smoke:
            points += 1
    elif range_check(70, 79, age):
        if range_check(240, 279, chol):
            points += 1
        elif range_check(280, numpy.inf, chol):
            points += 1
        if smoke:
            points += 1
    
    #HDL
    if range_check(-numpy.inf, 39, hdl_chol):
        points += 2
    elif range_check(40, 49, hdl_chol):
        points += 1
    elif range_check(60, numpy.inf, hdl_chol):
        points -= 1
    
    #BP
    if med:
        if range_check(120, 129, bp):
            points += 1
        elif range_check(130, 159, bp):
            points += 2
        elif range_check(160, numpy.inf, bp):
            points += 3
    else:
        if range_check(130, 159, bp):
            points += 1
        elif range_check(160, numpy.inf, bp):
            points += 2
    
    #Points to Precent
    if range_check(-numpy.inf, -1, points):
        percent = "<1"
    elif range_check(0, 4, points):
        percent = "1"
    elif range_check(5, 6, points):
        percent = "2"
    elif points == 7:
        percent = "3"
    elif points == 8:
        percent = "4"
    elif points == 9:
        percent = "5"
    elif points == 10:
        percent = "6"
    elif points == 11:
        percent = "8"
    elif points == 12:
        percent = "10"
    elif points == 13:
        percent = "12"
    elif points == 14:
        percent = "16"
    elif points == 15:
        percent = "20"
    elif points == 16:
        percent = "25"
    else:
        percent = ">30"

# Female

else:
    # Age Points
    if range_check(20, 34, age):
        points -= 7
    elif range_check(35, 39, age):
        points -= 3
    elif range_check(40, 44, age):
        points += 0
    elif range_check(45, 49, age):
        points += 3
    elif range_check(50, 54, age):
        points += 6
    elif range_check(55, 59, age):
        points += 8
    elif range_check(60, 64, age):
        points += 10
    elif range_check(65, 69, age):
        points += 12
    elif range_check(70, 74, age):
        points += 14
    elif range_check(75, 79, age):
        points += 16
        
    #Cholesterol and Smokers
    if range_check(20, 39, age):
        if range_check(160, 199, chol):
            points += 4
        elif range_check(200, 239, chol):
            points += 8
        elif range_check(240, 279, chol):
            points += 11
        elif range_check(280, numpy.inf, chol):
            points += 13
        if smoke:
            points += 9
    elif range_check(40, 49, age):
        if range_check(160, 199, chol):
            points += 3
        elif range_check(200, 239, chol):
            points += 6
        elif range_check(240, 279, chol):
            points += 8
        elif range_check(280, numpy.inf, chol):
            points += 10
        if smoke:
            points += 7
    elif range_check(50, 59, age):
        if range_check(160, 199, chol):
            points += 2
        elif range_check(200, 239, chol):
            points += 4
        elif range_check(240, 279, chol):
            points += 5
        elif range_check(280, numpy.inf, chol):
            points += 7
        if smoke:
            points += 4
    elif range_check(60, 69, age):
        if range_check(160, 199, chol):
            points += 1
        elif range_check(200, 239, chol):
            points += 2
        elif range_check(240, 279, chol):
            points += 3
        elif range_check(280, numpy.inf, chol):
            points += 4
        if smoke:
            points += 2
    elif range_check(70, 79, age):
        if range_check(160, 239, chol):
            points += 1
        elif range_check(240, numpy.inf, chol):
            points += 2
        if smoke:
            points += 1
    
    #HDL
    if range_check(-numpy.inf, 39, hdl_chol):
        points += 2
    elif range_check(40, 49, hdl_chol):
        points += 1
    elif range_check(60, numpy.inf, hdl_chol):
        points -= 1
    
    #BP
    if med:
        if range_check(120, 129, bp):
            points += 3
        elif range_check(130, 139, bp):
            points += 4
        elif range_check(140, 159, bp):
            points += 5
        elif range_check(160, numpy.inf, bp):
            points += 6
    else:
        if range_check(120, 129, bp):
            points += 1
        elif range_check(130, 139, bp):
            points += 2
        elif range_check(140, 159, bp):
            points += 3
        elif range_check(160, numpy.inf, bp):
            points += 4
    
    #Points to Precent
    if range_check(-1000000000, 8, points):
        percent = "<1"
    elif range_check(9, 12, points):
        percent = "1"
    elif range_check(13, 14, points):
        percent = "2"
    elif points == 15:
        percent = "3"
    elif points == 16:
        percent = "4"
    elif points == 17:
        percent = "5"
    elif points == 18:
        percent = "6"
    elif points == 19:
        percent = "8"
    elif points == 20:
        percent = "11"
    elif points == 21:
        percent = "14"
    elif points == 22:
        percent = "17"
    elif points == 23:
        percent = "22"
    elif points == 24:
        percent = "27"
    else:
        percent = ">30"

# Output statement
print("Your 10-year risk of a heart attack is " + percent + "%")
    
            
    
    
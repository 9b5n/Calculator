import math
radius= float(input("Radius of circle:"))
area_circle= math.pi*radius*radius
print("Area of circle=", area_circle)
circumference= 2*math.pi*radius
print("Circumference of circle", circumference)
cost= int(input("Enter cost of fencing for 1 meter"))
cost_fencing= print("Cost of fencing the circular garden:", circumference*cost)
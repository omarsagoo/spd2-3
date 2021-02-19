# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math
XC1 = 4
YC1 = 4.25
XC2 = 53
YC2 = -5.35

XA = -36
YA = 97
XB = .34
YB = .91

# Calculate the distance between the two circle
def calculate_distance():
    return math.sqrt((XC1-XC2)**2 + (YC1 - YC2)**2)

distance = calculate_distance()
print('distance ', distance)

# *** somewhere else in your program ***

# calculate the length of vector AB vector which is a vector between A and B points.
def calculate_length_of_vector():
    return math.sqrt((XA-XB)**2 + (YA-YB)**2)

length = calculate_length_of_vector()
print('length', length)
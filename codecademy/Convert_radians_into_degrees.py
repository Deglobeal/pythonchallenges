# first you have to import the math function 
import math

def radians_to_degrees(radians):
   
    #Convert radians to degrees.
    
    degrees = radians * (180 / math.pi)
    return degrees

# Example usage:
radian_value = 10  # Replace with any radian value
degree_value = radians_to_degrees(radian_value)
print(f"{radian_value} radians is equal to {degree_value} degrees.")

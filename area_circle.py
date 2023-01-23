import math

# Get the radius value from the user (in cm)
radius = float(input("Enter the radius of the circle in cm: "))

def calculate_area(radius):
    # Calculate the area of the circle
    area = radius * radius * math.pi

    # Return the calculated area
    return area

# Calculate and print the area of the circle
area = calculate_area(radius)
roundedArea = round(area, 2)  # Round the area to two decimal places
print(f"The area of the circle with radius {radius} cm is {roundedArea} cm^2.")

import math

# Taking radius input from the user
radius = float(input("Sisesta ringi raadius "))
 
# Calculating area and circumference
area = math.pi * radius**2
circumference = 2 * math.pi * radius
 
# Displaying the results
print(f"Ringi pindala {area}")
print(f"Ringi Ümbermoot: {circumference}")



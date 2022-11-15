width = int(input("Enter rectangle width:"))
assert width > 0, "Width must be grater than 0"
height = int(input("Enter rectangle height:"))
assert height > 0, "Height must be grater than 0"

area = width * height
print(f"Area = {area}")
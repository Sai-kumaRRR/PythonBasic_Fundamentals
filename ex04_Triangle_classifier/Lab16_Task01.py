# Triangle classifier

# side1 == side2 == side3 -> equals
# side1 == side2 or side2 == side3 or side1 == side3 -> 150
# else -> scalene

side1 = float(input("enter the side1\n"))
side2 = float(input("enter the side2\n"))
side3 = float(input("enter the side3\n"))

if side1 == side2 == side3:
    print("EQ")
elif side1 == side2 or side3 == side2 or side2 == side3:
    print("ISQ")
else:
    print("Scalene")
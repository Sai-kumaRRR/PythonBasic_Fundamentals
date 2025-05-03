# write a program that calculates and display the letter grade
# given numerical score (e.g A , B , C , D OR F)
# based on the following grading scale
# input - score - 89
# output - B
# a : 90 - 100
# b: 80 - 89
# c: 70 - 79
# d : 60 - 69
# f : 0 - 59

# if - elif - else

# step 1
# figure ot the input
#inputs ? int


scale = int(input("enter the number you got!\n"))

# step 2 & step 3
# print the output
# Logic
# printA -> if scale <= 100 and scale >= 90

if scale >= 90 and scale <= 100:
    print("Grade is A ")
elif scale >= 80 and scale <= 89:
    print("Grade is B ")
elif scale >= 70 and scale <= 70:
    print("Grade is C")
elif scale >= 60 and scale <= 69:
    print("Grade is D ")
elif scale >= 0 and scale <= 59:
    print("Grade is F ")
else:
    print("Invalid input")
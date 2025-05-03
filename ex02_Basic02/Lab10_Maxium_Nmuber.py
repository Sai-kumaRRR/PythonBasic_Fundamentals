# Problem find the max between 3 members


num1 = 45
num2 = 89
num3 = 78

num1 = int(input("enter the num1"))
num2 = int(input("enter the num2"))
num3 = int(input("enter the num3"))

# max_number = max(num1 , num2 , num3)
# print(max_num)

if num1 > num2 and num1 < num3:
    print("Max is", num1)
elif num2 > num1 and num2 < num3:
    print("max is", num2)
elif num3 < num1 and num2 > num1:
    print("max is", num3)
else:
    print("find they max number")

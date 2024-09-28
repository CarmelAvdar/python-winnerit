# 1
num1 = float(input("enter start point "))
num2 = float(input("enter end point "))
print(abs(num1 - num2))

# 2
grm = float(input("enter number of grams"))
print(f"in kilogram: {grm//1000}")

# 3
num1, num2 = map(int, input("enter 2 numbers").split())
print(num1%7==0 and num2%7==0)

# 4
num1 = int(input("enter a number "))
print(f"The last digit is: {num1%10}")


print("enter a number, for finish enter 'q' ")
number = input()
count = sum_ = 0
while number != 'q':
    sum_ += int(number)
    count += 1
    print("enter a number, for finish enter 'q' ")
    number = input()

print(f"the average is {sum_/count}")



from random import random

def change_list(list_numbers_: [], number_: int):
    l = len(list_numbers_)
    while l > 0:
        if list_numbers[l - 1] % number_ == 0:
            list_numbers_.remove(list_numbers[l - 1])
        l -= 1
    return list_numbers_

list_numbers = [112, 178, 6, 5, 9]
print(f"The list is {list_numbers}")
number = 2
new_list = change_list(list_numbers, number)
print(f"The new list is: {new_list}")
import random
print("הכנס 3 מספרים")
num1 = input()
num2 = input()
num3 = input()
user_numbers = [num1, num2, num3]
ran1 = random.randint(0,9)
ran2 = random.randint(0,9)
ran3 = random.randint(0,9)

if ran1 in user_numbers and ran2 in user_numbers and ran3 in user_numbers:
    print("You Win! :)")
else:
    print("You lose :( ")

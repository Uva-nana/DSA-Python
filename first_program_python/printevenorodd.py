#Write a program to print whether a number is even or odd, also take input from the user.

user_input = int(input("Please enter the number : "))
if user_input%2==0:
    print("The number :" , user_input , "is a even number")
else:
    print("The number : " ,user_input, "is a odd number")
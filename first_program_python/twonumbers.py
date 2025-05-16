#Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)


firstnum = int(input("Enter the first number: "))
secondnum = int(input("Enter the second number: "))
select_operator = input("Please select one of the operators (+, -, *, /): ")

if select_operator == "+":
    result = firstnum + secondnum
    print("Result:", result)

elif select_operator == "-":
    result = firstnum - secondnum
    print("Result:", result)

elif select_operator == "*":
    result = firstnum * secondnum
    print("Result:", result)

elif select_operator == "/":
    if secondnum != 0:
        result = firstnum / secondnum
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator selected.")

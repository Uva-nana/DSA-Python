#To find Armstrong Number between two given number.

# Function to check if a number is Armstrong
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

# Input range from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Armstrong numbers between {start} and {end} are:")

for number in range(start, end + 1):
    if is_armstrong(number):
        print(number)

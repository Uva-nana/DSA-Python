#Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.

#Simple Interset formula SI = (P*T*R)/100
principal = int(input("Enter the Principal Amount"))
time = int(input("Enter the time"))
rate = int(input("Enter the rate"))
div = 100

simple_Interest = (principal*time*rate)/div
print(simple_Interest)


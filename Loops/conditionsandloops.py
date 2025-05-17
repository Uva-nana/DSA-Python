#Testingallsyntaxofloops

#print first five numbers

print("The first five numbers are: ")
for i in range(1,6):

    print(i)

#Get input from user and print the numbers 

getinput = int (input("Give the number : "))
for i in range(1,getinput+1): #5  = 0,1,2,3,4
    print(i)

a= int(input())
b= int(input())
for i in range(a+1, b): # 2, 7  2 3,4,5,6
    print(i)
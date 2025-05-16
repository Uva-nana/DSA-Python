#To calculate Fibonacci Series up to n numbers.
# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

# Generate and print the Fibonacci series
for _ in range(n): #5 #_ is called throwaway
    print(a, end=' ') # 0 ,
    a, b = b, a + b 

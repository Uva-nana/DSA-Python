#To find out whether the given String is Palindrome or not.
string = "Madam"
string_lower = string.lower()
string_reverse = string_lower[::-1]
if string_reverse == string_lower:
    print("The Given String is a Palindrome")
else:
    print("The Given string is not a palindrome")

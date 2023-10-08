# Create a function that checks if a given string is a palindrome

def isPalindrome(s):
    return s == s[::-1]


st = input("Enter any string: ")
res = "String is palindrome" if isPalindrome(
    st) else "String is not a palindrome"
print(res)

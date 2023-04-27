
def palindrome(s):
    if s == s[::-1]:
        print ("{} is a palindrom".format(s))
    else:
        print("{} is not a palindrom".format(s))

palindrome(str(input("Enter the String : ")))
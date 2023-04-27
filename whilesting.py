#This program will repeatedly print the string until the given times
#input the string 
string = str(input("Enter string to repeat : "))
i = 1
#input how many times to repeat
num = int(input("How many times to print : "))
#check while condition
while i <= num :
    print(string)
    i = i + 1 
else :
    print("Loop Finished...!")
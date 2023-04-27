#This is Multiplication table program
#input the number 
mul=int(input ("enter a number to display the multiplication table:"))
#input multiplication upto 
#For loop is used tp calculate upto multiplication
last=int(input("enter the last point:"))
for i in range(1,last+1):
      print(i , "*", mul, "=" ,i *mul)
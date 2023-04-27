from secrets import choice


print("Select Between 1 to 7")
choice = int(input("Enter a choice : "))

if choice == 1 :
    print("DAY ONE IS SUNDAY")
elif choice == 2 :
    print("DAY ONE IS MONDAY")
elif choice == 3 :
    print("DAY ONE IS TUESDAY")
elif choice == 4 :
    print("DAY ONE IS WEDNESDAY")
elif choice == 5 :
    print("DAY ONE IS THURSDAY")
elif choice == 6 :
    print("DAY ONE IS FRIDAY")
elif choice == 7 :
    print("DAY ONE IS SATURDAY")
else :
    print("Invalid input...!\nPlease select correct input")
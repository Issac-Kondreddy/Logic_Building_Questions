month = int(input("Enter month: "))
year = int(input("Enter year: "))
odd_month = month % 2!=0
if (month == 2 and ((year%400==0) or ((year%100!=0) and (year%4==0)))):
    print("Number of days is 29")
elif month == 2:
    print("Number of days is 28")
elif odd_month:
    print("Number of days is 31")
else:
    print("Number of days is 30")
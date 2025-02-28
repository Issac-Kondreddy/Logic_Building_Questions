
for year in [2000, 1900, 2024, 2023, 2100]:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    elif year%4==0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
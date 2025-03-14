def countEvenOdd(arr):
    dict = {}
    dict['Even'] = 0
    dict['Odd'] = 0
    for i in arr:
        if i % 2 == 0:
            dict['Even'] += 1
        else:
            dict['Odd'] += 1
    return f"{dict['Even']} even elements \n{dict['Odd']} odd elements"

arr = [11, 20, 35, 40, 53]
print(countEvenOdd(arr))

def countEvenOdd2(arr):
    evencount = 0
    oddcount = 0
    for i in arr:
        if i&1==0:
            evencount += 1
        else:
            oddcount += 1
    return f"{evencount} even elements \n{oddcount} odd elements"

arr = [11, 20, 35, 40, 53]
print(countEvenOdd2(arr))
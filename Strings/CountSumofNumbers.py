def SumofNumbers(str):
    list_ = []
    for i in str:
        if not i.isalpha():
            if i.isnumeric():
                list_.append(int(i))
    return sum(list_)

String = "Daya123Ben456"
print(SumofNumbers(String))


def SumofNumbers2(str):
    sum1 = 0
    for i in str:
        if 48<=ord(i)<=57:
            sum1 += int(i)
    return sum1

String = "Daya123Ben456"
print(SumofNumbers2(String))
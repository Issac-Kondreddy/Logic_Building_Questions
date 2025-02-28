a = int(input())
b = int(input())
if a>=b:
    if a>b:
        print("a is Greater")
    else:
        print("a==b")
else:
    print("b is Greater")


print("a is Greater" if a>b else "b is Greater")

print(max(a, b))
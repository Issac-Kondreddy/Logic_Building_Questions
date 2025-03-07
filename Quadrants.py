def Quadrant(x,y):
    if x==0 and y == 0:
        return "Origin"
    elif x!=0 and y==0:
        return "X-Axis"
    elif x==0 and y!=0:
        return "Y-Axis"
    elif x>0 and y>0:
        return "First Quadrant"
    elif x<0 and y>0:
        return "Second Quadrant"
    elif x<0 and y<0:
        return "Third Quadrant"
    elif x>0 and y<0:
        return "Fourth Quadrant"
    else:
        return "Invalid Quadrant"

print(Quadrant(0,0))
print(Quadrant(0,1))
print(Quadrant(1,0))
print(Quadrant(1,1))
print(Quadrant(1,-2))
print(Quadrant(-1,0))
print(Quadrant(-1,1))


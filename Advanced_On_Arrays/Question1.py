"""
find a duplicate in an array of N+1 integers
"""

def duplicate(arr):
    dict = set()
    for num in arr:
        if num in dict:
            return num
        dict.add(num)
    return None
numbers = [1, 2, 3, 4, 2]
duplicate = duplicate(numbers)
print(f"The duplicate number is: {duplicate}")



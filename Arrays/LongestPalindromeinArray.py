def isPalindrome(n):
    temp = n
    reverse = 0
    while temp > 0:
        rem = temp % 10
        reverse = reverse * 10 + rem
        temp = temp // 10
    return n == reverse

def longestPalindrome(arr):
    n = len(arr)
    longest_palindrome = float('-inf')
    for i in range(n):
        if (isPalindrome(arr[i])) and (arr[i]>longest_palindrome):
            longest_palindrome = arr[i]
    return longest_palindrome

arr = [1, 232, 5545455, 909090, 161]
print(longestPalindrome(arr))
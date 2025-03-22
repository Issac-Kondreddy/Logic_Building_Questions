def solve(str1, str2):
    n = len(str1)
    m = len(str2)
    if n==0 and m==0:
        return True
    if m==0:
        return False
    if n==0:
        return all(c =='*' for c in str2)
    if n>0 and m>0 and ((str1[0]==str2[0]) or (str2[0]=='?')):
        return solve(str1[1:], str2[1:])
    if m>0 and str2[0]=='*':
        return solve(str1[1:], str2) or solve(str1[1:], str2[1:])
    return False


str1 = "Issac"
str2 = "Is*a?"
print(solve(str1, str2))

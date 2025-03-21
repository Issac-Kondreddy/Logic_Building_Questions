string = "I am Issac Studying Btech in USA"
new_substring = "Masters"
old_substring = "Btech"
print(string.replace(old_substring, new_substring))

index = string.find(old_substring)
print(index)
if index:
    s_new = string[:index] + new_substring + string[index+len(old_substring):]
print(s_new)

import re
s_re = re.sub(old_substring, new_substring, string)
print(s_re)
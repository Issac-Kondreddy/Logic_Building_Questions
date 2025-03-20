def palindrome1(str):
    str = str.lower()
    return str==str[::-1]

def palindrome2(str):
    str = str.lower()
    output = ""
    for i in str[::-1]:
        output += i
    return output == str

test_cases = [
    ("", True),
    ("a", True),
    ("madam", True),
    ("hello", False),
    ("RaceCar", False),
    ("A man, a plan, a canal, Panama", False),
    ("12321", True),
    ("12345", False),
    ("No 'x' in Nixon", False),
    ("😊man😊", False)
]

# Test function for palindrome1
def test_palindrome1():
    print("Testing palindrome1")
    for input_str, expected in test_cases:
        result = palindrome1(input_str)
        if result == expected:
            print(f"PASS: '{input_str}' is correctly identified as {'a palindrome' if expected else 'not a palindrome'}.")
        else:
            print(f"FAIL: '{input_str}' was expected to be {'a palindrome' if expected else 'not a palindrome'}, but was not.")

# Test function for palindrome2
def test_palindrome2():
    print("Testing palindrome2")
    for input_str, expected in test_cases:
        result = palindrome2(input_str)
        if result == expected:
            print(f"PASS: '{input_str}' is correctly identified as {'a palindrome' if expected else 'not a palindrome'}.")
        else:
            print(f"FAIL: '{input_str}' was expected to be {'a palindrome' if expected else 'not a palindrome'}, but was not.")

test_palindrome1()
test_palindrome2()
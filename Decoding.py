digits_to_char = {str(i):chr(64+i) for i in range(1, 27)}

def decode(digits):
    if not digits:
        return [""]
    results = []
    if digits[0] in digits_to_char:
        for i in decode(digits[1:]):
            results.append(digits_to_char[digits[0]] + i)
    if len(digits)>=2 and digits[:2] in digits_to_char:
        for i in decode(digits[2:]):
            results.append(digits_to_char[digits[:2]] + i)
    return results

seq = "12345"
print(decode(seq))
digit_to_char = {str(i):chr(64+i) for i in range(1,27)}
def decode(digits):
    if not digits:
        # If there are no more digits left, return a list with an empty string
        return [""]

    results = []

    # Check if the first digit is valid
    if digits[0] in digit_to_char:
        # Get all combinations starting with this one digit
        for combination in decode(digits[1:]):
            results.append(digit_to_char[digits[0]] + combination)

    # Check if the first two digits form a valid number
    if len(digits) >= 2 and digits[:2] in digit_to_char:
        # Get all combinations starting with these two digits
        for combination in decode(digits[2:]):
            results.append(digit_to_char[digits[:2]] + combination)

    return results

# Example usage
encoded_string = "131"
decoded_strings = decode(encoded_string)
print(decoded_strings)

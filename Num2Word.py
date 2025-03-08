singleDigits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tensMultiples = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
specialNumbers = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                  "Nineteen"]


def countthreedigits(number):
    words = []
    hundreds = number // 100
    if hundreds > 0:
        words.append(singleDigits[hundreds] + " Hundred")

    tens = number % 100
    if 10 < tens < 20:
        words.append(specialNumbers[tens - 10])
    elif tens == 10:
        words.append("Ten")
    else:
        ten_part = tens // 10
        unit_part = tens % 10
        if ten_part >= 2:
            words.append(tensMultiples[ten_part])
        if unit_part > 0:
            words.append(singleDigits[unit_part])

    return " ".join(words)


def num2words(number):
    if number == 0:
        return "Zero"
    parts = []
    if number >= 1000:
        thousands = number // 1000
        if thousands > 0:
            parts.append(countthreedigits(thousands) + " Thousand")
        number %= 1000

    if number > 0 or not parts:
        parts.append(countthreedigits(number))

    return " ".join(parts).strip()  # Strip any leading/trailing spaces


# Example usage
print(num2words(12345))
print(num2words(10101))

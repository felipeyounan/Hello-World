def reverse_digits(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    digits = [int(digit) for digit in reversed_str]
    return digits

number = 12345
reversed_digits = reverse_digits(number)
print(reversed_digits)


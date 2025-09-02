import random

def generate_14_digit_number():
    first_digit = random.randint(1, 9)
    other_digits = random.randint(0, 10**13 - 1)
    number = int(str(first_digit) + f"{other_digits:013d}")
    return number



def is_power_of_four(number: int) -> bool:
    if number == 1:
        return True
    n = 4
    while n < number:
        n *= 4
    if n % number == 0 and n / number == 1:
        return True
    return False

print(is_power_of_four(int(input())))
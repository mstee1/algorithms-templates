def to_binary(number: int) -> str:
    num_binary = ''
    while number > 0:
        num_binary = str(number % 2) + num_binary
        number = number // 2
    return num_binary

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))

# 69338624

def nearest_zero(list_houses: list) -> list:
    dist_houses = [0] * len(list_houses)
    dist_zero = float('inf')
    for key, value in enumerate(list_houses):
        if value == 0:
            dist_houses[key] = 0
            dist_zero = 0
            for i in range(key, 0-1, -1):
                if dist_zero <= dist_houses[i]:
                    dist_houses[i] = dist_zero
                    dist_zero += 1
                else:
                    break
            dist_zero = 0
        else:
            dist_zero += 1
            dist_houses[key] = dist_zero
    return dist_houses

def read_input() -> int:
    n: int = int(input())
    list_houses: list = [int(elem) for elem in input().split()]
    return n, list_houses

if __name__ == '__main__':
    n, list_houses = read_input()
    print(*nearest_zero(list_houses))

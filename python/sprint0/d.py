from typing import List, Tuple

def moving_average(arr: List[int], window_size: int) -> List[float]:
    count = 0
    while True:
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == window_size:
                    print(arr[i], arr[j])
                    count += 1
                    return False
        if count == 0:
            print(bug)
            return False

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

bug = 'None'
arr, window_size = read_input()
moving_average(arr, window_size)

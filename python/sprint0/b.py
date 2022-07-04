from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
	for i in range(0, len(a)):
		result.append(a[i])
		result.append(b[i])
	return result

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
result = []
print(" ".join(map(str, zipper(a, b))))

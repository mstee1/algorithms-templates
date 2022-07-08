# 69339870

from collections import Counter

def read_input():
    k = int(input()) * 2
    matrix = []
    for _ in range(4):
        numbers = input(str())
        matrix += numbers
    return k, matrix


def get_points(k, matrix):
    points = 0
    dict_matrix = dict(Counter(matrix))
    for key in dict_matrix:
        if key != '.':
            value = dict_matrix[key]
            if value <= k:
                points += 1
    return points

if __name__ == '__main__':
    k, matrix = read_input()
    print(get_points(k, matrix))

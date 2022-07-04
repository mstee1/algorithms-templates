from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    temperatures=[min(temperatures)-1]+temperatures+[min(temperatures)-1]
    w_ch=(len([n for n in range(1,len(temperatures)) 
        if temperatures[n-1]<temperatures[n] >temperatures[n+1]]))
    return w_ch

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
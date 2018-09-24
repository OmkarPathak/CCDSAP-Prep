'''
    For problem statement visit: https://www.codechef.com/problems/RAINBOWA
'''

def get_rainbow_array(array):
    start, end = 0, len(array) - 1
    
    for i in range(1, 8):
        count = 0
        while (start <= end) and (array[start] == array[end]) and (array[start] == i):
            start += 1
            end -= 1
            count += 1
        if count == 0:
            return 'no'
    if start < end:
        return 'no'
    return 'yes'

for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    print(get_rainbow_array(numbers))
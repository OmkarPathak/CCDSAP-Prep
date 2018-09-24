'''
    For problem statement visit: https://www.codechef.com/problems/CHN15A
'''

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    minions = list(map(int, input().split()))
    count = 0
    for i in range(n):
        check = minions[i] + k
        if check % 7 == 0:
            count += 1
    print(count)
    
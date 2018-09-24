'''
    For problem statement visit: https://www.codechef.com/problems/LECANDY
'''

for _ in range(int(input())):
    # n = number of elephants, c = number of candies
    n = list(map(int, input().split()))
    c = n[1]
    n = n[0]
    need = list(map(int, input().split()))

    print('Yes' if sum(need) <= c else 'No')

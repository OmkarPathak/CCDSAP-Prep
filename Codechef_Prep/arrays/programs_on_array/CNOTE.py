'''
    For problem statement visit: https://www.codechef.com/problems/CNOTE
'''

for _ in range(int(input())):
    # x = pages to write, y = pages remaining, k = budget, n = number of notebooks
    x, y, k, n = list(map(int, input().split()))
    flag = False
    for _ in range(n):
        # p = number of pages, c = cost of notebook
        p, c = list(map(int, input().split()))
        if (x - y) <= p and c <= k:
            flag = True
    if flag:
        print("LuckyChef")
    else:
        print("UnluckyChef")

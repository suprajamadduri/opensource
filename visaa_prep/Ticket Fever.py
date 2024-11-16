T = int(input())
for i in range(0,T):
    n, m = map(int,input().split())
    if n-m < 0:
        print('0')
    else:
        print(n-m)

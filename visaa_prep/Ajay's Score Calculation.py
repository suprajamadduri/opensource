t = int(input())
for i in range(0, t):
    x,n = map(int, input().split())
    each_p = x/10
    total = each_p * n
    print(int(total))

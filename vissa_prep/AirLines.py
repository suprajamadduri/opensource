X,N=map(int,input().split())
if N%100==0:
    y=N//100
    if y>=X:
        print(y-X)
    else:
        print(0)
else:
    y=(N//100)+1
    if y>=X:
        print(y-X)
    else:
        print(0)

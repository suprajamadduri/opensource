n=int(input().strip())
a=list(map(int,input().strip().split()))
r=a[::-1]
print(" ".join(map(str,r)))

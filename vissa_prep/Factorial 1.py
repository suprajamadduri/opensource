n=int(input())
factorial=1
if n <0:
    print("factorial not exist")
elif n==0:
    print("1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)

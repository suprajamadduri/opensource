n = int(input())
k = int(input())
n = bin(n)
if k < len(n) and n[-k] == '1':
    print("true")
else:
    print("false")

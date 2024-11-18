n = input()
count = 1
res = ""
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        count += 1
    else:
        res += n[i-1] + str(count)
        count = 1
print(res +n[-1]+str(count))

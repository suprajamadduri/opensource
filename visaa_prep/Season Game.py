n = int(input())
if n in [3,4,5]:
    print("Spring")
if n in [6,7,8]:
    print("Summer")
if n in [9,10,11]:
    print("Autumn")
if n in [12,1,2]:
    print("Winter")
if n not in [i for i in range(1,13)]:
    print("Invalid")

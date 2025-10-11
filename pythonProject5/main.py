s = 0
num = 0
a = int(input())
while a !=   0:
    num += 1
    if(a % 2 != 0) and (a % 3 == 0):
        s += 1
    a = int(input())
print(s)
print(num)

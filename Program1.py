d = int(input())
c = 0
for p in range (1, d + 1):
    if d % p == 0: c += d
print(c)

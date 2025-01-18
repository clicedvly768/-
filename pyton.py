n = input().split()
minn = len(n[0])
p = 0
for i in range(1,3):
    if len(n[i])<minn:
        minn=len(n[i])
        p=1
print(n[p])

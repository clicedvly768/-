n = int(input())
minn = 9
n = str(n)
for i in range(len(n)):
    if int(n[i])<minn:
        minn = int(n[i])
print(n)

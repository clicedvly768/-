n = int(input( "Имена людишек и сколько:"))
names = []
for i in range(n):
    names.append(input())
for i in range(n):
    print(i+1, names[i],)
print("Расчёт закончен.")

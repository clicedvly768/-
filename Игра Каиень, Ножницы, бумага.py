import random
while True:
    print('1-Stone')
    print('2-Scissors')
    print('3-Paper')
    p = int(input())
    n = random.randint(1,3)
    if (p==n):
            print("Draw")
    elif ((p== 1 and n==2) or (p==1 and n==3) or (p==1 and n==1)):
        print('Win')
    else:
        print('Won')

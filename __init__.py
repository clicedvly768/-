n = input().split('.')
print(n)
if 999<int(n[2])<10000:
    if 0<int(n[1])<13:
        if 0<int(n[0])<32:
            print('Good')
        else:print('Error 401')     #401 - day
    else:print('Error 402')         #402 - month
else:print('Error 403')             #403 - Year


A = int(input())
B = int(input())
if A>=1000 and A<=9999 and B>=1000 and B<=9999:
    for i in range(A,B+1,1):
        C = i
        c_1=C%10
        C1=C//10
        c_2=C1%10
        C2=C1//10
        c_3=C2%10
        C3=C2//10
        c_4=C3%10
        if (c_1==c_4 and c_2==c_3):
            print(i)
else:
    print("Не 4х-значные числа")
def Power(b, a, n):
    b = b * a
    n = n - 1
    if n == 1:
        print(b)
        return
    Power(b, a, n)

print("Write number:")
a = int(input())
print("Write power:")
n = int(input())
Power(a, a, n)
def my_div(n):
    result =n
    for i in range (n-1, 1, -1):
        if n%i ==0:
            return(i)
print("Write a number: ")
n= int(input())
max_0= my_div(n)
print(max_0)
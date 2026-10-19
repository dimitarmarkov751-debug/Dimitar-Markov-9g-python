n = int(input("Please enter a number: "))
a = 0
a1 = 1
for i in range(1,n):
    if n<a:
        break
    print(a)
    a2=a1 + a
    a=a1
    a1=a2
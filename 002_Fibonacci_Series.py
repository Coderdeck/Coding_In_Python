num = int(input())
a, b = 0 , 1
for i in range(0, num):
    print(a, end='\t')
    a, b = b, a+b

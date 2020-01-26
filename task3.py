print("Enter a number: ")
n=int(input())
factorial=1
while n>0:
    factorial=factorial*n
    n=n-1
print('Факториал равен: '+str(factorial))

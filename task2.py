print("Enter a:")
a=int(input())
print("Enter b:")
b=int(input())
print("Enter c:")
c=int(input())
count=0
for i in range(a,b):

    if i%c!=0:
        count=count+1
    i=i+1
print('Количество чисел:'+str(count))
print('Enter X:')
x = int(input())
count = 0
nech_count = 0
while count <=x:
    if count%2!=0:
        nech_count = nech_count+1
        print(count**2)
    count=count+1
print('Количество чисел: '+str(nech_count))


my_list=[]
print('Enter start:')
start=int(input())
print('Enter finish:')
finish=int(input())
print('Enter step:')
step=int(input())
def range(a,b,c):
    while a<=b:
        my_list.append(a)
        a=a+c
range(start,finish,step)
print(my_list)


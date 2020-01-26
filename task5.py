password='mypass'
print("Enter your name: ")
name=input()
print("Enter password:")
user_pass=input()
if user_pass!=password:
    while user_pass != password:
        print('Password for user: ' + name + ' is incorrect' + '\nPlease try again..')
        user_pass = input()
    print('Password for user: ' + name + ' is correct')
else:
    print('Password for user: ' + name + ' is correct')
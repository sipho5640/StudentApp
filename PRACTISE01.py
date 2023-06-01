import random

username = 'Admin'
userinput = ''
tryCount = 0
tryLimit = 3
timeOut = False

while username != userinput and not timeOut:
    if tryCount < tryLimit:
        userinput = input('Please enter your username: ')
        tryCount += 1
    else:
        timeOut = True

if timeOut:
    print('You are out of tries, ypu have been blocked from using this system')
else:
    print('You are logined in as ' + username)

passlen = int(input("enter the length of password: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, passlen))
#random sampling by joining the length of the password and the variable to generate a random password
print('Your login details are as follows, USERNAME: ' + username)
print('Your login details are as follows, PASSWORD: ' + p)

studentNumlen = int(input('pLEASE ENTER THE LENGTH OF THE STUDENT NUMBER: '))
#THE LENGTH OF ANY STUDENT NUMBER SHOULD NOT BE MORE THAN 6
st = '0123456789'
studNum = "".join(random.sample(st, studentNumlen))
print('Your automated student number is: '+studNum)


import random
r=random.randint(1, 10)
t= int(input('Guess the number '))
u=range(9)
for i in u:
    if t==r:
        print('You win')
        break
    elif t<r:
        t=int (input('Try higher '))
    elif t>r:
        t=int(input('Try lower '))


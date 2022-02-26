def issafe(password: str):
    check=0
    up=0
    down=0
    dig=0
    if len(password)<8:
        return False
    for symbol in password:
            if  symbol.isdigit():
                dig=1
            elif symbol.isalpha():
                if symbol.islower():
                    if up==1:
                        check=1
                    else:
                        down=1
                else:
                    if down == 1:
                        check = 1
                    else:
                        up = 1


    if check>0 and dig>0:
         return True
    else:
        return False
d=input('Write your password ')
if issafe(d)==True:
    print('It is safe ')
else:
    print('It is not safe ')
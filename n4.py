import random
def password():
    num=random.randint(7,10)
    st=[]
    i=0
    while i<num:
        letter=chr(random.randint(33, 126))
        st.append(letter)
        i+=1
    t="".join(st)
    return t
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
p=''
times=-1
while issafe(p)==False:
    p=password()
    times+=1
print(p, ' ', times)
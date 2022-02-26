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
print(password())
#Atousa Niazi Abkoh-98440127-python-couples-OSLab-T7-1

import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
married_coupls=[]

def search(married_coupls,groom,bride):
    couple=[]
    for i in married_coupls:
        if i[0]==groom:
            return 1
        if i[1]==bride:
            return 1
    else:
        return 0
while True:
    gr=random.choice(boys)
    groom=str(gr)
    br=random.choice(girls)
    bride=str(br)
    n=search(married_coupls,groom,bride)
    if n==0:
        married_coupls.append((groom,bride))
        if len(married_coupls)==8:
            print(married_coupls)
            break



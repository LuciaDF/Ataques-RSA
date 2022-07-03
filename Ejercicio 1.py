
import resource
import random
import math 

def fact(n):
    p1 = math.floor(math.sqrt(n))
    a = n % p1
    while(a != 0):
        p1 -= 1
        if p1==0:
            print("bajo hasta cero")
            break

        a = n % p1
    return p1
    

if __name__ == '__main__':
    
    e = 65537
    n = 999630013489
    c =  747120213790
    
    p=fact(n)
    q=int(n/p)
    n1=int(p*q)
    phin=int((p-1)*(q-1))
    mcd,d,y=resource.euclides_ext(e,phin)
    d=d%phin
    print("d: ",d)
    m1=resource.exp_Mod(c,d,n)
    print("c^d mod n == m1: ",m1)
    c1=resource.exp_Mod(m1,e,n)
    print("m1 ^ e mod n == c1: ",c1)
    print("c: ",c)
    print("EXITO!")

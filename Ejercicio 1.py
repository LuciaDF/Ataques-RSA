import RSA
import resource 

if __name__ == '__main__':
    e = 65537
    n = 999630013489
    c = 747120213790

    # halar p y q
    p = resource.fact(n)
    q = int(n / p)
    
    # hallar fi(n)
    phi = (p-1)*(q-1)

    # hallar d
    mcd, d1, y = resource.euclides_ext(e, phi)
    d = d1 % phi
    print("d = ", d)

    # ya esta
    m = RSA.cifrar(c,d,n)
    c1 = RSA.cifrar(m,e,n)
    print("m = ", m)
    print("c = " ,c1)



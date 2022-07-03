import resource

def cifrar (a,b,c):
    return resource.exp_Mod(a, b, c)

def descifrar(a,b,c):
    return resource.exp_Mod(a, b, c)

def gen_Key_RSA( ):

    p = resource.randomgen_primos(32)
    q = resource.randomgen_primos(32)
    n1 = p * q
    fi = resource.gen_fi(p,q)
    e1 = resource.gen_e(fi)
    d1 = resource.gen_d(e1,fi)

    return (e1, d1, n1)
if __name__ == '__main__':
    m = resource.randomgen_primos(32)
    (x, y, z) = gen_Key_RSA()
    print (x , y, z)

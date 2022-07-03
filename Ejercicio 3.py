import random
from hashlib import sha1

import RSA


def cifrarm(mensaje,d,n):
    
    num = [ord(char) for char in mensaje]
    c = [pow(ord(char),d,n) for char in mensaje]
    return c


def descifrarc(cif,e,n):
    num = [pow(char, e, n) for char in cif]
    strm= [chr(pow(char, e, n)) for char in cif]
    return ''.join(strm)

    
def funcionhash(M):
    m = sha1(M.encode("UTF-8")).hexdigest()
    return m
    
  
def verificar(m,M):
    m1 = funcionhash(M)
    if m == m1:
        print("Exito!: ", )
        print(m, " = ", m1)
    else:
        
        print("Verificacion fallida")
        print(m, " != ", m1)
        
def FirmaDigital(M):
    print(" ")
    print(" ")
    print("------------FIRMA DIGITAL ---------------")
    (e, d, n) = RSA.gen_Key_RSA()
    m = funcionhash(M)
    
    mcif = cifrarm(m,d,n)   
    print("Mensaje cifrado: ")
    print(''.join(map(lambda x: str(x), mcif)))
    #print(encrypted_msg)
    
    print("")
    print("---------VERIFICACION---------")
    mdescif = descifrarc(mcif,e,n)
    print("Mensaje descifrado:")  
    print(mdescif)
    print(" ")
    verificar(m, M)
    print(" ")
    print(" ")
    
def main():


    M1="La inteligencia consiste no sólo en el conocimiento, sino también en la destreza de aplicar los conocimientos en la práctica "
    M2= "Cuando pierdas, no pierdas la lección"
    M3="Si te caíste ayer, levántate hoy"
    FirmaDigital(M1)
    FirmaDigital(M2)
    FirmaDigital(M3)
  

   
main()    
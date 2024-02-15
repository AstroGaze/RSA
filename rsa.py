#Practica de Algoritmo 
#Cifrado de Mensaje

#2024-02-14

#Importamos

import Crypto.Util.number

#Numero de bits
bits = 1024

#Obtener lso primos para Alice y Bob
#Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

#Bob
pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)


print("pA: ", pA, "\n")
print("qA: ", qA, "\n")

nA = pA * qA
nB = pB * qB

print("nA" , nA )
print("nB ", nB )

#Calculamos el indicador de Eular Phi
phiA = (pA - 1) * (qA - 1)
phiB = (pB - 1) * (qB - 1) 

#Por razones de eficiencia usaremos el numero 4 de Fernet, 65537, debido a que es un primo largo y no es potencia de 2, y como
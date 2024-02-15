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

#Por razones de eficiencia usaremos el numero 4 de Fernet, 65537, debido a que es un primo largo y no es potencia de 2

e = 65537

dA = Crypto.Util.number.inverse(e, phiA)
dB = Crypto.Util.number.inverse(e, phiB)

print("dA: ", dA, "\n")

#Ciframos el menesaje 
msg = 'Hola mundo'
print("Mensaje Original: ", msg ,"\n")
print("Longitud del mensaje en bytes : ", len(msg.encode('utf-8')))

#Convertir el mensaje a numero
m = int.from_bytes(msg.encode('utf-8', byteorder = 'big'))
print("Mensaje convertido en entero: ", m, "\n")


c = pow(m, e, nB)
print("Mensaje cifrado ", c, "\n")

#Desciframos mensaje 
des = pow(c, dB, nB)

print("Mensaje Descifrado: ", des, "\n")

#Convertimos el mensaje de numero a texto
msg_final = int.to_bytes(des, len(msg), byteorder='big').decode('utf-8')
print("Mensaje convertido en entero: ", msg, "\n")
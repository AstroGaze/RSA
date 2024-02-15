import Crypto.Util.number
import Crypto.Random

# Configuración inicial igual que tu código
bits = 1024
e = 65537

# Generación de claves para Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
nA = pA * qA
phiA = (pA - 1) * (qA - 1)
dA = Crypto.Util.number.inverse(e, phiA)

# Supongamos que este es el mensaje que Alice quiere enviar y firmar
msg = 'Hola mundo'
m = int.from_bytes(msg.encode('utf-8'), byteorder='big')

# Firma el mensaje
firma = pow(m, dA, nA)

# Enviar `m` y `firma` a Bob, quien puede verificar la firma usando la clave pública de Alice
# Para este ejemplo, simularemos la verificación inmediatamente después

# Verificación de la firma
m_verificado = pow(firma, e, nA)

# Comprobamos si la verificación fue exitosa
if m == m_verificado:
    print("La firma es válida.")
else:
    print("La firma NO es válida.")

# Convertir m_verificado a texto para asegurarse de que coincide con el mensaje original
msg_verificado = int.to_bytes(m_verificado, len(msg), byteorder='big').decode('utf-8')
print("Mensaje verificado: ", msg_verificado)

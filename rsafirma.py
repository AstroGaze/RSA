import Crypto.Util.number
import Crypto.Random
from Crypto.Hash import SHA256
import Crypto.PublicKey.RSA as RSA

# Configuración inicial
bits = 1024
e = 65537

# Generación de claves para Alice
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
nA = pA * qA
phiA = (pA - 1) * (qA - 1)
dA = Crypto.Util.number.inverse(e, phiA)

# Mensaje que Alice quiere enviar y firmar
msg = 'Hola mundo como estan'

# Paso 1: Hash del mensaje
hash_obj = SHA256.new(msg.encode('utf-8'))
m_hash = int.from_bytes(hash_obj.digest(), byteorder='big')

# Paso 2: Firma del hash del mensaje
firma = pow(m_hash, dA, nA)

# Bob recibe el mensaje y la firma, y realiza la verificación

# Paso 3: Verificación de la firma
# Bob calcula el hash del mensaje recibido
hash_obj_bob = SHA256.new(msg.encode('utf-8'))
m_hash_bob = int.from_bytes(hash_obj_bob.digest(), byteorder='big')

# Bob usa la clave pública de Alice para verificar la firma
m_verificado = pow(firma, e, nA)

# Comprobación de la verificación
if m_hash_bob == m_verificado:
    print("La firma es válida.")
else:
    print("La firma NO es válida.")

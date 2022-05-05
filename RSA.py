import hashlib
import binascii
import random as rd


def home_mod_expnoent(x, y, n):  # exponentiation modulaire (on prend x puissance y)
    return(pow(x,y,n))


def generateRandomNumber(length):
    p=rd.getrandbits(length)
    p = p | 1 << (length-1) | 1
    return p

def isPrime(n,k):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0:
        return False
    # We need to find r and s such that r*(2^s)=(n-1) with r odd
    else:
        s = 0
        r = n - 1
        while r%2==0:
            s += 1
            r //=2
        # We do the test k times
        for _ in range(k):
            # Firstly, we take an a such that a is in [1,n-1]
            a=rd.randrange(1,n-1)
            # We then do the modular exponentiation of a
            x=pow(a,r,n)
            # First test to see if a^r != 1 (mod n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    # Test to see if a^((2^j)r) != -1 (mod n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        # will return True if a^r = 1 (mod n) or a^((2^j)r) = -1 (mod n)
        return True

def generatePrimeNumber(length,numberOfTests):
    numberToTest=generateRandomNumber(length)
    while not(isPrime(numberToTest,numberOfTests)):
        numberToTest=generateRandomNumber(length)
    return numberToTest


def home_ext_euclide(a, b):  # algorithme d'euclide étendu pour la recherche de l'exposant on a r=au+bv
    (r,u,v,rp,up,vp)=(a,1,0,b,0,1)
    while rp!=0:
        q=r//rp
        (r, u, v, rp, up, vp) = (rp , up , vp , r-q*rp , u-q*up , v-q*vp)
    return (v)



def home_pgcd(a, b):  # recherche du pgcd
    if (b == 0):
        return a
    else:
        return home_pgcd(b, a % b)


def home_string_to_int(x):  # pour transformer un string en int
    z = 0
    for i in reversed(range(len(x))):
        z = int(ord(x[i])) * pow(2, (8 * i)) + z
    return (z)


def home_int_to_string(x):  # pour transformer un int en string
    txt = ''
    res1 = x
    while res1 > 0:
        res = res1 % (pow(2, 8))
        res1 = (res1 - res) // (pow(2, 8))
        txt = txt + chr(res)
    return txt


def mot10char():  # entrer le secret
    secret = input("donner un secret de 10 caractères au maximum : ")
    return (secret)

def generatePublicKey(phi):
    publicKey=rd.randrange(1,phi,1)
    while(home_pgcd(publicKey, phi)!=1):
        publicKey=rd.randrange(1,phi,1)
    return publicKey



# voici les éléments de la clé d'Alice
# x1a = generatePrimeNumber(512, 128)  # p
# x2a = generatePrimeNumber(512, 128)  # q
# while (x1a==x2a):
#     x2a=generatePrimeNumber(512, 128)
# na = x1a * x2a  # n
# phia = ((x1a - 1) * (x2a - 1)) // home_pgcd(x1a - 1, x2a - 1)
# ea = generatePublicKey(phia)  # exposant public
# da = home_ext_euclide(phia, ea)  # exposant privé
# # voici les éléments de la clé de bob
# x1b = generatePrimeNumber(512, 128)  # p
# x2b = generatePrimeNumber(512, 128)  # q
# while (x1b==x2b):
#     x2b=generatePrimeNumber(512, 128)
# nb = x1b * x2b  # n
# phib = ((x1b - 1) * (x2b - 1)) // home_pgcd(x1b - 1, x2b - 1)
# eb = generatePublicKey(phib)  # exposants public
# db = home_ext_euclide(phib, eb)  # exposant privé
# print(da)
# print("Vous êtes Bob, vous souhaitez envoyer un secret à Alice")
# print("voici votre clé publique que tout le monde a le droit de consulter (de Bob)")
# print("n =", nb)
# print("exposant :", eb)
# print("voici votre précieux secret")
# print("d =", db)
# print("*******************************************************************")
# print("Voici aussi la clé publique d'Alice que tout le monde peut consulter")
# print("n =", na)
# print("exposent :", ea)
# print("*******************************************************************")
# print("il est temps de lui envoyer votre secret ")
# print("*******************************************************************")
# x = input("appuyer sur entrer")
# secret = mot10char()
# print("*******************************************************************")
# print("voici la version en nombre décimal de ", secret, " : ")
# num_sec = home_string_to_int(secret)
# print(num_sec)
# print("voici le message chiffré avec la clé publique d'Alice : ")
# chif = home_mod_expnoent(num_sec, ea, na)
# print(chif)
# print("*******************************************************************")
# print("On utilise la fonction de hashage MD5 pour obtenir le hash du message", secret)
# Bhachis0 = hashlib.sha256(secret.encode(encoding='UTF-8', errors='strict')).digest()  # MD5 du message
# print("voici le hash en nombre décimal ")
# Bhachis1 = binascii.b2a_uu(Bhachis0)
# Bhachis2 = Bhachis1.decode()  # en string
# Bhachis3 = home_string_to_int(Bhachis2)
# print(Bhachis3)
# print("voici la signature avec la clé privée de Bob du hachis")
# signe = home_mod_expnoent(Bhachis3, db, nb)
# print(signe)
# print("*******************************************************************")
# print("Bob envoie \n \t 1-le message chiffré avec la clé public d'Alice \n", chif, "\n \t 2-et le hash signé \n", signe)
# print("*******************************************************************")
# x = input("appuyer sur entrer")
# print("*******************************************************************")
# print("Alice déchiffre le message chiffré \n", chif, "\nce qui donne ")
# dechif = home_int_to_string(home_mod_expnoent(chif, da, na))
# print(dechif)
# print("*******************************************************************")
# print("Alice déchiffre la signature de Bob \n", signe, "\n ce qui donne  en décimal")
# designe = home_mod_expnoent(signe, eb, nb)
# print(designe)
# print("Alice vérifie si elle obtient la même chose avec le hash de ", dechif)
# Ahachis0 = hashlib.sha256(dechif.encode(encoding='UTF-8', errors='strict')).digest()
# Ahachis1 = binascii.b2a_uu(Ahachis0)
# Ahachis2 = Ahachis1.decode()
# Ahachis3 = home_string_to_int(Ahachis2)
# print(Ahachis3)
# print("La différence =", Ahachis3 - designe)
# if (Ahachis3 - designe == 0):
#     print("Alice : Bob m'a envoyé : ", dechif)
# else:
#     print("oups")

# RSA_CRT

# Génération des clés :

p=generatePrimeNumber(512, 128)
q=generatePrimeNumber(512,128)
if(q>=p):
    temp=q
    q=p
    p=temp
n=p*q
phiN=(p-1)*(q-1)
e=generatePublicKey(phiN)
d=home_mod_expnoent(e,-1,phiN)
dp=home_mod_expnoent(d,1,p-1)
dq=home_mod_expnoent(d,1,q-1)
qInv=home_mod_expnoent(q,-1,p)

print("Voici p: ",p,"\net q: ",q)
print("n: ",n)
print("phi(n): ",phiN)
print("la clé publique e: ",e)
print("d: ",d)
print("dp: ",dp,"dq: ",dq)
print("qInv: ",qInv)

messageToEncode=input("Message à encoder: ")
messageToEncodeInDecimal = home_string_to_int(messageToEncode)
print("La version décimal du message à encoder: ", messageToEncodeInDecimal)

messageEncoded=home_mod_expnoent(messageToEncodeInDecimal,e,n)
print("Le message encodé: ",messageEncoded)
mp=home_mod_expnoent(messageEncoded,dp,p)
mq=home_mod_expnoent(messageEncoded,dq,q)
h=qInv*((mp-mq))%p
m=mq+h*q
messageDecoded=home_int_to_string(m)
print("Le message décodé: ",messageDecoded)






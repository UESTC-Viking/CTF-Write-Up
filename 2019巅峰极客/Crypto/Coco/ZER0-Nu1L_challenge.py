from Crypto.Util.number import *
from Crypto.Random.random import *
from flag import flag
import gmpy2

def CoCoCoCo(Co, CoCo):  # gcd()
    while CoCo: Co, CoCo = CoCo, Co % CoCo #欧几里得的前提 ??? = 
    return Co
def CoCoCoCoCo(a, n, d): # pow(a,b,c)
    four = 1
    while n != 0:
        if (n & 1) == 1: #n == b'1111'
            four = (four * a) % d
        n >>= 1
        a = (a * a) % d
    return four

a = getStrongPrime(1024)
p = getStrongPrime(1024)
c = getStrongPrime(1024)

eight = pow(c, a, p)
while True:# get a number(n), enable (n-1, random-e) = 1
    e = randint(1, 2 ** 512) # 1- 2 ** 512 之间
    if CoCoCoCo(e, p - 1) == 1:
        break

six = bytes_to_long("CoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCoCo")
ten = pow(c, e, p)
eleven = (six * pow(eight, e, p)) % p
seven = bytes_to_long(flag)######################
twelve = (seven * pow(eight, e, p)) % p

with open('cipher.txt', 'w') as f:
    f.write("CoCoCoCoCoCoCoCoCoCo = " + str(ten) + "\n")
    f.write("CoCoCo = " + str(c) + "\n")
    f.write("CoCoCoCoCoCoCoCoCoCoCo = " + str(eleven) + "\n")
    f.write("CoCo = " + str(p) + "\n")
    f.write("CoCoCoCoCoCoCoCoCoCoCoCo = " + str(twelve) + "\n")

# two - p
# CoCoCoCoCo(a, n, d)??
# (e, n - 1) == 1
# three - c
# one - a
# nine - e
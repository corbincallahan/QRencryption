from random import Random

def diffieHellman(base, e, p):
    return pow(base, e, p)

def elGamalKey(g, a, p):
    if(not (1 <= a and a <= p)):
        return -1
    return pow(g, a, p)

def elGamalEncrypt(m, g, A, p):
    rand = Random()
    k = rand.randrange(1, p)
    c1 = pow(g, k, p)
    c2 = m * pow(A, k, p)
    return (c1, c2)

def elGamalDecrypt(c1, c2, a, p):
    inv = pow(c1, a, p)
    inv = pow(inv, p - 2, p)
    return (inv * c2) % p

def stringToInt(message): #Works with alphanumerics and whitespace
    out = 0
    for character in message.lower():
        out *= 37
        if(character.isalpha()):
            out += ord(character) - 97
        elif(character.isdigit()):
            out += ord(character) - 22
        else:
            out += 36
    return out

def intToString(message):
    out = ""
    while(message > 0):
        character = message % 37
        message //= 37
        if(character < 26):
            out = chr(character + 97) + out
        elif(character < 36):
            out = chr(character + 22) + out
        else:
            out = ' ' + out
        
    return out

p = 10 ** 48 + 193
myString = "thirty character encrypt limit"
print("String length: " + str(len(myString)))
m = stringToInt(myString)
print("m: " + str(m))
a = 15695809
g = 2
A = elGamalKey(g, a, p)
print("A: " + str(A))
c1c2 = elGamalEncrypt(m, g, A, p)
print("c1c2: " + str(c1c2))
print("stringified c1: " + intToString(c1c2[0]))
print("stringified c2: " + intToString(c1c2[1]))
mPrime = elGamalDecrypt(c1c2[0], c1c2[1], a, p)
print("mPrime: " + str(mPrime))
myStringPrime = intToString(mPrime)
print(myStringPrime)
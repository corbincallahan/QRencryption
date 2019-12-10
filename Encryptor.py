from random import Random

p = 10 ** 55 + 21

def diffieHellman(base, e):
    return pow(base, e, p)

def elGamalKey(g, a):
    if(not (1 <= a and a <= p)):
        return -1
    return pow(g, a, p)

def elGamalEncrypt(m, g, A):
    rand = Random()
    k = rand.randrange(1, p)
    c1 = pow(g, k, p)
    c2 = m * pow(A, k, p)
    return (c1, c2)

def elGamalDecrypt(c1, c2, a):
    inv = pow(c1, a, p)
    inv = pow(inv, p - 2, p)
    return (inv * c2) % p

def stringToInt(message): #Works with alphanumerics and whitespace
    out = 0
    for character in message:
        out *= 66
        if(character.isalpha()):
            if(character.islower()):
                out += ord(character) - 97
            else:
                out += ord(character) - 39
        elif(character.isdigit()):
            out += ord(character) + 4
        elif(character == '.'):
            out += 62
        elif(character == '/'):
            out += 63
        elif(character == ':'):
            out += 64
        else:
            out += 65
    return out

def intToString(message):
    out = ""
    while(message > 0):
        character = message % 66
        message //= 66
        if(character < 26):
            out = chr(character + 97) + out
        elif(character < 52):
            out = chr(character + 39) + out
        elif(character < 62):
            out = chr(character - 4) + out
        elif(character == 62):
            out = '.' + out
        elif(character == 63):
            out = '/' + out
        elif(character == 64):
            out = ':' + out
        else:
            out = ' ' + out
        
    return out

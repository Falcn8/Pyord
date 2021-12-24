__version__ = '1.0'

import random

def encrypt(text:str, shift:int=64):
    s = text
    l = []
    l2 = []
    for i in s:
        l.append(i)
    for i in range(len(l)):
        try:
            symbol = random.choice(["+", "-"])
            letter = chr(eval(f"ord(l[i]){symbol}{str(shift)}"))
            l2.append(symbol)
            l2.append(letter)
        except:
            try:
                nsymbol = ["+", "-"]
                nsymbol.remove(symbol)
                symbol = nsymbol[0]
                letter = chr(eval(f"ord(l[i]){symbol}{str(shift)}"))
                l2.append(symbol)
                l2.append(letter)
            except:
                symbol = "="
                l2.append(symbol)
                l2.append(l[i])
    return "".join(l2)

def decrypt(text:str, shift:int=64):
    s = text
    symbols = []
    for i in range(0, len(s), 2):
        symbols.append(s[i])
    letters = []
    for i in range(1, len(s)+1, 2):
        letters.append(s[i])
    for i in range(len(letters)):
        if symbols[i] != "=":
            symbol = ["+", "-"]
            symbol.remove(symbols[i])
            symbol = symbol[0]
            letters[i] = chr(eval(f"ord(letters[i]){symbol}{str(shift)}"))
    return "".join(letters)

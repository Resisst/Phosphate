from base64 import b64encode as w 
from random import randint as v
from random import choice as x

m = "!£$^&*():;#~/?.>,<"

def j(max:int):
    return v(int(float(max/2)), max)

def u(s:int):
    return ''.join(x(m)for _ in range(s))

def q(s:str):
    if len(s) % 4 == 0:
        l = int(len(s) / 4)
        s = s[l:] + s[:l]
        l = l * 2
        s = s[l:] + s[:l]
        return s
    else:
        return False

def g(string:str):
    return " ".join(f"{ord(i):08b}" for i in string)

def encode(s:str):
    n = ''
    for c in w(s.encode("utf8")).decode():
        n += u(j(3)) + c
    n = f"[{n}]"
    while len(n) % 4 != 0:
        n += "]"
    n = q(n)
    n = g(n)
    n = n.replace("11", "+").replace("10", "&").replace("00", "_").replace("+ ", "-").replace("1 ", "=").replace("& ", "[").replace("0 ", "]")
    while len(n) % 4 != 0:
        n += "."
    e = q(n)
    return e[::-1]
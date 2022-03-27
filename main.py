import phosphate
from colorama import Fore
from codecs import encode as c_encode

reverse_shuffle = """
def f(s:str):
    if len(s) % 4 == 0:
        l = int(len(s) / 2)
        s = s[l:] + s[:l]
        l = int(l / 2)
        s = s[l:] + s[:l]
        l = l * 2
        s = s[l:] + s[:l]
        return s
    else:
        return False"""
deobfuscate_function = """
from base64 import b64decode as t
from string import digits as p
from string import ascii_letters as o

h = p + o
def b(s:str):
    s = s.replace(" ", "")
    c = 1
    l = ''
    n = ''
    for i in s:
        l += i
        if c == 8:
            n += chr(int(l, 2))
            c = 0
            l = ''
        c += 1
    return n

def f(s:str):
    if len(s) % 4 == 0:
        l = int(len(s) / 2)
        s = s[l:] + s[:l]
        l = int(l / 2)
        s = s[l:] + s[:l]
        l = l * 2
        s = s[l:] + s[:l]
        return s
    else:
        return False

def r(s:str):
    s = s[::-1]
    s = f(s).replace(".", "")
    s = s.replace("]", "0 ").replace("[", "& ").replace("=", "1 ").replace("-", "+ ").replace("_", "00").replace("&", "10").replace("+", "11")
    s = b(s)
    s = f(s)
    n = ""
    for i in s:
        if i in h + "=":
            n += i
    return t(n.encode("utf8")).decode()
"""
def shuffle(s:str):
    if len(s) % 4 == 0:
        l = int(len(s) / 4)
        s = s[l:] + s[:l]
        l = l * 2
        s = s[l:] + s[:l]
        return s
    else:
        return False

def obfuscate():
    file_name = input(f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter the name of the file to obfuscate: ")
    if not file_name[-3:] == ".py":
        file_name += ".py"
    encrypted_file_name = file_name[:-3] + "_obfuscated.py"
    with open(file_name, "r") as f:
        code_list = f.readlines()
        imports = []
        for i in code_list:
            if i.startswith("import"):
                imports.append(i)
        imports = "".join(imports)
        code_list = [i for i in code_list if not i.startswith("import")]
        code = "".join(code_list)
        obfuscated_code = phosphate.encode(code)
        layer1 = deobfuscate_function+'\n'+f"exec(r(\"{obfuscated_code}\"))"
        layer2 = c_encode(layer1.encode("utf8"), "uu").decode()
        while len(layer2) % 4 != 0:
            layer2 += "~"
        layer3_shuffled = shuffle(layer2).encode("utf8")
        layer3_compression = c_encode(layer3_shuffled, "zip")
        with open(encrypted_file_name, "w") as f:
            if len(imports) > 1:
                f.write(f"from codecs import decode as c_decode\n{imports}\n{reverse_shuffle}\nexec(c_decode(f(c_decode({layer3_compression}, 'zip').decode()).replace('~', '').encode('utf8'), 'uu').decode())")
            else:
                f.write(f"from codecs import decode as c_decode\n{reverse_shuffle}\nexec(c_decode(f(c_decode({layer3_compression}, 'zip').decode()).replace('~', '').encode('utf8'), 'uu').decode())")


        print(f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Obfuscated file saved as {encrypted_file_name}")

obfuscate()
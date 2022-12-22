def palin(s):
    return s == s[::-1]
    if s:
        print(True)
    else:
        print(False)    

print(palin('121'))
print(palin('-34'))
print(palin('121'))
print(palin('454'))
print(palin('-545'))
#cézarová šifra
ret = "Ahoj"
print(ord("A"))
print(ord("h"))
print(ord("o"))
print(ord("j"))

ret1 = (chr(65 + 1)) + ret[1:],  (chr(104 + 1)) + ret[2:], (chr(111 + 1)) + ret[3:], (chr(106 + 1)) + ret[4:]
ret2 = (chr(104 + 1)) + ret[2:]
ret3 = (chr(111 + 1)) + ret[3:]
ret4 = (chr(106 + 1)) + ret[4:]

print(ret1)


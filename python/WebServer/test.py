a = bytearray([50,51,52,53,54,0,0,0])
string = ''
for s in a:
    string += chr(s)
print(string)

b = bytearray([1,2,3])
string2 = int.from_bytes(b,'little')

print(string2)

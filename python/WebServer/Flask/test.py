#data = [0, 1, 2, 3, 97, 98, 99,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
data = [0, 1, 2, 3, 97, 98, 99]

# $B%P%$%HNs$N:BI8$rI=<($9$k(B
s = str()
a = '|' # ASCII$BJ8;zIt(B
s += '{0:08X}  '.format(0)
for i, byte in enumerate(data, start=1):
    s += '{0:02X} '.format(byte)
    # ASCII$BJ8;z$NHO0O30$J$i(B' '$BJ8;z$rI=<((B
    if byte in range(32, 127):
        a += chr(byte)
    else:
        a += '.'
    # i$B$,(B16$B$NG\?t$G(BASCII$BIt$rDI2C$9$k(B
    if i % 16 == 0:
        s += '{0}|\n{1:08X}  '.format(a, i)
        a = '|' # a$B$r%/%j%"(B
    elif i % 8 == 0:
        s += ' '
    # $B:G8e$N%9%Z!<%9$r@07A$9$k(B
    if len(data) == i:
        if (16 - i % 16) < 8:
            add_space = ''
        else:
            add_space = ' '
        s += '   ' * (16 - i % 16)
        s += add_space
        a += ' ' * (16 - i % 16)
        a += '|'
        s += a
print(s, end='')
print('$B!z(B')


        

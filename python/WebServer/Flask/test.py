#data = [0, 1, 2, 3, 97, 98, 99,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
data = [0, 1, 2, 3, 97, 98, 99]

# バイト列の座標を表示する
s = str()
a = '|' # ASCII文字部
s += '{0:08X}  '.format(0)
for i, byte in enumerate(data, start=1):
    s += '{0:02X} '.format(byte)
    # ASCII文字の範囲外なら' '文字を表示
    if byte in range(32, 127):
        a += chr(byte)
    else:
        a += '.'
    # iが16の倍数でASCII部を追加する
    if i % 16 == 0:
        s += '{0}|\n{1:08X}  '.format(a, i)
        a = '|' # aをクリア
    elif i % 8 == 0:
        s += ' '
    # 最後のスペースを整形する
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
print('★')


        

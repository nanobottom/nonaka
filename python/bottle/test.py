import configparser

inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
body_lst = bytearray()
# name
name = [ord(s) for s in inifile.get('response', 'name')]
# 20bytesの内、埋まらなかった箇所に0x00を付加
zero_lst = [0] * (20 - len(name))
name.extend(zero_lst)
body_lst.extend(name)

# address
address = [ord(s) for s in inifile.get('response', 'address')]
# 100bytesの内、埋まらなかった箇所に0x00を付加
zero_lst = [0] * (100 - len(address))
address.extend(zero_lst)
body_lst.extend(address)

# age
body_lst.append(int(inifile.get('response', 'age')))

# birthday
birthday = [ord(s) for s in inifile.get('response', 'birthday')]
# 20bytesの内、埋まらなかった箇所に0x00を付加
zero_lst = [0] * (20 - len(birthday))
birthday.extend(zero_lst)
body_lst.extend(birthday)

print(body_lst)

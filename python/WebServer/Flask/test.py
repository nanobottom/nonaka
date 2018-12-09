def range_check(param, param_name, begin, end):
    try:
        if (param in range(begin, end)) == False:
            raise ValueError('Parameter {} is over range of num.'.format(param_name))
    except ValueError as e:
        print("ValueError : {}".format(e))

def get_little_endian(data):
    s = ""
    data.reverse()
    for b in data:
        s += format(b, "02x")
        s += " "
    return s

def get_data_as_bits(offset, digit):
    mask = 0
    for i in range(digit):
        mask += 2**i
    data = 0b01101010
    return bin(data>>offset & mask)


range_check(8, 'test', 0, 9)
data = [1, 2, 33, 44]
print(get_little_endian(data))
print(get_data_as_bits(3, 4))

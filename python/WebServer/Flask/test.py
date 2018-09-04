x = 0b10011010
def get_bit(bits, digit):
    digit -= 1
    return bin(int(bin(bits >> digit), 2) & 0b1)
print(get_bit(x,1))
print(get_bit(x,2))
print(get_bit(x,3))
print(get_bit(x,4))

def set_bit(bits, digit, change_bit):
    digit -= 1
    and_bits = (0b11111110, 0b11111101, 0b11111011, 0b11110111, 0b11101111, 0b11011111, 0b10111111, 0b01111111)
    or_one_bits = (0b1, 0b10, 0b100, 0b1000, 0b10000, 0b100000, 0b1000000, 0b10000000)

    if change_bit == 0:
        return bin(bits & and_bits[digit])
    elif change_bit == 1:
        return bin(bits & and_bits[digit] | or_one_bits[digit])

print(set_bit(x, 4, 0))
print(set_bit(x, 3, 1))
print(set_bit(x, 8, 0))
print(set_bit(x, 7, 1))


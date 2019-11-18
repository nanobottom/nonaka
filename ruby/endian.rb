byte_array = [0x00, 0x11, 0x22, 0x33]
def get_value_as_little_endian(byte_array, offset, size)
  ans = 0
  for i in 0..(size - 1) do
    ans |= byte_array[offset, size][i] << (i * 8)
  end
  printf("0X%02X\n", ans)
end

def get_value_as_big_endian(byte_array, offset, size)
  ans = 0
  ia = 0..(size - 1)
  ia = ia.to_a
  ia.zip(ia.reverse) do |i, j|
    ans |= byte_array[offset, size][j] << (i * 8)
  end
  printf("0X%04X\n", ans)
end
get_value_as_little_endian(byte_array, 2, 2)
get_value_as_big_endian(byte_array, 2, 2)

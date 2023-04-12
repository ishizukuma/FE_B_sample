# def encode(codePoint):
#     utf8Bytes = [0b11100000, 0b10000000, 0b10000000] #224, 128, 128
#     cp = codePoint
    
#     for i in range(len(utf8Bytes)-1, 0, -1):
#         utf8Bytes[i] = 0b10000000 | (cp & 0b00111111)
#         cp >>= 6
    
#     # utf8Bytes[0] = (0b11110000 << 2) | (cp >> 12)
#     return utf8Bytes

# print(encode(0x3042))  # [0b11100011, 0b10000001, 0b10000010]

# 未完成:完全実装できていませんがイメージはつくと思います。
def encode(codePoint):
    utf8Bytes = [224, 128, 128]
    cp = codePoint
    
    for i in range(len(utf8Bytes), 0, -1):
        utf8Bytes[i] = utf8Bytes[i] + (cp % 64)
        cp = cp // 64
    
    return utf8Bytes

print(encode(0x3042))
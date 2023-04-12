def rev(byte):
    rbyte = byte
    r = 0
    
    for i in range(0, 8):
        r = (r << 1) | (rbyte & 1)
        rbyte = (rbyte >> 1) & 0b01111111  # 末尾のビットを落とす
        
    return r

result = rev(0b01001011)
ans = format(result, "b")
print(ans)
# 0b11010010
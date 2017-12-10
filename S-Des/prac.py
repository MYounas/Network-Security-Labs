import binascii

# key="1234"
#
# key=list(key)
# key.reverse()
# temp=key.pop()
# key.reverse()
# key.append(temp)
#
# print(key)

# key="567894312"
# key=list(key)
# key=int(key)

# a=bin(0b0100 ^ 0b1000)
# a.decode('ascii')

# print( a[2:]+"ddfd" )

# a="0100"
# # a=map(bin,bytearray(a,'utf-8'))
# # a=bin(a)
# a=bin(ord(a[1])).zfill(1)
# print(a)
# print(bin(a^b))

# key=key[1::]+key[:1:]
# key=key[2:]+key[:2]
# key=key[:1]
# print(key[::-1])
# print(key)



def convertXOR(t1, t2):
    ansr = ""
    for i in range(len(t1)):
        ansr += "0" if t1[i] == t2[i] else "1"

    return ansr

print(convertXOR("0100","1000"))

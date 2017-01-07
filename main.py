import EncodeAndDecode

TestString = 'Hello world'

print('Encoding: ' + TestString)
EncodedString = EncodeAndDecode.encode(TestString)
print('Coded as: ' + EncodedString)

print(' ')
print('Decoding: ' + EncodedString)
DecodedString = EncodeAndDecode.decode(EncodedString)
print('Decoded as: ' + DecodedString)





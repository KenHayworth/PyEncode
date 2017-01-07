
AlphabetString = 'abcdefghijklmnopqrstuvwxyz'
CodeString = 'zyxwvutsrqponmlkjihgfedcba'

def encode(InputString):
    EncodedString = ''
    for letter in InputString.lower():
        AlphabetIndex = AlphabetString.find(letter)
        if AlphabetIndex == -1:
            EncodedString = EncodedString + letter
        else:
            EncodedString = EncodedString + CodeString[AlphabetIndex]
    return EncodedString
    
def decode(InputString):
    DecodedString = ''
    for letter in InputString.lower():
        CodeIndex = CodeString.find(letter)
        if CodeIndex == -1:
            DecodedString = DecodedString + letter
        else:
            DecodedString = DecodedString + AlphabetString[CodeIndex]
    return DecodedString
    
    

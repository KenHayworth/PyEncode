AlphabetString = 'abcdefghijklmnopqrstuvwxyz'
CodeString = 'zyxwvutsrqponmlkjihgfedcba'

def encode(InputString):
    EncodedString = ''
    for letter in InputString:
        AlphabetIndex = AlphabetString.find(letter.lower())
        if AlphabetIndex == -1:
            EncodedLetter = letter
        else:
            if letter.islower():
                EncodedLetter = CodeString[AlphabetIndex]
            else: #change to uppercase
                EncodedLetter = CodeString[AlphabetIndex].upper()
        EncodedString = EncodedString + EncodedLetter
    return EncodedString
    
def decode(InputString):
    DecodedString = ''
    for letter in InputString:
        CodeIndex = CodeString.find(letter.lower())
        if CodeIndex == -1:
            DecodedLetter = letter
        else:
            if letter.islower():
                DecodedLetter = AlphabetString[CodeIndex]
            else: #change to uppercase
                DecodedLetter = AlphabetString[CodeIndex].upper()
        DecodedString = DecodedString + DecodedLetter
    return DecodedString
    
    

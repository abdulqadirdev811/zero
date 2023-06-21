def getShiftedCharactor(ordNumber,shiftValue):
    sumASCII = ordNumber+ shiftValue 
    encrypedValue = sumASCII 
    if sumASCII > 122:
       encrypedValue = (sumASCII - 122) + 96
    encrypedValue = chr(encrypedValue)
    return encrypedValue


def calculateCaesarCipher(plainText,shiftValue):
    asciiCodesList = range(97,123)
    ecryptedList = [getShiftedCharactor(ord(i),shiftValue) if ord(i) in asciiCodesList  else i for i in plainText]
    ecrypteText = ''.join(ecryptedList)
    return ecrypteText


plainText,shiftValue = "abcd xyz",4
caesarText = calculateCaesarCipher(plainText,shiftValue)
print(caesarText)
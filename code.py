import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]
decodeAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]
finalAlphabet = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None, 'm': None, 'n': None, 'o': None, 'p': None, 'q': None, 'r': None, 's': None, 't': None, 'u': None, 'v': None, 'w': None, 'x': None, 'y': None, 'z': None," ":None}


#create decode key
disk1 = random.randint(1,100000)
disk2 = random.randint(1,1000000)
disk3 = random.randint(1,10000000)
rotationletter = random.randint(0,26)
print(f"___IMPORTANT___ key:{rotationletter} disk 1: {disk1} disk 2: {disk2} disk 3: {disk3}")
#rotate the decode alphabet
decodeAlphabet[rotationletter:]
decodeAlphabet = decodeAlphabet[rotationletter:] + decodeAlphabet[:rotationletter]
decodeAlphabet = decodeAlphabet[disk1:] + decodeAlphabet[:disk1]
decodeAlphabet = decodeAlphabet[disk2:] + decodeAlphabet[:disk2]
decodeAlphabet = decodeAlphabet[disk3:] + decodeAlphabet[:disk3]
#print alphabet and decode
print("decode:", decodeAlphabet)
print("\n orignal:",alphabet)
for key, value in zip(finalAlphabet, decodeAlphabet):
    finalAlphabet[key] = value
#final decode
print("use to decode:",finalAlphabet)
#get user input
stringToEncode = input()
encodedString = ''
#run for as many chars in the user input
for char in stringToEncode:
	stringToEncode += finalAlphabet.get(char.lower(), char)
	encodedString = stringToEncode
#output
print(encodedString)

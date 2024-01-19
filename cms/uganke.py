def letter_position(letter):
    if len(letter) == 1 and letter.isalpha():
        letter = letter.lower()
        return ord(letter) - ord('a') + 1
    
    
def number_to_letter(position):
    if isinstance(position, int) and 1 <= position <= 26:
        letter = chr(ord('a') + position - 1)
        return letter

def what_shift(letter, shifter):
    if letter == " " or shifter == " ":
        pass
    elif letter > shifter:
        LoopShift = (26 - letter_position(letter)) + letter_position(shifter) + 1
        if LoopShift > 26:
           return LoopShift-26
        return LoopShift
    else:
        noLoopShift = letter_position(shifter) - letter_position(letter) + 1
        return noLoopShift
    
    
    
   # 
   # poettvojnovsl

cipheredText = "wtxf iacn jpp kuvaxzrja zaoyu epox"
decipherStart = "poet tvoj novsl"

deciphered = []
decipheredText = []
KEY = []
starterKEY = []
i=0
for i in range(len(decipherStart)):
    starterKEY.append(number_to_letter(what_shift(decipherStart[i], cipheredText[i])))
    KEY = [item for item in starterKEY if item is not None]
    
    
print(f"Key is: {KEY}")   
keyLenght = len(KEY)
k = 0
j = 0
print(keyLenght)
whereBlank = []
for j in range(len(cipheredText)):
    if cipheredText[j] is None:

        pass
    else:
        letter_pos = letter_position(cipheredText[j])
        key_pos = letter_position(KEY[k])

        if letter_pos is not None and key_pos is not None:
            backShift = letter_pos - key_pos
            if backShift < 0:
                backerShift = 26 + backShift
                deciphered.append(backerShift)
            else:
                deciphered.append(backShift)

        k += 1
        if k == keyLenght:
            k = 0
        
for m in range(len(deciphered)):
    decipheredText.append(number_to_letter(deciphered[m]+1))

print(decipheredText)

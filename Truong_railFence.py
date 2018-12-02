# This program will take your input and will encrypt or decrypt your message depending on your choice.
# decryption credits to profecali on youtube


choice = input("Would you like to encrypt or decrypt a message? Enter E for encrypt or D for decrypt; or B for both: ")

def Scramble2Text(plainText):
    charCount = 0
    evenChars = ""
    oddChars = ""
    if(len(plainText)%2 == 1):
            plainText = plainText + " "
    for ch in plainText:
        if(charCount%2 == 0):
            evenChars += ch
        else:
            oddChars += ch
        charCount += 1
    cipherText = oddChars + evenChars
    return cipherText


if(choice == "E"):
    plainText = input("Please enter text you would like to encrypt: ")
    encryptedmsg = Scramble2Text(plainText)
    print(encryptedmsg)

def decryptMessage(cipherText):
    half = len(cipherText)//2
    plainText = ""
    oddChars = cipherText[:half]
    evenChars = cipherText[half:]
    if len(evenChars) > len(oddChars):
        plainText += evenChars[-1]
    for i in range(half):
        plainText += evenChars[i]
        plainText += oddChars[i]
    return plainText

if(choice == "D"):
    cipherText = input("Please enter text you would like to decrypt: ")
    decryptedMessage = decryptMessage(cipherText)
    print(decryptedMessage)

if(choice == "B"):
    plainText = input("Please enter text you would like to encrypt: ")
    encryptedmsg = Scramble2Text(plainText)
    print(encryptedmsg)
    cipherText = encryptedmsg
    decryptedMessage = decryptMessage(cipherText)
    print(decryptedMessage)
leaveOpen = input("Press enter to end the program: ")


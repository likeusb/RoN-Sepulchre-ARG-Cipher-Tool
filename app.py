# Ready or Not Sepulchre ARG Cipher Tool
# Developed by @Likeusb on GitHub & Discord, I give you full permission to modify this tool in whatever way you see fit, so long as you don't take credit for it.

# Defines dicts and initializes Wall of Letters
gwynn = {
    0: 'A',
    1: 'P',
    2: 'E',
    3: 'T',
    4: 'I',
    5: 'X',
    6: 'M',
    7: 'B',
    8: 'Q',
    9: 'F',
    10: 'U',
    11: 'J',
    12: 'Y',
    13: 'N',
    14: 'C',
    15: 'R',
    16: 'G',
    17: 'V',
    18: 'K',
    19: 'Z',
    20: 'O',
    21: 'D',
    22: 'S',
    23: 'H',
    24: 'W',
    25: 'L'
}
a0z = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}
a1z = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z'
}
kam = {
    1: ['a', 'b', 'c', 'd', 'e'],
    2: ['f', 'g', 'h', 'i', 'j'],
    3: ['k', 'l', 'm', 'n', 'o'],
    4: ['p', 'q', 'r', 's', 't'],
    5: ['u', 'v', 'w', 'x', 'y', 'z']
}

WoL = []

while True:
    FoR = input("Would you like to encrypt or decrypt?\n1> Decrypt\n2> Encrypt\n> ")
    if FoR == '1':
        print('Decryption selected\n')
        break
    elif FoR == '2':
        print('Encryption selected.\n')
        break
    elif (FoR == 'exit'):
        exit()
    else:
        print("Invalid input, please try again.\n")

# Defines type of cipher to use based on user input
while True:
    t = input("Type:\n1> Gwynnstitution \n2> A0Z25\n3> A1Z26\n4> Kaminstitution\n> ")
    if t == '1':
        cipher = gwynn
        print('Gwynnstitution selected.\n')
        break
    elif t == '2':
        cipher = a0z
        print('A0Z25 selected.\n')
        break
    elif t == '3':
        cipher = a1z
        print('A1Z26 selected.\n')
        break
    elif t == '4':
        cipher = kam
        print('Kaminstitution selected.\n')
        break
    elif (t == 'exit'):
        exit()
    else:
        print("Invalid input, please try again.\n")

if FoR == '1' and t != '4':
    # Sanitized input for the numbers to decipher
    while True:
        Input = input("Please input your numbers, each number should be separated by a single whitespace (' '): ").split(' ')
        incorrect = False
        for i in range(len(Input)):
            if not (Input[i].isdigit()):
                incorrect = True
                print("Invalid input, please try again.\n")
        if not incorrect:        
            for i in range(len(Input)):
                # Checks if the input is within the bounds of the cipher
                if (t == '1' and int(Input[i]) > 25) or (t == '2' and int(Input[i]) > 25) or (t == '3' and (int(Input[i]) > 26) or (int(Input[i]) < 1)) or (int(Input[i]) < 0):
                    incorrect = True
                    print("Invalid input, please try again.\n")
                elif (Input[i] == 'exit'):
                    exit()
                else:
                    incorrect = False
        if not incorrect:
            break

    # Deciphers
    for i in range(len(Input)):
        WoL.append(cipher[int(Input[i]) % 26])

if FoR == '2' and t != '4':
    # Sanitized input for the letters to encrypt
    while True:
        Input = input("Please input your letters, each letter should be separated by a single whitespace (' '): ").split(' ')
        incorrect = False
        for i in range(len(Input)):
            if not (Input[i].isalpha()):
                incorrect = True
                print("Invalid input, please try again.\n")
        if not incorrect:
            for i in range(len(Input)):
                if (Input[i] == 'exit'):
                    exit()
                else:
                    incorrect = False
        if not incorrect:
            break

    while True:
        # Encrypts
        for i in range(len(Input)):
            for j in range(len(cipher)):
                if Input[i].upper() == cipher[j]:
                    WoL.append(j)
        break

# Exclusively for Kaminstitution
if FoR == '1' and t == '4':
    # Sanitized input for the numbers to decipher
    while True:
        input_string = input("Please input your numbers, non-separated: ")
        Input = [input_string[i:i+2] for i in range(0, len(input_string), 2)]
        incorrect = False
        for i in range(len(Input)):
            if not (Input[i].isdigit()):
                incorrect = True
                print("Invalid input, please try again.\n")
        if not incorrect:
            for i in range(len(Input)):
                # Checks if the input is within the bounds of the cipher
                if int(Input[i]) < 0:
                    incorrect = True
                    print("Invalid input, please try again.\n")
                elif (Input[i] == 'exit'):
                    exit()
                else:
                    incorrect = False
        if not incorrect:
            break
    
    # Deciphers
    for i in range(len(Input)):
        ti = list(Input[i])
        WoL.append(cipher[int(ti[0])][(int(ti[1]) - 1)])

# Exclusively for Kaminstitution       
if FoR == '2' and t == '4':
    # Sanitized input for the letters to encrypt
    while True:
        Input = list(input("Please input your letters: "))
        incorrect = False
        for i in range(len(Input)):
            if not (Input[i].isalpha()):
                incorrect = True
                print("Invalid input, please try again.\n")
        if not incorrect:
            for i in range(len(Input)):
                if (Input[i] == 'exit'):
                    exit()
                else:
                    incorrect = False
        if not incorrect:
            break

    # Encrypts
    for i in range(len(Input)):
        for z in range(5):
            if (Input[i]).lower() in cipher[z + 1]:
                WoL.append(''.join([str(z + 1), str((cipher[z + 1].index(Input[i].lower())) + 1)]))

print(''.join(WoL))
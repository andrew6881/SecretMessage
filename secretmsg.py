"""

Create a secret message encoder.

Each time the program is run, the user is prompted to select whether they are the sender or receiver of a secret message. Depending on their selection, their actions will be as follows:

Sender: They will type a secret message (in english) and the output will be the encoded message.

Receiver: They will be prompted to enter an encoded message and the output will be the english translation.

"""

# make a custom alphabet to transmit encoded message

# put alphabet in list

# prompt user whether they want to send/decode
# if send:
#   prompt what the message wants to be
#   send confirmation message
#   print original message and encoded message
# if decode:
#   prompt what the user wants to decode
#   decode message
#   print out encoded message and decoded message

# ------------------------------------------------------------ encoded character dictionary

encodedcharacters = {
    "a" : "____",
    "b" : "_._-",
    "c" : ".-__",
    "d" : "..--",
    "e" : "..._",
    "f" : "--_.",
    "g" : "._--",
    "h" : "__._",
    "i" : "-...",
    "j" : ".-_.",
    "k" : "---_",
    "l" : "_.--",
    "m" : ".-..",
    "n" : "--__",
    "o" : "-.-.",
    "p" : "....",
    "q" : "-_.-",
    "r" : "_.._",
    "s" : "_-._",
    "t" : "._.-",
    "u" : "_-__",
    "v" : ".._.",
    "w" : "-__.",
    "x" : ".-_-",
    "y" : "...-",
    "z" : "_--.",
    "0" : "-_||",
    "1" : "||||",
    "2" : "|.|.",
    "3" : "|..|",
    "4" : "||..",
    "5" : "|||.",
    "6" : "|.||",
    "7" : ".-|.",
    "8" : "-|--",
    "9" : "|||-",
    " " : "_-.."
}

decodingkeys = (list(encodedcharacters.keys()))
decodingvalues = (list(encodedcharacters.values()))

# ------------------------------------------------------------

# prompt user whether they want to send/decode
# if send:
#   prompt what the message wants to be
#   send confirmation message
#   print original message and encoded message
# if decode:
#   prompt what the user wants to decode
#   decode message
#   print out encoded message and decoded message

rstring = ""
listtodecode = []
 
while True:
    choice = int(input("What would you like to do? \n Enter '1' if you want to encode a message \n Enter '2' if you want to decode a message "))
    if choice == 1: # to send message
        msg = input("Please input your message in English characters. Only use the letters A-Z and numbers 0-9: ")
        for i in range(len(msg)):
            rstring += (encodedcharacters[msg[i]])
        print("Original message: " + msg)
        print("Encoded message: " + rstring)
        break

    elif choice == 2: # to decode message
        msg = input("Enter your encoded message to be decoded here: ")
        listtodecode = [msg[i:i+4] for i in range(0, len(msg), 4)]
        for i in range(len(listtodecode)):
            position = decodingvalues.index(listtodecode[i])
            rstring += decodingkeys[position]
        print(rstring)
        break
        
    else:
        print("Please pick either 1 or 2")
        print("---------------------------")
    

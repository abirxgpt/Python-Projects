import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '?', '/', ':', ';']

print(art.logo)

directionx = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
textx = input("Type your message:\n").lower()
shiftx = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    edited_text = ''
    if direction == "decode":
        shift *= -1
    for j in text:
        if j == " ":
            edited_text += " "
        elif j in numbers:
            j = int(j)
            j += shift
            j = str(j)
            edited_text += j
        elif j in symbols:
            edited_text += j
        else:
            step = alphabet.index(j)
            step = step + shift
            if step > 25 or step < 0:
                step = step % 26
            edited_text += alphabet[step]
        
    print(f"the {direction}d Text is :{edited_text}")

caesar(text=textx,shift=shiftx,direction=directionx)



# Previous code did more Refinement
# def encrypt(text, shift):

#     cipher_text = ''
#     for j in text:
#         if j == " ":
#             j = " "
#             cipher_text += " "
#         else:
#             step = alphabet.index(j)
#             step = step + shift
#             if step > 25:
#                 step = step % 26
#         cipher_text += alphabet[step]
#     print(f"the Encoded Text is :{cipher_text}")

# def decrypt(text, shift):

#     decoded_text = ''
#     for j in text:
#         if j == " ":
#             j = " "
#             decoded_text += " "
#         else:
#             step = alphabet.index(j)
#             step = step - shift
#             if step < 0:
#                 step = step % 26
#             decoded_text += alphabet[step]
#     print(f"the Decoded Text is :{decoded_text}")

# if direction == "encode":
#     encrypt(text=text1 ,shift=shift1)
# else:
#     decrypt(text=text1 ,shift=shift1

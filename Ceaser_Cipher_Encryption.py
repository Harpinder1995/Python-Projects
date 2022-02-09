logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
Should_continue = True
while Should_continue:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z']

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  try:
    shift = int(input("Type the shift number:\n"))



    response = ""

    def caeser(plain_text,shift_amount,direction):
            cipher_text = ""
            if shift_amount>26:
              shift_amount = shift_amount %26
            for letter in plain_text:
              if letter in alphabet:
                position = alphabet.index(letter)
                if direction == "encode":
                  new_position = position + shift_amount
                elif direction == "decode":
                  new_position = position - shift_amount
                cipher_text += alphabet[new_position]
              else:
                cipher_text += letter
            print(f"The {direction}d text is {cipher_text}")



    caeser(text, shift, direction)
    response = input("Type 'yes' if you continue want to use this program OR type 'no' to Exit")
    if response == "no":
      Should_continue = False
    elif response == "yes":
      Should_continue = True
    else:
      print("Please Enter Correct Option..!")
  except:
    print("Please Enter Correct Shift Value")

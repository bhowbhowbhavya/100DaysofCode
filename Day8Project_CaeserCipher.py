alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(plain_text, shift_amount, direction_parameter):
    cipher_text=""
    if direction_parameter == "encode":
        for i in plain_text:
           if i in alphabet: 
                position = alphabet.index(i)
                new_position = shift_amount+position
                if new_position<=25:
                    cipher_text += alphabet[new_position] 
                else:
                    value = new_position - 26
                    cipher_text += alphabet[value]
        print(f"The encoded text is {cipher_text}") 
    if direction_parameter == "decode":
        for i in plain_text:
            if i in alphabet:
                position = alphabet.index(i)
                new_position = position - shift_amount
                if new_position>=0:
                    cipher_text += alphabet[new_position] 
                else:
                    value =  new_position + 26
                    cipher_text += alphabet[value]
        print(f"The decoded text is {cipher_text}")
  
should_continue = True     
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    caeser(plain_text = text, shift_amount = shift, direction_parameter = direction)
    result = input("Type 'yes' if you want to go again. Otherwise 'no'")
    if result == "no":
        print("Goodbye!")
        should_continue = False
    
    
caeser(plain_text=text,shift_amount=shift,direction_parameter=direction)
    
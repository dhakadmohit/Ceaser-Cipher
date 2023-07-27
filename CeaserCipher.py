import prerequsiteforCeaserCipher
print(prerequsiteforCeaserCipher.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceasar(plain_text, shift_amount, n_direction):
    cipher_text = ""
    if (n_direction == 'decode'):
        shift_amount *= -1
    for letter in plain_text:
          if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
          else:
              cipher_text += letter
    print(f"{cipher_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if int(shift) > 26:
     shift = shift % 26
    ceasar(plain_text=text, shift_amount=shift, n_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwis type 'no'\n")
    if result == 'no':
         should_continue = False
         print("Goodbye!!")
text = 'Cipher Caesar'
shift = 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_text = '' 
i = 0  

# Boucle 
while i < len(text):
    char = text[i]  # le caractere actuel

    if char.lower() in alphabet:  # Si c'est une lettre

        # Trouve l'index et decale avec alphabet.index()
        shifted_char = alphabet[(alphabet.index(char.lower()) + shift) % len(alphabet)]

        # Respect de la casse
        if char.isupper():
            shifted_text += shifted_char.upper()
        else:
            shifted_text += shifted_char
    else:
        # Si c'est pas une lettre
        shifted_text += char
    i += 1  # Alors on passe au caractère suivant

print(shifted_text)
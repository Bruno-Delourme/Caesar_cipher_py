def caesar_cipher(text, shift, decrypt=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_text = ''
    
    if decrypt:
        shift = -shift
    
    for char in text:
        if char.lower() in alphabet:
            shifted_char = alphabet[(alphabet.index(char.lower()) + shift) % len(alphabet)]
            shifted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            shifted_text += char
            
    return shifted_text

texte = 'Cipher Caesar'
texte_chiffre = caesar_cipher(texte, 1)
print(f"Texte chiffré: {texte_chiffre}")
texte_dechiffre = caesar_cipher(texte_chiffre, 1, decrypt=True)
print(f"Texte déchiffré: {texte_dechiffre}")
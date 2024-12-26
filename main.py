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

def keyword_cipher(text, keyword, decrypt=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword = ''.join(dict.fromkeys(keyword.lower()))
    cipher_alphabet = keyword + ''.join(c for c in alphabet if c not in keyword)
    
    result = ''
    for char in text:
        if char.lower() in alphabet:
            if decrypt:
                idx = cipher_alphabet.index(char.lower())
                new_char = alphabet[idx]
            else:
                idx = alphabet.index(char.lower())
                new_char = cipher_alphabet[idx]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

texte = 'Cipher Caesar'
texte_chiffre = caesar_cipher(texte, 1)
print(f"Texte chiffré (César): {texte_chiffre}")
texte_dechiffre = caesar_cipher(texte_chiffre, 1, decrypt=True)
print(f"Texte déchiffré (César): {texte_dechiffre}")

mot_cle = "SECRET"
texte_chiffre_mc = keyword_cipher(texte, mot_cle)
print(f"Texte chiffré (mot-clé): {texte_chiffre_mc}")
texte_dechiffre_mc = keyword_cipher(texte_chiffre_mc, mot_cle, decrypt=True)
print(f"Texte déchiffré (mot-clé): {texte_dechiffre_mc}")
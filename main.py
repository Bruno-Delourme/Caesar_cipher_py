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

def menu():
    while True:
        print("\n=== Menu de Chiffrement ===")
        print("1. Chiffrement César")
        print("2. Chiffrement par mot-clé")
        print("3. Quitter")
        
        choix = input("\nChoisissez une option (1-3): ")
        
        if choix == "3":
            print("Au revoir!")
            break
            
        texte = input("Entrez le texte à traiter: ")
        
        if choix == "1":
            try:
                decalage = int(input("Entrez le décalage (nombre entier): "))
                action = input("Chiffrer (C) ou Déchiffrer (D)? ").upper()
                
                if action == "C":
                    resultat = caesar_cipher(texte, decalage)
                elif action == "D":
                    resultat = caesar_cipher(texte, decalage, decrypt=True)
                else:
                    print("Action non valide!")
                    continue
                    
                print(f"\nRésultat: {resultat}")
                
            except ValueError:
                print("Erreur: Le décalage doit être un nombre entier!")
                
        elif choix == "2":
            mot_cle = input("Entrez le mot-clé: ")
            action = input("Chiffrer (C) ou Déchiffrer (D)? ").upper()
            
            if action == "C":
                resultat = keyword_cipher(texte, mot_cle)
            elif action == "D":
                resultat = keyword_cipher(texte, mot_cle, decrypt=True)
            else:
                print("Action non valide!")
                continue
                
            print(f"\nRésultat: {resultat}")
            
        else:
            print("Option non valide!")

if __name__ == "__main__":
    menu()
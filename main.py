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

def save_history(text, result, method, action):
    with open('historique.txt', 'a', encoding='utf-8') as f:
        f.write(f"{method} - {action}: '{text}' → '{result}'\n")

def menu():
    while True:
        print("\n=== Menu de Chiffrement ===")
        print("1. Chiffrement César")
        print("2. Chiffrement par mot-clé")
        print("3. Voir l'historique")
        print("4. Effacer l'historique")
        print("5. Quitter")
        
        choix = input("\nChoisissez une option (1-5): ")
        
        if choix == "5":
            print("Au revoir!")
            break
            
        if choix == "3":
            try:
                with open('historique.txt', 'r', encoding='utf-8') as f:
                    historique = f.read()
                    print("\n=== Historique des chiffrements ===")
                    print(historique if historique else "Aucun historique disponible")
                continue
            except FileNotFoundError:
                print("Aucun historique disponible")
                continue
                
        if choix == "4":
            try:
                with open('historique.txt', 'w', encoding='utf-8') as f:
                    f.write("")
                print("L'historique a été effacé avec succès!")
            except:
                print("Erreur lors de l'effacement de l'historique")
            continue
                
        texte = input("Entrez le texte à traiter: ")
        
        if choix == "1":
            try:
                decalage = int(input("Entrez le décalage (nombre entier): "))
                action = input("Chiffrer (C) ou Déchiffrer (D)? ").upper()
                
                if action == "C":
                    resultat = caesar_cipher(texte, decalage)
                    save_history(texte, resultat, "César", "Chiffrement")
                elif action == "D":
                    resultat = caesar_cipher(texte, decalage, decrypt=True)
                    save_history(texte, resultat, "César", "Déchiffrement")
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
                save_history(texte, resultat, f"Mot-clé ({mot_cle})", "Chiffrement")
            elif action == "D":
                resultat = keyword_cipher(texte, mot_cle, decrypt=True)
                save_history(texte, resultat, f"Mot-clé ({mot_cle})", "Déchiffrement")
            else:
                print("Action non valide!")
                continue
                
            print(f"\nRésultat: {resultat}")
            
        else:
            print("Option non valide!")

if __name__ == "__main__":
    menu()
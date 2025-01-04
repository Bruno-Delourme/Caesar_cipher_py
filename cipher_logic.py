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
    with open('history.txt', 'a', encoding='utf-8') as f:
        f.write(f"{method} - {action}: '{text}' → '{result}'\n")

def display_cipher_alphabet(method, shift=None, keyword=None):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if method == "caesar":
        cipher_alphabet = ''.join(alphabet[(i + shift) % 26] for i in range(26))
    elif method == "keyword":
        keyword = ''.join(dict.fromkeys(keyword.lower()))
        cipher_alphabet = keyword + ''.join(c for c in alphabet if c not in keyword)
    
    print("\nAlphabet correspondence:")
    print("Original:", ' '.join(alphabet))
    print("Cipher  :", ' '.join(cipher_alphabet))
    print()

def menu():
    while True:
        print("\n=== Encryption Menu ===")
        print("1. Caesar Cipher")
        print("2. Keyword Cipher")
        print("3. View History")
        print("4. Clear History")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "5":
            print("Goodbye!")
            break
            
        if choice == "3":
            try:
                with open('history.txt', 'r', encoding='utf-8') as f:
                    history = f.read()
                    print("\n=== Encryption History ===")
                    print(history if history else "No history available")
                continue
            except FileNotFoundError:
                print("No history available")
                continue
                
        if choice == "4":
            try:
                with open('history.txt', 'w', encoding='utf-8') as f:
                    f.write("")
                print("History cleared successfully!")
            except:
                print("Error while clearing history")
            continue
                
        text = input("Enter text to process: ")
        
        if choice == "1":
            try:
                shift = int(input("Enter shift value (integer): "))
                display_cipher_alphabet("caesar", shift=shift)
                action = input("Encrypt (E) or Decrypt (D)? ").upper()
                
                if action == "E":
                    result = caesar_cipher(text, shift)
                    save_history(text, result, "Caesar", "Encryption")
                elif action == "D":
                    result = caesar_cipher(text, shift, decrypt=True)
                    save_history(text, result, "Caesar", "Decryption")
                else:
                    print("Invalid action!")
                    continue
                    
                print(f"\nResult: {result}")
                
            except ValueError:
                print("Error: Shift must be an integer!")
                
        elif choice == "2":
            keyword = input("Enter keyword: ")
            display_cipher_alphabet("keyword", keyword=keyword)
            action = input("Encrypt (E) or Decrypt (D)? ").upper()
            
            if action == "E":
                result = keyword_cipher(text, keyword)
                save_history(text, result, f"Keyword ({keyword})", "Encryption")
            elif action == "D":
                result = keyword_cipher(text, keyword, decrypt=True)
                save_history(text, result, f"Keyword ({keyword})", "Decryption")
            else:
                print("Invalid action!")
                continue
                
            print(f"\nResult: {result}")
            
        else:
            print("Invalid option!")

if __name__ == "__main__":
    menu()
import tkinter as tk
from tkinter import ttk, messagebox
from styles import STYLES, COLORS, WIDGET_CONFIG
from cipher_logic import caesar_cipher, keyword_cipher, display_cipher_alphabet
from theme import ThemeManager

class CipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(WIDGET_CONFIG['main_window']['title'])
        self.root.configure(bg=COLORS['bg_main'])
        
        # Initialisation du gestionnaire de thème
        self.theme_manager = ThemeManager(root)
        
        self.result_var = tk.StringVar()
        self.setup_gui()
        
    def setup_gui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, **STYLES['frame'])
        main_frame.pack(expand=True, fill='both')
        
        # Zone de saisie avec bouton Clear
        input_frame = tk.Frame(main_frame, bg=COLORS['bg_main'])
        input_frame.pack()
        
        tk.Label(input_frame, text="Text to process:", **STYLES['label']).pack()
        
        # Frame pour le texte et son bouton Clear
        text_clear_frame = tk.Frame(input_frame, bg=COLORS['bg_main'])
        text_clear_frame.pack()
        
        self.text_input = tk.Entry(text_clear_frame, **STYLES['entry'])
        self.text_input.pack(side=tk.LEFT, pady=5)
        
        clear_text_btn = self.theme_manager.create_button(
            text_clear_frame, 
            "Clear", 
            self.clear_fields
        )
        clear_text_btn.pack(side=tk.LEFT, padx=5)
        
        # Sélection de la méthode avec boutons d'aide
        method_frame = tk.Frame(main_frame, **WIDGET_CONFIG['radio_frame'])
        method_frame.pack()
        
        method_title_frame = tk.Frame(method_frame, bg=COLORS['bg_main'])
        method_title_frame.pack()
        
        self.cipher_method = tk.StringVar(value="caesar")
        
        # Groupe des radio boutons et boutons d'aide
        radio_help_frame = tk.Frame(method_frame, bg=COLORS['bg_main'])
        radio_help_frame.pack()
        
        # César avec son bouton d'aide
        cesar_frame = tk.Frame(radio_help_frame, bg=COLORS['bg_main'])
        cesar_frame.pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(cesar_frame, text="Caesar", variable=self.cipher_method, 
                      value="caesar", **STYLES['radio']).pack(side=tk.LEFT)
        tk.Button(cesar_frame, text="?", 
                 command=lambda: self.show_help("caesar"), **STYLES['help_button']).pack(side=tk.LEFT, padx=2)
        
        # Mot-clé avec son bouton d'aide
        keyword_frame = tk.Frame(radio_help_frame, bg=COLORS['bg_main'])
        keyword_frame.pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(keyword_frame, text="Keyword", variable=self.cipher_method, 
                      value="keyword", **STYLES['radio']).pack(side=tk.LEFT)
        tk.Button(keyword_frame, text="?", 
                 command=lambda: self.show_help("keyword"), **STYLES['help_button']).pack(side=tk.LEFT, padx=2)
        
        # Paramètres
        self.param_frame = tk.Frame(main_frame, **WIDGET_CONFIG['param_frame'])
        self.param_frame.pack()
        
        self.param_label = tk.Label(self.param_frame, text="Shift:", **STYLES['label'])
        self.param_label.pack(side=tk.LEFT)
        
        self.param_entry = tk.Entry(self.param_frame, **STYLES['entry_small'])
        self.param_entry.pack(side=tk.LEFT, padx=5)
        
        # Boutons d'action
        button_frame = tk.Frame(main_frame, **WIDGET_CONFIG['button_frame'])
        button_frame.pack()
        
        self.theme_manager.create_button(
            button_frame, 
            "Encrypt", 
            lambda: self.process_text(False)
        ).pack(side=tk.LEFT, padx=5)
        
        self.theme_manager.create_button(
            button_frame, 
            "Decrypt", 
            lambda: self.process_text(True)
        ).pack(side=tk.LEFT, padx=5)
        
        # Résultat et bouton copier
        result_frame = tk.Frame(main_frame, **WIDGET_CONFIG['result_frame'])
        result_frame.pack()
        
        tk.Label(result_frame, textvariable=self.result_var, **STYLES['result']).pack(side=tk.LEFT)
        
        # Bouton copier
        self.copy_button = self.theme_manager.create_button(
            result_frame, 
            "📋 Copy", 
            self.copy_result
        )
        self.copy_button.pack(side=tk.LEFT, padx=5)
        self.copy_button['state'] = 'disabled'
        
        # Binding des événements
        self.cipher_method.trace('w', self.update_param_label)
        
    def update_param_label(self, *args):
        if self.cipher_method.get() == "caesar":
            self.param_label.config(text="Shift:")
        else:
            self.param_label.config(text="Keyword:")
            
    def copy_result(self):
        """Copie uniquement le texte chiffré/déchiffré sans le préfixe 'Résultat: '"""
        result_text = self.result_var.get()
        # Enlève le préfixe "Résultat: " s'il existe
        if result_text.startswith("Résultat: "):
            result_text = result_text[9:]  # Longueur de "Résultat: "
            
        self.root.clipboard_clear()
        self.root.clipboard_append(result_text)
        self.root.update()  # nécessaire pour certains systèmes
        
        # Feedback visuel temporaire
        original_text = self.copy_button['text']
        self.copy_button['text'] = "✓ Copied!"
        self.root.after(1500, lambda: self.copy_button.configure(text=original_text))
        
    def process_text(self, decrypt=False):
        text = self.text_input.get()
        method = self.cipher_method.get()
        param = self.param_entry.get()
        
        try:
            if method == "caesar":
                shift = int(param)
                result = caesar_cipher(text, shift, decrypt)
            else:
                if not param.strip():
                    messagebox.showerror("Error", "Keyword cannot be empty!")
                    return
                result = keyword_cipher(text, param, decrypt)
                
            self.result_var.set(f"Result: {result}")
            self.copy_button['state'] = 'normal'
            
        except ValueError as e:
            messagebox.showerror("Error", "Invalid parameter!")
            self.copy_button['state'] = 'disabled'
        
    def show_help(self, method_type):
        """Affiche une fenêtre d'aide avec des exemples concis"""
        help_window = tk.Toplevel(self.root)
        help_window.title("Help - Encryption")
        help_window.configure(bg=COLORS['bg_main'])
        
        frame = tk.Frame(help_window, **STYLES['help_window'])
        frame.pack(expand=True, fill='both')
        
        if method_type == "caesar":
            title = "Caesar Cipher"
            text = """Shifts each letter in the alphabet by a fixed number of positions.

Example with shift of 3:
HELLO → KHOOR
(H+3=K, E+3=H, L+3=O, etc.)

Example with shift of 1:
HELLO → IFMMP
(H+1=I, E+1=F, L+1=M, etc.)"""

        else:
            title = "Keyword Cipher"
            text = """Creates a custom alphabet using a keyword.

Example with keyword "SECRET":
New alphabet: SECRETABDFGHIJKLMNOPQUVWXYZ
HELLO → KBPPJ

Example with keyword "KEY":
New alphabet: KEYABCDFGHIJLMNOPQRSTUVWXZ
HELLO → KBPPJ"""
        
        tk.Label(frame, text=title, font=(STYLES['help_text']['font'][0], 13, 'bold'),
                bg=COLORS['bg_main'], fg=COLORS['text']).pack(pady=(0, 10))
        
        tk.Label(frame, text=text, **STYLES['help_text']).pack()
        
        tk.Button(frame, text="Close", command=help_window.destroy,
                 **STYLES['button']).pack(pady=(15, 0))
        
        # Centrer la fenêtre
        help_window.update_idletasks()
        width = help_window.winfo_width()
        height = help_window.winfo_height()
        x = (help_window.winfo_screenwidth() // 2) - (width // 2)
        y = (help_window.winfo_screenheight() // 2) - (height // 2)
        help_window.geometry(f'{width}x{height}+{x}+{y}')
        
        # Rendre la fenêtre modale
        help_window.transient(self.root)
        help_window.grab_set()
        self.root.wait_window(help_window) 

    def clear_fields(self):
        """Réinitialise tous les champs"""
        self.text_input.delete(0, tk.END)
        self.param_entry.delete(0, tk.END)
        self.result_var.set("")
        self.copy_button['state'] = 'disabled' 
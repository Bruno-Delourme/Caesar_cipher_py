import tkinter as tk
from tkinter import ttk
from styles import STYLES, COLORS

class ThemeManager:
    def __init__(self, root):
        self.root = root
        self.setup_theme()
    
    def setup_theme(self):
        # Configuration du style de base
        style = ttk.Style()
        style.theme_use('clam')  # Utilisation du thème 'clam' pour un look moderne
        
        # Style personnalisé pour les boutons
        style.configure(
            'Custom.TButton',
            background=COLORS['accent'],
            foreground='white',
            padding=(15, 8),
            font=STYLES['button']['font'],
            borderwidth=0,
            relief='flat'
        )
        
        # Style pour le survol des boutons
        style.map(
            'Custom.TButton',
            background=[('active', self._adjust_color(COLORS['accent'], -20))],
            relief=[('active', 'flat')]
        )
        
        # Style pour les boutons désactivés
        style.map(
            'Custom.TButton',
            background=[('disabled', '#cccccc')],
            foreground=[('disabled', '#666666')]
        )
        
        # Configuration des coins arrondis via un canvas personnalisé
        self.setup_rounded_button_style()
    
    def setup_rounded_button_style(self):
        class RoundedButton(tk.Canvas):
            def __init__(self, parent, width, height, cornerradius, padding, color, command=None, text='', **kwargs):
                tk.Canvas.__init__(self, parent, borderwidth=0, 
                                 relief="flat", highlightthickness=0, bg=COLORS['bg_main'])
                self.command = command
                
                if cornerradius > 0.5*width:
                    cornerradius = 0.5*width
                if cornerradius > 0.5*height:
                    cornerradius = 0.5*height

                # Création du fond arrondi
                self.rect = self.create_rounded_rect(padding, padding, 
                                                   width-padding, height-padding, 
                                                   cornerradius, fill=color)
                
                # Ajout du texte
                self.text = self.create_text(width/2, height/2, text=text, 
                                           fill='white', font=STYLES['button']['font'])
                
                self.bind('<Button-1>', self._on_click)
                self.bind('<Enter>', lambda e: self._on_enter(e, color))
                self.bind('<Leave>', lambda e: self._on_leave(e, color))
                
                # Définition de la taille du widget
                self.configure(width=width, height=height)
            
            def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
                points = [x1+radius, y1,
                         x2-radius, y1,
                         x2, y1,
                         x2, y1+radius,
                         x2, y2-radius,
                         x2, y2,
                         x2-radius, y2,
                         x1+radius, y2,
                         x1, y2,
                         x1, y2-radius,
                         x1, y1+radius,
                         x1, y1]
                return self.create_polygon(points, **kwargs, smooth=True)
            
            def _on_click(self, event):
                if self.command:
                    self.command()
            
            def _on_enter(self, event, color):
                self.itemconfig(self.rect, fill=self._adjust_color(color, -20))
            
            def _on_leave(self, event, color):
                self.itemconfig(self.rect, fill=color)
            
            def _adjust_color(self, color, amount):
                # Assombrir ou éclaircir la couleur
                r = int(color[1:3], 16) + amount
                g = int(color[3:5], 16) + amount
                b = int(color[5:7], 16) + amount
                r = min(max(0, r), 255)
                g = min(max(0, g), 255)
                b = min(max(0, b), 255)
                return f'#{r:02x}{g:02x}{b:02x}'
        
        self.RoundedButton = RoundedButton
    
    def _adjust_color(self, color, amount):
        # Assombrir ou éclaircir la couleur
        r = int(color[1:3], 16) + amount
        g = int(color[3:5], 16) + amount
        b = int(color[5:7], 16) + amount
        r = min(max(0, r), 255)
        g = min(max(0, g), 255)
        b = min(max(0, b), 255)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def create_rounded_button(self, parent, text, command, width=120, height=35):
        return self.RoundedButton(
            parent, 
            width=width, 
            height=height, 
            cornerradius=17,
            padding=2,
            color=COLORS['accent'],
            command=command,
            text=text
        ) 
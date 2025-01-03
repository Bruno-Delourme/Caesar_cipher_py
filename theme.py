import tkinter as tk
from styles import STYLES, COLORS

class ThemeManager:
    def __init__(self, root):
        self.root = root
    
    def create_button(self, parent, text, command):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            **STYLES['button']
        )
        
        def on_enter(e):
            button['background'] = self._adjust_color(COLORS['accent'], -20)

        def on_leave(e):
            button['background'] = COLORS['accent']

        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        return button

    def _adjust_color(self, color, amount):
        r = int(color[1:3], 16) + amount
        g = int(color[3:5], 16) + amount
        b = int(color[5:7], 16) + amount
        r = min(max(0, r), 255)
        g = min(max(0, g), 255)
        b = min(max(0, b), 255)
        return f'#{r:02x}{g:02x}{b:02x}' 
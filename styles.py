import tkinter.font as tkfont
import os

# Définition de la police par défaut
FONT_FAMILY = 'Helvetica'  # Police par défaut

# Couleurs
COLORS = {
    'bg_main': '#f0f0f0',
    'bg_input': '#ffffff',
    'accent': '#007bff',
    'text': '#333333',
    'error': '#dc3545'
}

# Configuration des widgets
WIDGET_CONFIG = {
    'main_window': {
        'title': "Chiffrement de texte",
        'bg': COLORS['bg_main']
    },
    'radio_frame': {
        'bg': COLORS['bg_main'],
        'pady': 10
    },
    'param_frame': {
        'bg': COLORS['bg_main'],
        'pady': 5
    },
    'button_frame': {
        'bg': COLORS['bg_main'],
        'pady': 10
    },
    'result_frame': {
        'bg': COLORS['bg_main'],
        'pady': 10
    }
}

# Styles des widgets
STYLES = {
    'frame': {
        'bg': COLORS['bg_main'],
        'padx': 30,
        'pady': 25
    },
    'label': {
        'font': ('Helvetica', 11),
        'bg': COLORS['bg_main'],
        'fg': COLORS['text'],
        'pady': 8
    },
    'entry': {
        'font': ('Helvetica', 11),
        'bg': COLORS['bg_input'],
        'relief': 'solid',
        'borderwidth': 1,
        'width': 50
    },
    'entry_small': {
        'font': ('Helvetica', 11),
        'bg': COLORS['bg_input'],
        'relief': 'solid',
        'borderwidth': 1,
        'width': 15
    },
    'button': {
        'font': ('Helvetica', 10),
        'bg': COLORS['accent'],
        'fg': 'white',
        'pady': 8,
        'padx': 15,
        'relief': 'flat',
        'cursor': 'hand2'
    },
    'result': {
        'font': ('Helvetica', 12, 'bold'),
        'bg': COLORS['bg_main'],
        'fg': COLORS['text'],
        'pady': 15
    },
    'radio': {
        'bg': COLORS['bg_main'],
        'font': ('Helvetica', 10),
        'padx': 5
    },
    'help_button': {
        'font': ('Helvetica', 10, 'bold'),
        'bg': COLORS['bg_main'],
        'fg': COLORS['accent'],
        'pady': 2,
        'padx': 6,
        'relief': 'flat',
        'cursor': 'hand2',
        'borderwidth': 1,
        'width': 2,
        'height': 1
    },
    'help_window': {
        'bg': COLORS['bg_main'],
        'padx': 20,
        'pady': 20
    },
    'help_text': {
        'font': ('Helvetica', 11),
        'bg': COLORS['bg_main'],
        'fg': COLORS['text'],
        'pady': 5,
        'justify': 'left',
        'wraplength': 400
    }
} 
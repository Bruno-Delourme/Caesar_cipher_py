import tkinter.font as tkfont
import os

# Définition de la police par défaut
FONT_FAMILY = 'Segoe UI'  # Plus moderne que Helvetica, bien supportée sur Windows/Mac/Linux

# Couleurs
COLORS = {
    'bg_main': '#f8f9fa',      # Gris très clair, plus doux
    'bg_input': '#ffffff',
    'accent': '#4361ee',       # Bleu plus moderne
    'text': '#2b2d42',         # Gris foncé plus doux
    'error': '#ef233c',
    'hover': '#3046c5'         # Couleur pour les effets hover
}

# Configuration des widgets
WIDGET_CONFIG = {
    'main_window': {
        'title': "Text Encryption",
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
        'padx': 35,            # Padding légèrement augmenté
        'pady': 30
    },
    'label': {
        'font': (FONT_FAMILY, 11),
        'bg': COLORS['bg_main'],
        'fg': COLORS['text'],
        'pady': 10
    },
    'entry': {
        'font': (FONT_FAMILY, 11),
        'bg': COLORS['bg_input'],
        'relief': 'flat',      # Bordure plate plus moderne
        'borderwidth': 0,
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
        'font': (FONT_FAMILY, 10, 'bold'),  # Texte en gras
        'bg': COLORS['accent'],
        'fg': 'white',
        'pady': 10,            # Padding augmenté
        'padx': 20,
        'relief': 'flat',
        'cursor': 'hand2',
        'borderwidth': 0,      # Pas de bordure
        'highlightthickness': 0  # Supprime la bordure de focus
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
        'font': (FONT_FAMILY, 10, 'bold'),
        'bg': COLORS['bg_main'],
        'fg': COLORS['accent'],
        'pady': 4,
        'padx': 8,
        'relief': 'flat',
        'cursor': 'hand2',
        'borderwidth': 0,
        'width': 2,
        'height': 1,
        'highlightthickness': 0
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
    },
    'animation_letter': {
        'font': ('Helvetica', 12, 'bold'),
        'bg': COLORS['bg_main'],
        'fg': COLORS['text'],
        'pady': 5,
        'relief': 'flat'
    },
    'animation_active': {
        'font': ('Helvetica', 12, 'bold'),
        'bg': COLORS['accent'],
        'fg': 'white',
        'pady': 5,
        'relief': 'flat'
    },
    'animation_frame': {
        'bg': COLORS['bg_main'],
        'pady': 10
    },
    'original_letter': {
        'width': 2,
        'bg': COLORS['bg_main'],
        'font': ('Helvetica', 12, 'bold'),
        'padx': 1
    },
    'cipher_letter': {
        'width': 2,
        'bg': COLORS['bg_main'],
        'font': ('Helvetica', 12, 'bold'),
        'padx': 1
    },
    'arrow': {
        'font': ('Helvetica', 20),
        'bg': COLORS['bg_main'],
        'pady': 5
    },
    'highlighted_letter': {
        'bg': COLORS['accent'],
        'fg': 'white'
    }
} 
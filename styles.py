import tkinter.font as tkfont

# Définition de la police par défaut
FONT_FAMILY = 'Helvetica'

# Couleurs
COLORS = {
    'bg_main': '#f8f9fa',
    'bg_input': '#ffffff',
    'accent': '#4361ee',
    'text': '#2b2d42',
    'error': '#ef233c'
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
    'result': {
        'font': ('Helvetica', 12, 'bold'),
        'bg': COLORS['bg_main'],
        'fg': COLORS['text'],
        'pady': 15
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
    }
} 
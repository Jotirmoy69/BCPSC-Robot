# utils.py
conversation_memory = []

def is_bangla(text):
    """Detect if text contains Bangla characters"""
    for c in text:
        if '\u0980' <= c <= '\u09FF':
            return True
    return False

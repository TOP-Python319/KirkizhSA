
import string
import re

def strong_password(password: str) -> bool:
    
    if len(password) < 8:
        return False
    
    # Присутствие буквенных символов в обоих регистрах
    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        return False
    
    # Присутствие минимум двух символов цифр
    if not sum(c.isdigit() for c in password) >= 2:
        return False
    
    # Присутствие символов прочих категорий
    if not any(c in string.punctuation or c in string.whitespace for c in password):
        return False
    
    return True
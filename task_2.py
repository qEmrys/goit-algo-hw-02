from collections import deque


def is_polyndrome(s: str) -> bool:
    cleaned_s = ''.join(filter(str.isalnum, s)).lower()
    char_deque = deque(cleaned_s)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
            
    return True

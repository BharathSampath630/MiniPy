import re

# -------------------------
# Token Specification
# -------------------------
TOKEN_SPEC = [
    ("NUMBER",   r'\d+(\.\d+)?'),           # Integer or float
    ("STRING",   r'"[^"]*"'),               # String literals
    ("IDENT",    r'[A-Za-z_][A-Za-z0-9_]*'), # Identifiers
    ("PLUS",     r'\+'),
    ("MINUS",    r'-'),
    ("MUL",      r'\*'),
    ("DIV",      r'/'),
    ("INTDIV",   r'//'),
    ("EQ",       r'='),
    ("LPAREN",   r'\('),
    ("RPAREN",   r'\)'),
    ("COLON",    r':'),
    ("COMMA",    r','),                     # Added comma for function parameters
    ("NEWLINE",  r'\n'),
    ("SKIP",     r'[ \t]+'),                # Spaces/tabs
    ("MISMATCH", r'.'),                     # Any other character
]

# -------------------------
# Keywords
# -------------------------
KEYWORDS = {"let", "print", "if", "else", "while", "def", "return"}

# -------------------------
# Token Class
# -------------------------
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"{self.type}({self.value})"

# -------------------------
# Lexer Function
# -------------------------
def lexer(code):
    tokens = []
    pattern = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPEC)
    regex = re.compile(pattern)
    
    for match in regex.finditer(code):
        kind = match.lastgroup
        value = match.group()
        
        if kind == "IDENT" and value in KEYWORDS:
            kind = value.upper()       # convert keywords to token type
        elif kind == "SKIP":
            continue                  # ignore spaces/tabs
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character: {value}")
        
        tokens.append(Token(kind, value))
    
    return tokens

# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    code = '''
let x = 10
let y = 5
print(x + y)

def add(a, b):
    return a + b
'''
    tokens = lexer(code)
    for t in tokens:
        print(t)

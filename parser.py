# -------------------------
# PARSER
# -------------------------
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def advance(self):
        self.pos += 1
    
    def skip_newlines(self):
        while self.current() and self.current().type == "NEWLINE":
            self.advance()
    
    def expect(self, type_):
        token = self.current()
        if not token or token.type != type_:
            raise SyntaxError(f"Expected {type_}, got {token}")
        self.advance()
        return token
    
    def parse_program(self):
        statements = []
        while self.current():
            self.skip_newlines()
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return Program(statements)
    
    def parse_statement(self):
        self.skip_newlines()
        tok = self.current()
        if not tok:
            return None
        
        # Handle ELSE only inside parse_if
        if tok.type == "ELSE":
            return None  # skip at top-level (or will be handled inside parse_if)
        
        if tok.type == "LET":
            return self.parse_assignment()
        elif tok.type == "PRINT":
            return self.parse_print()
        elif tok.type == "IF":
            return self.parse_if()
        elif tok.type == "WHILE":
            return self.parse_while()
        elif tok.type == "FOR":
            return self.parse_for()
        elif tok.type == "DEF":
            return self.parse_func()
        elif tok.type == "RETURN":
            self.advance()
            return Return(self.parse_expression())
        else:
            raise SyntaxError(f"Unknown statement: {tok}")

    
    def parse_assignment(self):
        self.expect("LET")
        var_name = self.expect("IDENT").value
        self.expect("EQ")
        expr = self.parse_expression()
        return Assignment(var_name, expr)
    
    def parse_print(self):
        self.expect("PRINT")
        self.expect("LPAREN")
        expr = self.parse_expression()
        self.expect("RPAREN")
        return Print(expr)

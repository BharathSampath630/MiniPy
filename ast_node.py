# -------------------------
# AST NODES
# -------------------------
class Program:
    def __init__(self, statements):
        self.statements = statements

class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Print:
    def __init__(self, expr):
        self.expr = expr

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Number:
    def __init__(self, value):
        self.value = value

class Var:
    def __init__(self, name):
        self.name = name

class IfElse:
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class WhileLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForLoop:
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body

class FuncDef:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class Return:
    def __init__(self, value):
        self.value = value
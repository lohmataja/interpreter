__author__ = 'lohmataja@gmail.com'
class ExpressionAST():
    def __init__(self, items):
        self.items = items
class NumberAST():
    def __init__(self, num):
        self.value = num
class VariableAST():
    def __init__(self, name, value):
        self.name = name
        self.value = value
class CallAST():
    def __init__(self, callee, args):
        self.callee = callee
        self.args = args
class BinaryExprAST():
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
class PrototypeAST():
    def __init__(self, name, *args):
        self.name = name
        self.args = args
class FunctionAST():
    def __init__(self, proto, body):
        self.proto = proto
        self.body = body
class ConditionAST():
    def __init__(self, condition, then_clause, else_clause):
        self.condition = condition
        self.then_clause = then_clause
        self.else_clause = else_clause

def make_AST(tokens):
    if type(tokens) == list:
        if len(tokens) == 0:
            return None
        elif tokens[0] == 'define':
            if type(tokens[1]) == str:
                return VariableAST(tokens[1], tokens[2])
            else:
                return FunctionAST(PrototypeAST(*tokens[1]), make_AST(tokens[2]))
        elif tokens[0] == 'if':
            condition, then_clause, else_clause = tokens[1:]
            return ConditionAST(make_AST(condition), make_AST(then_clause), make_AST(else_clause))
        else:
            return CallAST(*tokens)
    else:
        try:
            val = float(tokens)
            return NumberAST(val)
        except ValueError:
            return ExpressionAST(tokens)

def module_to_AST(module_tree):
    return [make_AST(subtree) for subtree in module_tree]
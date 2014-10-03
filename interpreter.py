__author__ = 'lohmataja@gmail.com'
import builtins
import operator as op
import my_parser


def evaluate(items):
    predefined = {'+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, '**':op.pow,
                  'quote':(lambda *args: args)}
    if type(items) == list:
        if len(items) == 0:
            return items
        func, *args = items
        args = [evaluate(arg) for arg in args]
        try:
            return locals().get(func, predefined[func])(*args)
        except KeyError:
            try: return getattr(builtins, func)(*args)
            except: print("Function {} is not defined".format(func))
    else:
        return items

def s_eval(code):
    parse_tree = my_parser.parse(my_parser.tokenize(code))
    print(parse_tree)
    print(evaluate(parse_tree))

# code = ''
# while True:
#     new_line = sys.stdin.readline()
#     if new_line == '\n':
#         s_eval(code)
#         code = ''
#     else:
#         code += new_line

s_eval("(+ 5 6)")
s_eval("(sum '(1 2 3))")
def tokenize(code):
    return code.replace('(', ' ( ').replace(')', ' ) ').replace("' (", "( quote").split()

def read_tokens(tokens):
    res = []
    while tokens:
        cur = tokens.pop(0)
        if cur == '(':
            res.append(read_tokens(tokens))
        elif cur == ')':
            return res
        else:
            try: cur = int(cur)
            except ValueError:
                try: cur = float(cur)
                except: pass
            res.append(cur)
    return res

def parse(tokens):
    first = tokens.pop(0)
    assert first == '('
    return read_tokens(tokens)



if __name__ == "__main__":
    c1 = """   (define (f n)
        (let ((a 4.5)
              (b 7))
              (* a b)))"""
    c2 = "(sum '(1 2 3))"
    print(parse(tokenize(c2)))
    print(parse(tokenize(c1)))

# def num(n):
#     def try_f(f):
#         try:
#             return f(n)
#         except:
#             return
#     return next(try_f(f) for f in [int, float, str] if try_f(f) != None)
#
# for n in ['5', '5.5', '0.0', '56.d']:
#     print(num(n), type(num(n)))
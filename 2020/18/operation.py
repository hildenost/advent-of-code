from operator import add, mul

test1 = "1 + 2 * 3 + 4 * 5 + 6"
test2 = "1 + (2 * 3) + (4 * (5 + 6))"
test3 = "2 * 3 + (4 * 5)"
test4 = "5 + (8*3+9+3*4*3)"
test5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
test6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


def parser_1(expression):
    i = 0
    answer = 0
    op = add
    while i < len(expression):
        curr = expression[i]
        if curr.isdigit():
            answer = op(answer, int(curr))
        elif curr == "*":
            op = mul
        elif curr == "+":
            op = add
        elif curr == "(":
            sub_answer, delta = parser_1(expression[i + 1 :])
            answer = op(answer, sub_answer)
            i += delta
        elif curr == ")":
            return answer, i + 1
        i += 1
    return answer, i


def lexer(expression):
    tokens = []
    for c in expression:
        if c.isdigit():
            tokens.append(int(c))
        elif c == "*":
            tokens.append(mul)
        elif c == "+":
            tokens.append(add)
        elif c in "()":
            tokens.append(c)
    tokens.append(None)
    return tokens


def addend(token, tokens):
    """ addend : INTEGER | ( term ) """
    if isinstance(token, int):
        return token
    elif token == "(":
        return interpreter(tokens)


def term(token, tokens):
    """ term : addend (ADD addend)* """
    result = addend(token, tokens)

    token = tokens[0]
    while token == add and token is not None:
        token = tokens.pop(0)
        token = tokens.pop(0)
        result += addend(token, tokens)
        token = tokens[0]
    return result


def interpreter(tokens):
    """ expr: term (MUL term)* """
    token = tokens.pop(0)
    result = term(token, tokens)

    token = tokens.pop(0)
    while token == mul and token is not None:
        token = tokens.pop(0)
        result *= term(token, tokens)
        token = tokens.pop(0)

    return result


def solve(expression):
    tokens = lexer(expression)
    answer = interpreter(tokens)
    return answer


with open("18/input.txt") as f:
    expressions = f.read().splitlines()

assert solve(test1) == 231
assert solve(test2) == 51
assert solve(test3) == 46
assert solve(test4) == 1445
assert solve(test5) == 669060
assert solve(test6) == 23340

print("Part 1: ", sum(parser_1(expr)[0] for expr in expressions))
print("Part 2: ", sum(solve(expr) for expr in expressions))

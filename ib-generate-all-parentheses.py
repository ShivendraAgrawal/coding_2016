def isValid(A):
    stack = []
    for c in A:
        if c in ['(', '{', '[']:
            stack.append(c)
        elif c in [')', '}', ']'] and len(stack) == 0:
            return 0
        elif c == ')' and stack[-1] == '(':
            stack.pop()
        elif c == '}' and stack[-1] == '{':
            stack.pop()
        elif c == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return 0
    if len(stack) == 0:
        return 1
    else:
        return 0






A = '(({}))'
A = '()[]{}'
A = '])'
print(isValid(A))
def braces(A):
    stack = []
    redundant = False
    for c in A:
        if c != ' ':
            if c in ['(', '+', '-', '*', '/']:
                stack.append(c)
            elif c == ')':
                redundant = True
                while stack[-1] != '(':
                    redundant = False
                    stack.pop()
                stack.pop()
                if redundant:
                    return int(redundant)
    return int(redundant)


A = '((a+b))'
# A = '()[]{}'
A = '(a + (a + b))'
A = '(a+(a))'
print(braces(A))
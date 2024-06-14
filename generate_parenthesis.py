def generate_parenthesis(n: int):
    stack = []
    res = []

    def backtrack(open_n, closed_n):
        if open_n == closed_n == n:
            res.append("".join(stack))
            return
        if open_n < n:
            stack.append("(")
            backtrack(open_n + 1, closed_n)
            stack.pop()

        if closed_n < open_n:|
            stack.append(")")
            backtrack(open_n, closed_n + 1)
            stack.pop()
    
    backtrack(0, 0)

    return res

generate_parenthesis(3)
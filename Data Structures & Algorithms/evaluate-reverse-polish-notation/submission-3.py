class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token == '+':
                x, y = res.pop(), res.pop()
                res.append(int(x+y))
            elif token == '-':
                x, y = res.pop(), res.pop()
                res.append(int(y-x))
            elif token == '*':
                x, y = res.pop(), res.pop()
                res.append(int(x*y))
            elif token == '/':
                x, y = res.pop(), res.pop()
                res.append(int(y/x))
            else:
                res.append(int(token))
        return int(res.pop())

        
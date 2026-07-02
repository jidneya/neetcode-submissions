class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token == '+':
                x, y = res.pop(), res.pop()
                res.append(x+y)
            elif token == '-':
                x, y = res.pop(), res.pop()
                res.append(y-x)
            elif token == '*':
                x, y = res.pop(), res.pop()
                res.append(x*y)
            elif token == '/':
                x, y = res.pop(), res.pop()
                res.append(int(y/x))
            else:
                res.append(int(token))
        return res[0]

        
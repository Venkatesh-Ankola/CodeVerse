class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for n in s:
            print(n)
            if n == '(' or n== '[' or n== '{':
                l.append(n)
            if n == ')':
                if len(l) == 0:
                    return False
                if l[-1] == '(':
                    l.pop()
                else:
                    return False
            if n== ']':
                if len(l) == 0:
                    return False
                if l[-1] == '[':
                    l.pop()
                else:
                    return False

            if n== '}':
                if len(l) == 0:
                    return False
                if l[-1] == '{':
                    l.pop()
                else:
                    return False

        if len(l) == 0:
            return True
        return False
        
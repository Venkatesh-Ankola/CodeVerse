class Solution:
    def simplifyPath(self, path: str) -> str:
        comp = path.split("/")
        stack = []

        for n in comp:
            if n == "" or n ==".":
                continue

            if n == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(n)

        # return "/"+"/".join(stack)
        st = ""
        if not stack:
            return "/"
        for n in stack:
            st+='/'
            st+=n
            

        return st


        
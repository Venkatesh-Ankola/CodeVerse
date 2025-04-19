class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st =[]
        for n in tokens:

            if n == "+":
                a = st.pop(-1)
                b = st.pop(-1)
                st.append(a+b)
            
            elif n == "-":
                a = st.pop(-2)
                b = st.pop(-1)
                st.append(a-b)

            elif n == "*":
                a = st.pop(-2)
                b = st.pop(-1)
                st.append(a*b)

            elif n == "/":
                a = st.pop(-2)
                b = st.pop(-1)
                st.append(int(a/b))

            else:
                st.append(int(n))

            # print(st)

            

        return st[0]
            

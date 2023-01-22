"""
Check if everything ok with parenthesis in string s.
If it's not ok, print place of mistake.
"""


def parenthesis(s):
    if type(s) is not str:
        raise TypeError('Incorrect input. Please enter a string.')
    d = dict((('(', ')'), ('[', ']'), ('{', '}')))
    st = []

    for i in range(len(s)):
        if s[i] in d.keys():
            st.append([s[i], i])

        elif s[i] in d.values():
            if len(st) == 0:
                return i + 1
            elif len(st) > 0:
                tmp = st.pop()
                if d[tmp[0]] != s[i]:
                    return i + 1
    if len(st) == 0:
        return 'Success'
    else:
        return st[len(st) - 1][1] + 1

def main():
    s = input('Please enter a string to check if it has correct parenthesis: ')
    print(s)
    print(parenthesis(s))

if __name__ == '__main__':
    main()

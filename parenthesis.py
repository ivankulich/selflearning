import re

"""
Check if everything ok with parenthesis in string s.
If it's not ok, print place of mistake.
"""

def test(m=10):
    import random
    for _ in range(m):
        n = random.randint(0, 30)
        s = (random.choice(['[', '(', '{', ']', ')', '}','*']) for _ in range(n))
        s = ''.join(list(s))
    return s

# test data
s = test()
#s = input()
#s = '([](){([])})'
#s = '()[]}'
#s = '{{[()]]'
#s = 'abc'
#s = '[]([]'
#s = '{{{[][][]'
#s = '}*(]'
#s = '{([{()[]]}'
#s = {}(*{{]*}(}*(](*(*}
#s = '()}['
#s = '[]{'
#s = '()*((}{(}}[)(}])]))['
#s = ''
#s = '(){}'
#s = '((('
#s = '}}}'

print(s)

#s = re.sub('[^\(\)\{\}\[\]]', '', s)
#print(s)


def parenthesis(s):
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

print(parenthesis(s))

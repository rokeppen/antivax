def regex(word):
    res = [translate_char(a.upper()) for a in word]
    return ''.join(res) + '|' + ''.join(res[::-1])


def translate_char(a):
    dic = {'B': '[ND]', 'Z': '[QE]', 'X': '[A-Z]', 'O': '[A-Z]', 'J': 'I', 'U': 'V'}
    return dic.get(a, a)

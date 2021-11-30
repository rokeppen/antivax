def read_result(file):
    result = dict()
    with open(file) as f:
        key = ''
        value = []
        for line in f.readlines():
            if line[0] == '>':
                if key:
                    result[key] = value
                key = line.strip()[1:]
                value = []
            else:
                value.append(line.strip())
    return result


def get_union(dic):
    result = set(list(dic.values())[0]).intersection(set(list(dic.values())[1]))
    #for li in dic.values():
    #    result = result.intersection(set(li))
    return len(result), sorted(list(result), key=len)[::-1]


def is_in(dic, word):
    return [key for key, li in dic.items() if word in li]


def are_in(dic, wordlist):
    return [key for key, li in dic.items() if all(word in li for word in wordlist)]


res = read_result('result.txt')
# print(res)
# print(get_union(res))
print(are_in(res, ['made', 'in', 'China']))
print(are_in(res, ['viroloog', 'mark', 'van', 'Ranst']))
print(are_in(res, ['dit', 'is', 'een', 'mop', 'haha']))
print(are_in(res, ['weer', 'veel', 'geld']))
print(are_in(res, ['neem', 'mij', 'niet']))

from collections import Counter


class MyTree:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def get_key(some_d, value):
    for k, v in some_d.items():
        if v == value:
            return k


def min_nums(array):
    min_1 = None
    min_2 = None
    max_num = max(array)
    for index, num in enumerate(array):
        if num <= max_num:
            max_num = num
            min_1 = (num, index)
    max_num = max(array)
    for index, num in enumerate(array):
        if index != min_1[1]:
            if num <= max_num:
                max_num = num
                min_2 = (num, index)
    return min_1, min_2


def recurs_bin_codes(tree, bin_codes, code):
    if tree.left is not None:
        code.append('0')
        if isinstance(tree.left, str):
            bin_codes[tree.left] = ''.join(code)
            code.pop()
        else:
            recurs_bin_codes(tree.left, bin_codes, code)
            code.pop()
    if tree.right is not None:
        code.append('1')
        if isinstance(tree.right, str):
            bin_codes[tree.right] = ''.join(code)
            code.pop()
        else:
            recurs_bin_codes(tree.right, bin_codes, code)
            code.pop()


inp_data = input('Введите строку для кодировки ')
letters = Counter(inp_data)

frq = []
for i in letters:
    frq.append(letters[i])

for i in range(len(letters)-1):
    minimals = min_nums(frq)
    key_1 = list(letters.keys())[minimals[0][1]]
    key_2 = list(letters.keys())[minimals[1][1]]
    node_key = key_1 + key_2
    frq.remove(minimals[0][0])
    frq.remove(minimals[1][0])
    frq.append(minimals[0][0] + minimals[1][0])

    if len(key_1) > 1 and len(key_2) > 1:
        letters[node_key] = MyTree(0, node_key, letters[key_1], letters[key_2])
    elif len(key_1) > 1:
        letters[node_key] = MyTree(0, node_key, letters[key_1], key_2)
    elif len(key_2) > 1:
        letters[node_key] = MyTree(0, node_key, key_1, letters[key_2])
    else:
        letters[node_key] = MyTree(0, node_key, key_1, key_2)
    letters.pop(key_1)
    letters.pop(key_2)
tree_result = letters[next(iter(letters))]
bin_codes = {}
code = []
recurs_bin_codes(tree_result, bin_codes, code)
bin_result = []
for letter in inp_data:
    bin_result.append(bin_codes[letter])
result_string = ''.join(bin_result)
print(result_string)

code_list = []
word_list = []
for bin_code in result_string:
    code_list.append(bin_code)
    if ''.join(code_list) in bin_codes.values():
        word_list.append(get_key(bin_codes, ''.join(code_list)))
        code_list.clear()

print(''.join(word_list))

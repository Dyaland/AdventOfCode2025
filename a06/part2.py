import re


def multi(lst):

    result = 1
    for val in lst:
        result *= int(val)
    return result


def addi(lst):

    return sum(int(val) for val in lst)


def solution(data):

    operator = {'*': multi, '+': addi}

    num_lengths = [len(item) -1 for item in re.findall(r'[+*][\s]*', data[-1])]
    operators_list = [char.strip(' ') for char in data.pop(-1) if char.strip(' ')]
    num_rows = range(len(data))

    grand_total = 0
    pos_mod = 0
    for index, length in enumerate(num_lengths):
        nums = []
        for i in range(length):
            nums.append(''.join([data[j][i+pos_mod] for j in num_rows if data[j][i+pos_mod].strip(' ')]))
        grand_total += operator[operators_list[index]](nums)
        pos_mod += length + 1

    return grand_total


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = [re.sub(r'\n', ' ', line) for line in f.readlines()]
    print(solution(data))

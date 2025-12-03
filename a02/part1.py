def check_repeat(num):
       
    strint, length = str(num), len(str(num))
    if length % 2 == 0:
        if strint[:length // 2] == strint[length // 2:]:
            return True
    return False


def solution():

    sum_of_false_ids = 0

    for id_range in data:
        for i in range(id_range[0], id_range[1] + 1):
            if check_repeat(i):
                sum_of_false_ids += i
    return sum_of_false_ids


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = ([int(first), int(last)] for pair in f.read().split(',') for first, last in [pair.split('-')])
    print(solution())

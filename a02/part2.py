def check_repeat(num):
    
    strint = str(num)
    divisors = [i for i in range(2, len(strint) + 1)]

    for div in divisors:
        alt_div = len(strint) // div
        if all(strint[0:alt_div] == strint[i:i + alt_div] for i in range(0, len(strint), alt_div)):
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

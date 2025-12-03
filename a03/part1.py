def max_joltage(num):

    first = max(num[:len(num) - 1])
    second = max(num[num.index(first) + 1:])

    return int(first + second)


def solution():

    output_power = 0
    for bank in bank_list:
        output_power += max_joltage(bank)

    return output_power


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        bank_list = [line.strip() for line in f.readlines() if line.strip()]
    print(solution())

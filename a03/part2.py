def max_joltage(bank):

    sequence = ''
    for i in range(-11, 0, 1):
        battery = max(bank[:i])
        sequence += battery
        bank = bank[bank.index(battery) + 1:]
    sequence += max(bank)

    return int(sequence)


def solution():

    output_power = 0
    for bank in bank_list:
        output_power += max_joltage(bank)

    return output_power


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        bank_list = [line.strip() for line in f.readlines() if line.strip()]
    print(solution())

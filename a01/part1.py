def spin_dial(dial, line):

    direction = -1 if line[0] == 'L' else 1
    value = int(line[1:])
    change = direction * value

    _, dial = divmod(dial + change, 100)

    return dial


def main():

    zero_count, dial = 0, 50
    for line in data:
        dial = spin_dial(dial, line)
        if dial == 0:
            zero_count += 1

    return zero_count


if __name__ == '__main__':

    with open('a01/input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines() if line.strip()]

    result = main()
    print(result)

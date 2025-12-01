def spin_dial(input_dial, line):

    direction = -1 if line[0] == 'L' else 1
    value = int(line[1:])
    change = direction * value

    zero_hits, dial = divmod(input_dial + change, 100)
    zero_hits = abs(zero_hits)

    if input_dial == 0 and change < 0:
        zero_hits -= 1
    if dial == 0 and change < 0:
        zero_hits += 1

    return dial, zero_hits


def main():

    zero_count, dial = 0, 50
    for line in data:
        dial, zero_hits = spin_dial(dial, line)
        zero_count += zero_hits

    return zero_count


if __name__ == '__main__':

    with open('a01/input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines() if line.strip()]

    result = main()
    print(result)
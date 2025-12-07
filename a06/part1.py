def solution(data):

    grand_total = 0
    width = len(data[0])
    height = len(data)

    for x in range(width):
        if data[-1][x] == '*':
            total = 1
            for y in range(height - 1):
                total *= int(data[y][x])
        else:
            total = 0
            for y in range(height - 1):
                total += int(data[y][x])
        grand_total += total

    return grand_total


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = [[item.strip() for item in line.split(' ') if item.strip()] for line in f.readlines()]
    print(solution(data))

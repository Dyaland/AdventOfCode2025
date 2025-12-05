def check_adjacent(y, x, data):
    adjacent = []
    y_adj, x_adj = [], []

    if y != 0:
        y_adj.append(-1)
    y_adj.append(0)
    if y != max_y:
        y_adj.append(1)

    if x != 0:
        x_adj.append(-1)
    x_adj.append(0)
    if x != max_x:
        x_adj.append(1)

    for y_mod in y_adj:
        for x_mod in x_adj:
            adjacent.append(data[y + y_mod][x + x_mod])

    if adjacent.count('@') < 5:
        return True
    return False


def solution(data):

    movable_count = 0
    change = True
    while change == True:
        change = False
        next_data = [[char for char in row] for row in data]
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if data[y][x] == '@' and check_adjacent(y, x, data):
                    movable_count += 1
                    next_data[y][x] = '.'
                    change = True
        data = [[char for char in row] for row in next_data]
    return movable_count
    


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines() if line.strip()]
        max_y = len(data) - 1
        max_x = len(data[0]) - 1
    print(solution(data))

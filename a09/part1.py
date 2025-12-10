def solution():

    result = 0
    for src in data[:len(data) + 1]:
        for dst in data:
            size = (abs(dst[0] - src[0]) + 1) * (abs(dst[1] - src[1]) + 1)
            if size > result:
                result = size
    return result

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = sorted([(int(line.split(',')[0]), int(line.split(',')[1].strip())) for line in f.readlines() if line.strip()])
    print(solution())
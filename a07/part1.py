def solution():

    splits = 0
    for y in range(len(data)):
        if y == 0:
            cur_tachyons = {data[0].index('S')}
            continue
        
        new_tachyons = set()
        ded_tachyons = set()
        for x in cur_tachyons:
            if data[y][x] == '^':

                splits += 1
                ded_tachyons.add(x)

                if x < len(data[0]):
                    new_tachyons.add(x + 1)
                if x > 0:
                    new_tachyons.add(x - 1)

        for x in ded_tachyons:
            cur_tachyons.remove(x)
        cur_tachyons.update(new_tachyons)

    return splits
                        

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines() if line.strip()]
    print(solution())

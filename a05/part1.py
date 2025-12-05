def check_freshness(item, id_ranges):

    for rng in id_ranges:
        if rng[0] <= item <= rng[1]:
            return True
    return False


def solution(ranges, ids):

    fresh_ids = 0

    id_ranges = [(int(item.split('-')[0]), int(item.split('-')[1])) for item in ranges.split('\n')]
    ingredients = [int(item) for item in ids.split('\n') if item.strip()]

    for item in ingredients:
        if check_freshness(item, id_ranges) is True:
            fresh_ids += 1
    return fresh_ids

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        ranges, ids = f.read().split('\n\n')
    print(solution(ranges, ids))

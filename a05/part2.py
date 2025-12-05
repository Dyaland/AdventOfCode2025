def merge_ranges(id_ranges):

    id_ranges.sort()
    merged_ranges = []
    for low, high in id_ranges:
        if not merged_ranges or low > merged_ranges[-1][1] + 1:
            merged_ranges.append((low, high))
        else:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], high))
    return merged_ranges


def solution(ranges):

    fresh_ids = 0

    id_ranges = [(int(item.split('-')[0]), int(item.split('-')[1])) for item in ranges.split('\n')]
    merged_rngs = merge_ranges(id_ranges)

    for rng in merged_rngs:
        fresh_ids += (rng[1] - rng[0]) + 1

    return fresh_ids


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        ranges, _ = f.read().split('\n\n')
    print(solution(ranges))

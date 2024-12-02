from aocd import get_data, submit

# data = get_data(day=1, year=2024)
# with open('day1/input.txt', 'w') as file:
#     file.write(data)

with open('day1/input.txt', 'r') as file:
    lines = file.readlines()

def part_a():
    list_a = []
    list_b = []

    for line in lines:
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))

    list_a.sort()
    list_b.sort()

    assert len(list_a) == len(list_b)

    sum_diffs = 0
    for i in range(len(list_a)):
        sum_diffs += abs(list_a[i] - list_b[i])

    submit(sum_diffs, part='a', day=1, year=2024)


def part_b():
    list_a = []
    list_b = []

    for line in lines:
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))
    
    sim_score = 0
    for a in list_a:
        sim_score += a * list_b.count(a)
    
    submit(sim_score, part='b', day=1, year=2024)


if __name__ == "__main__":
    part_a()
    part_b()
from aocd import get_data, submit

def save_input_data(day):
    data = get_data(day=day, year=2024)
    with open(f'day{day}/input.txt', 'w') as file:
        file.write(data)

def read_input_data(day):
    with open(f'day{day}/input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        return lines

def part_a(lines):
    def monotonic(levels):
        if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
            return True
        return False
    
    def good_diffs(levels):
        for i in range(len(levels) - 1):
            if not (abs(levels[i] - levels[i + 1]) >= 1 and abs(levels[i] - levels[i + 1]) <= 3):
                return False
        return True
    
    num_safe = 0
    
    for line in lines:
        levels = list(map(int, line.split()))
        if monotonic(levels) and good_diffs(levels):
            num_safe += 1
    
    print("Number of safe reports:", num_safe)
    return num_safe


def part_b(lines):
    def monotonic(levels):
        if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
            return True
        return False
    
    def good_diffs(levels):
        for i in range(len(levels) - 1):
            if not (abs(levels[i] - levels[i + 1]) >= 1 and abs(levels[i] - levels[i + 1]) <= 3):
                return False
        return True
    
    num_safe = 0
    
    for line in lines:
        levels = list(map(int, line.split()))
        if monotonic(levels) and good_diffs(levels):
            num_safe += 1
        else:
            # Loop through each level and remove it from the list, then check if the remaining levels are safe
            for i in range(len(levels)):
                if monotonic(levels[:i] + levels[i + 1:]) and good_diffs(levels[:i] + levels[i + 1:]):
                    num_safe += 1
                    break
    
    print("Number of dampened safe reports:", num_safe)
    return num_safe


if __name__ == "__main__":
    day = 2
    
    # save_input_data(day)
    
    lines = read_input_data(day)
    
    a_output = part_a(lines)
    
    # submit(a_output, part='a', day=day, year=2024)
    
    b_output = part_b(lines)
    
    submit(b_output, part='b', day=day, year=2024)
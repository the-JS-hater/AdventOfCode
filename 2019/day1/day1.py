def part_one():
    file = open("day1_input.txt", "r")
    required_fuel = lambda line :  int(int(line) / 3) - 2
    return sum(map(required_fuel, file.readlines()))


def part_two():
    def required_fuel(mass):
        x = int(int(mass) / 3) - 2
        if x <= 0:
            return 0
        return x + required_fuel(x)

    return sum(map(required_fuel, open("day1_input.txt", "r").readlines()))


if __name__ == "__main__":
    print(f"Solution to part 1: {part_one()}")
    print(f"Solution to part 2: {part_two()}")

from functools import reduce

DATA = open("02.txt").readlines()
COLOR_LIMIT = {"red": 12, "green": 13, "blue": 14}


def parse_game_record(game_record: list[str]) -> dict[str, dict[str, list[int]]]:
    games = {}

    for line in game_record:
        game_id, game_sets = line.split(":")

        game_id = game_id.split()[1]
        games[game_id] = {}

        # Extract count and color pairs from game sets as only the count
        # of the cubes for each color is required.
        game_sets = game_sets.strip().split(";")
        game_sets = ",".join(game_sets).split(",")
        counts_and_colors = [i.split() for i in game_sets]

        for cube_count, cube_color in counts_and_colors:
            if cube_color not in games[game_id]:
                games[game_id][cube_color] = []
            games[game_id][cube_color].append(int(cube_count))

    return games


game_record = parse_game_record(DATA)
possible_games = []  # Part 1
minimum_set_powers = []  # Part 2

for game_id, cubes in game_record.items():
    # Part 1
    game_possible = all(max(cubes[color]) <= COLOR_LIMIT[color] for color in cubes)
    if game_possible:
        possible_games.append(int(game_id))

    # Part 2
    fewest_cubes_required = [max(cubes[color]) for color in cubes]
    power_of_set = reduce(lambda x, y: x * y, fewest_cubes_required, 1)
    minimum_set_powers.append(power_of_set)

print(sum(possible_games))
print(sum(minimum_set_powers))

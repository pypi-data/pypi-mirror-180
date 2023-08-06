import random

def get_random_color(i):
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    if i:
        return colors[i % len(colors)]
    else:
        return random.choice(colors)


def generate_temperatures(number, start, end):
    return [random.randint(start, end) for _ in range(number)]
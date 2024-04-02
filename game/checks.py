import random

def roll_dice(num_dice: int):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return min(results)
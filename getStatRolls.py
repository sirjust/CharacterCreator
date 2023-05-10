import random

def main():
    stats = []

    for i in range(6):
        sum = roll()
        stats.append(sum)

    print(stats)
    return stats

def roll():
    # Roll a six-sided die
    die_roll = random.randint(1, 6)

    dice_rolls = []
    for i in range(4):
        die_roll = random.randint(1, 6)
        dice_rolls.append(die_roll)

    # Remove the lowest
    dice_rolls.remove(min(dice_rolls))

    # Add the rest together
    sum = 0
    for i in dice_rolls:
        sum += i
    return sum

if __name__ == '__main__':
    main()
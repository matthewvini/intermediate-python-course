

def main():
    import random
    dice_rolls = int(input("How many dice would you like to roll ?"))
    dice_size = int(input('How many sides are the dice?'))
    dice_sum = 0
    for i in range(0,dice_rolls):
        """ for every index in a range starting after 0 until the value is equal to dice_rolls, do this :"""
        roll = random.randint(1,dice_size)
        dice_sum+=roll
        if roll == 1:
            print(f'You rolled {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled {roll}! Critical Success')
        else:

            print(f'You rolled a {roll}')#f-string functionality.
    print(f'You have rolled a total of {dice_sum}')


if __name__== "__main__":
    main()

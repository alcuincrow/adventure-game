import time
import random

# list of monsters in const variables
MONSTER1 = "tax collector"
MONSTER2 = "bandit"
MONSTER3 = "troll"
MONSTER4 = "goblin"
MONSTER5 = "zombie"

# this gets a random monster for the game


def get_monster(result):
    monster_set = [MONSTER1, MONSTER2, MONSTER3, MONSTER4, MONSTER5]
    pick = random.choice(monster_set)
    if MONSTER1 in pick:
        result.append("tax collector")
    elif MONSTER2 in pick:
        result.append("bandit")
    elif MONSTER3 in pick:
        result.append("troll")
    elif MONSTER4 in pick:
        result.append("goblin")
    elif MONSTER5 in pick:
        result.append("zombie")
    return result

# used to print pauses


def print_pause(string_to_print):
    print(string_to_print)
    time.sleep(1)

# gets valid input from the player


def valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print_pause(
                f"Sorry, the option {choice} is invalid. Please try again!")

# options for the field choices


def field_choice(item, result):
    choice = valid_input("Please enter 1 or 2:\n", ["1", "2"])
    if choice == "1":
        house(item, result)
    elif choice == "2":
        cave(item, result)

# options for the cave choices


def cave_items(item):
    choice = valid_input("Please enter: 1, 2 or 3:\n", ["1", "2", "3"])
    if choice == "1":
        item.append("sword")
    elif choice == "2":
        item.append("mace")
    elif choice == "3":
        item.append("rock")
    if item != []:
        print_pause(
            f"You take your new {item[0]}, and head back to the field.")
    else:
        print_pause("You decide to leave the skeletons alone.")
        print_pause(
            "Since the cave is otherwise abandoned, "
            "you decide to return to the field.")

# choices in the house


def house_choices(item, result):
    choice = valid_input("Please enter 1 or 2:\n", ["1", "2"])
    if choice == "1":
        fight(item, result)
    elif choice == "2":
        print_pause("You flee to the safety of the field.")
        print_pause(f"The {result[0]} doesn't follow you.")
        field(item, result)

# introduction to the game


def intro(result):
    print_pause(f"A {result[0]} is terrorizing your village.")
    print_pause("A bounty has been offered to whoever defeats it.")
    print_pause("You want to be the one to collect it!")
    print_pause(
        f"Your search for the {result[0]} "
        "has led you to a field outside of the village.")
    print_pause("Nearby there is an old house and a cave.")

# things that happen when the player is in the field


def field(item, result):
    print_pause("You are standing in a field outside of your village.")
    print_pause("\nWhat would you like to do next?\n"
                "Enter 1 to visit the house.\n"
                "Enter 2 to explore the cave.\n")
    field_choice(item, result)

# things that happen when the player goes into the cave


def cave(item, result):
    print_pause("You peer into the cave.")
    print_pause(
        "It's dark inside the cave, "
        "but you can make out skeletons scattered about.")
    if item:
        print_pause(f"You're already carrying a {item[0]}.")
        print_pause("You decide to leave the skeletons in peace.")
        field(item, result)
    elif not item:
        print_pause("Among the remains you see several old weapons.")
        print_pause("\nWhich weapon do you want to pick up?\n"
                    "Enter 1 to pick up a rusty sword.\n"
                    "Enter 2 to pick up an old mace.\n"
                    "Enter 3 to leave the skeletons"
                    " alone and pick up a large rock.\n")
        cave_items(item)
        field(item, result)

# things that happen when the player goes into the house


def house(item, result):
    print_pause("You approach the house and knock on the door.")
    print_pause(f"The {result[0]} throws open the front door with a roar!")
    if item == []:
        print_pause("You are unarmed, and you cower in fear!")
    elif item != []:
        print_pause(f"You feel emboldened by your {item[0]}.")
    print_pause("\nWhat are you going to do next?\n"
                "Enter 1 to stand your ground and fight.\n"
                "Enter 2 to run back to the field.\n")
    house_choices(item, result)

# things that happen when the player fights


def fight(item, result):
    if item == []:
        print_pause(
            f"Because you are unarmed and terrified,"
            f"the {result[0]} easily defeats you.")
        print_pause("\n")
        print_pause("GAME OVER")
        start_over()
    else:
        print_pause(f"You raise your {item[0]}!")
        print_pause(
            f"The {result[0]} tries to attack, but you quickly sidestep it! ")
        if 'sword' in item:
            print_pause(
                f"The {result[0]} trips and lands on your raised {item[0]}!")
        else:
            print_pause(
                f"You swing your {item[0]} and"
                f" hit the {result[0]} in the head!")
        print_pause(
            f"The {result[0]} falls to the floor of the house, defeated.")
        print_pause(f"You have saved your village and can collect the bounty!")
        bounty = random.randint(6, 98)
        print_pause(f"Your reward is {bounty} copper coins.")
        print_pause("\n")
        print_pause("GAME OVER!")
        start_over()

# things that happen after the game ends


def start_over():
    choice = valid_input("Would you like to play again?\n"
                         "Enter 1 to play again.\n"
                         "Enter 2 to end the game.\n", ["1", "2"])
    if choice == "1":
        play_game()
    elif choice == "2":
        print_pause("Thank you for playing! ")
        exit(0)

# main function that runs the game


def play_game():
    item = []
    result = []
    get_monster(result)
    intro(result)
    field(item, result)


if __name__ == '__main__':
    play_game()

import random

def game(comp, you):
    valid_choices = ['s', 'w', 'g', 'q']
    if you not in valid_choices:
        return "invalid"

    if comp == you:
        return None
    elif you == 'q':
        return 'quit'
    
    # if comp chooses snack
    if comp == 's':
        if you == 'w':
            return False  # you lose
        elif you == 'g':
            return True   # you win

    # if comp chooses water
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    # if comp chooses gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


while True:
    rand_no = random.randint(1, 3)
    if rand_no == 1:
        comp = 's'
    elif rand_no == 2:
        comp = 'w'
    else:
        comp = 'g'   

    you = input("Your turn! Choose s for snack, w for water, g for gun, or q to quit: ").lower()

    result = game(comp, you)

    if result == "invalid":
        print("❌ Please enter a valid choice (s, w, g, or q).")
        continue  # skip rest and ask again

    print(f"You chose: {you}")
    print(f"Computer chose: {comp}")

    if result is None:
        print("It's a draw!")
    elif result == True:
        print("You win!")
    elif result == 'quit':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("You lose!")
import random

def game(comp, you):
    valid_choices = ['s', 'w', 'g', 'q']
    if you not in valid_choices:
        return "invalid"

    if comp == you:
        return None
    elif you == 'q':
        return 'quit'
    
    # if comp chooses snack
    if comp == 's':
        if you == 'w':
            return False  # you lose
        elif you == 'g':
            return True   # you win

    # if comp chooses water
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    # if comp chooses gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


while True:
    rand_no = random.randint(1, 3)
    if rand_no == 1:
        comp = 's'
    elif rand_no == 2:
        comp = 'w'
    else:
        comp = 'g'   

    you = input("Your turn! Choose s for snack, w for water, g for gun, or q to quit: ").lower()

    result = game(comp, you)

    if result == "invalid":
        print("❌ Please enter a valid choice (s, w, g, or q).")
        continue  # skip rest and ask again

    print(f"You chose: {you}")
    print(f"Computer chose: {comp}")

    if result is None:
        print("It's a draw!")
    elif result == True:
        print("You win!")
    elif result == 'quit':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("You lose!")






import random
def num_guessing_game():
    number=random.randint(1,10)
    attempts=0

    while True:
        guess=int(input("guess a number between 1 to 10"))
        attempts += 1
        if guess<number:
            print("too low!")
        elif guess>number:
            print("too high!")
        else:
            print(f"Congratulations! you guessed number {number} correctly in {attempts} attempts!")    
            break
num_guessing_game()        
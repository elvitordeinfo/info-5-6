import random

def main():
    na = input("Hello! What is your name?: ")
    print("Well" , na , "I am thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    answer = int(input("Take a guess..:"))

    while answer != number:
        if answer > number:
            print("Your guess is too high. Take a guess..:")
        elif answer < number:
            print("Your guess is to low. Take a guess..:")
        elif answer == number:
            print("Good job,", na, "! You guessed my number!")
            break

if __name__ == "__main__":
    main()


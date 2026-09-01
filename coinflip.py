import random

def main():
    coin = random.randint(1, 2)

    guess = input("Enter your guess: ").title().strip()

    if coin == (1,2):
        print("Heads")
    elif coin == (1,2):
        print("Tails")

    if guess == coin:
        print("Winner")
    else:
        print("Loser")

if __name__ == "__main__":
    main()



import random

class Game:
    def play(self):
        pass

class RockPaperScissors(Game):
    def play(self):
        choices = ["rock", "paper", "scissors"]
        user = input("Enter rock/paper/scissors: ").lower()
        comp = random.choice(choices)

        print(f"Computer chose: {comp}")

        if user == comp:
            print("Draw")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win")
        else:
            print("You lose")

class NumberGuessing(Game):
    def play(self):
        number = random.randint(1, 100)

        while True:
            guess = int(input("Guess number (1-100): "))

            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else:
                print("Correct!")
                break

class Hangman(Game):
    def play(self):
        words = ["python", "engineer", "hangman", "program"]
        word = random.choice(words)
        guessed = set()
        attempts = 6

        while attempts > 0:
            display = [letter if letter in guessed else "_" for letter in word]
            print(" ".join(display))

            if "_" not in display:
                print("You win!")
                return

            guess = input("Guess a letter: ").lower()

            if guess in word:
                guessed.add(guess)
            else:
                attempts -= 1
                print(f"Wrong! Attempts left: {attempts}")

        print(f"You lost. Word was: {word}")

class Blackjack(Game):
    def play(self):
        def draw_card():
            return random.randint(1, 11)

        user_score = draw_card() + draw_card()
        comp_score = draw_card() + draw_card()

        print(f"Your score: {user_score}")

        while input("Hit? (y/n): ").lower() == "y":
            user_score += draw_card()
            print(f"New score: {user_score}")
            if user_score > 21:
                print("Bust! You lose")
                return

        while comp_score < 17:
            comp_score += draw_card()

        print(f"Computer score: {comp_score}")

        if comp_score > 21 or user_score > comp_score:
            print("You win")
        elif user_score == comp_score:
            print("Draw")
        else:
            print("You lose")


def main():
    games = {
        "1": RockPaperScissors(),
        "2": NumberGuessing(),
        "3": Hangman(),
        "4": Blackjack()
    }

    while True:
        print("\n=== Game Suite ===")
        print("1. Rock Paper Scissors")
        print("2. Number Guessing")
        print("3. Hangman")
        print("4. Blackjack")
        print("5. Exit")

        choice = input("Choose a game: ")

        if choice == "5":
            break

        game = games.get(choice)

        if game:
            game.play()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
import random

WORDS = {
    "Computer Terms": [
        "computer",
        "keyboard",
        "monitor",
        "database",
        "processor"
    ],
    "Programming": [
        "python",
        "function",
        "variable",
        "algorithm",
        "developer"
    ],
    "Networking": [
        "router",
        "server",
        "firewall",
        "protocol",
        "bandwidth"
    ]
}


def display_word(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display


def play_hangman():

    category = random.choice(list(WORDS.keys()))
    secret_word = random.choice(WORDS[category])

    guessed_letters = []
    attempts = 6

    print("\n" + "=" * 40)
    print("         HANGMAN GAME")
    print("=" * 40)

    print(f"\nCategory: {category}")
    print("Guess the hidden word!")

    while attempts > 0:

        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Attempts Left:", attempts)

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✓ Correct!")
        else:
            attempts -= 1
            print("✗ Wrong Guess!")

        if all(letter in guessed_letters for letter in secret_word):

            print("\n" + "=" * 40)
            print("🎉 CONGRATULATIONS!")
            print(f"You guessed the word: {secret_word}")
            print("=" * 40)

            return

    print("\n" + "=" * 40)
    print("GAME OVER")
    print(f"The word was: {secret_word}")
    print("=" * 40)


while True:

    play_hangman()

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for playing!")
        break
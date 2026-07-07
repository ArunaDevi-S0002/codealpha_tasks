import random

print("=" * 60)
print("              AI RESCUE MISSION")
print("=" * 60)

name = input("Enter your name: ")

print(f"\nWelcome, {name}!")
print("Your mission is to save the AI system.")
print("Guess the secret word before all AI modules fail.\n")

# Word Bank
word_bank = {
    "python": {
        "category": "Programming Language",
        "hint": "Widely used in AI and Data Science"
    },
    "dataset": {
        "category": "Data Science",
        "hint": "Collection of information used for analysis"
    },
    "algorithm": {
        "category": "Programming Concept",
        "hint": "A step-by-step method to solve a problem"
    },
    "database": {
        "category": "Data Storage",
        "hint": "Stores structured information"
    },
    "neural": {
        "category": "Artificial Intelligence",
        "hint": "Related to brain-inspired networks"
    }
}

# Select Random Word
secret_word = random.choice(list(word_bank.keys()))

category = word_bank[secret_word]["category"]
extra_hint = word_bank[secret_word]["hint"]

guessed_letters = []

modules = [
    "Power Core",
    "Memory Unit",
    "Vision Sensor",
    "Language Engine",
    "Learning Module",
    "Decision Engine"
]

failed_modules = 0

while failed_modules < len(modules):

    print("\n" + "=" * 60)
    print("AI SYSTEM STATUS")
    print("=" * 60)

    for i in range(len(modules)):
        if i < failed_modules:
            print(f"✗ {modules[i]} - FAILED")
        else:
            print(f"✓ {modules[i]} - ACTIVE")

    print("\nCategory    :", category)
    print("Word Length :", len(secret_word))

    # Display Hidden Word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word        :", display_word)

    # Win Check
    if "_" not in display_word:
        print("\n CONGRATULATIONS!")
        print("You successfully saved the AI System.")
        print("Secret Word :", secret_word)
        break

    print("\nOptions")
    print("1. Guess Letter")
    print("2. Show Extra Hint")
    print("3. Guess Full Word")

    choice = input("Choose an option: ")

    if choice == "1":

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(" Correct Guess!")
        else:
            print(" Wrong Guess!")
            failed_modules += 1

    elif choice == "2":

        print("\n EXTRA HINT")
        print(extra_hint)

    elif choice == "3":

        full_guess = input("Enter the full word: ").lower()

        # Check word length before comparing
        if len(full_guess) != len(secret_word):
            print(
                f" The secret word contains {len(secret_word)} letters."
            )

        elif full_guess == secret_word:
            print("\n EXCELLENT!")
            print("You guessed the correct word.")
            break

        else:
            print(" Wrong Word!")
            failed_modules += 1

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

# Lose Condition
if failed_modules == len(modules):

    print("\n" + "=" * 60)
    print(" CRITICAL FAILURE")
    print("AI SYSTEM SHUTDOWN")
    print("=" * 60)

    print("Secret Word :", secret_word)

print("\nThank you for playing AI Rescue Mission!")
print("Keep learning Python, AI, and Data Science.")
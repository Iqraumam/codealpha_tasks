import random
words_bank = ["logic", "python", "simple", "intern", "console"]

secret_word = random.choice(words_bank)
revealed = ["_"] * len(secret_word)
used_chars = []
chances_left = 6

print("🎯 Hangman Game Started")
print("Word:", " ".join(revealed))

while chances_left > 0:
    user_char = input("\nGuess a letter: ").lower()

    if not user_char.isalpha() or len(user_char) != 1:
        print("Enter only one alphabet character.")
        continue

    if user_char in used_chars:
        print("You already tried this letter.")
        continue

    used_chars.append(user_char)

    if user_char in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == user_char:
                revealed[i] = user_char
        print("Good choice!")
    else:
        chances_left -= 1
        print(f"Incorrect guess. Remaining chances: {chances_left}")

    print("Word:", " ".join(revealed))

    if "_" not in revealed:
        print("\n🎉 Well done! You guessed the word.")
        break

if chances_left == 0:
    print("\n❌ No chances left.")
    print("Correct word was:", secret_word)

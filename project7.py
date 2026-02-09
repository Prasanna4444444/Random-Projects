secret_word = "python"
attempts = 5

print("🕵️ Welcome to the Secret Word Game!")
print("Hint: It's a programming language 🐍")
print("You have 5 attempts to guess the word.\n")

while attempts > 0:
    guess = input("Enter your guess: ").lower()

    if guess == secret_word:
        print("🎉 Correct! You guessed the secret word!")
        break
    else:
        attempts -= 1
        print("❌ Wrong guess.")
        print("Remaining attempts:", attempts, "\n")

if attempts == 0:
    print("😢 Game Over! The secret word was:", secret_word)

#syntax of while loop
i =1
while i <= 5:
    print(i)
    i+=2

#the guess game
secret_word = "computer"
guess = ""
guess_count = 0

while guess != secret_word:
    guess = input("Enter guess: ")
    guess_count += 1

print("You are win! You have guessed " + str(guess_count) + " times")




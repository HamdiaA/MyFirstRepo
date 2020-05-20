import random

secret = random.randint(0,100)

print("~ Guessing Game ~")

guess = int(input("Guess a number between 1 and 100: "))

while guess != secret:
  if guess > secret:
    print("Hmm...maybe too high. Try lower\n")
    guess = int(input("Guess again: "))
  elif guess < secret:
    print("Hmm...maybe too low. Try higher\n")
    guess = int(input("Guess again: "))

if guess == secret:
  print("Congrats! You guessed the secret number!")

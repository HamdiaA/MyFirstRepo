import random

#generates a random number between 0 to 100
secret = random.randint(0,100)

#you have to guess that random number
print("~ Guessing Game ~")

guess = int(input("Guess a number between 1 and 100: "))

while guess != secret:
  if guess > secret: #if your guess was too high
    print("Hmm...maybe too high. Try lower\n")
    guess = int(input("Guess again: "))

  elif guess < secret: #if your guess was too low
    print("Hmm...maybe too low. Try higher\n")
    guess = int(input("Guess again: "))

if guess == secret: #if you guessed correctly
  print("Congrats! You guessed the secret number!")

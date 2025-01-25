import random
high = 20
lowest = 10
answer = str(random.randint(10,20))
playing = True
guesses = 0
while playing :
  y = input("Guess a number between 10 - 20")
  if y == answer :
    print("Your guess is correct")
    break
  else :
    print("your guess is wrong try again")
    print("The number was", answer)
    guesses = guesses =+ 1
    print("Number of guesses", guesses)
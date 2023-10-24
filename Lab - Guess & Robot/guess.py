from random import randint 

answer = randint(0, 100)
result = ""
guesses = 0

def check_guess(guess):
  if answer > guess:
    return "HIGHER"
  if answer < guess:
    return "LOWER"
  if answer == guess:
    return "CORRECT"

print("What's your guess")
while result != "CORRECT":
  guesses += 1  
  result = check_guess(int(input("What's your guess")))
  print(result)

  if result == "CORRECT":
    break
  
  if guesses == 10:
    print("You've run out of guesses, it was " + str(answer))
    break
              
print("Game over")
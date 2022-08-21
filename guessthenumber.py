
import random
print("Welcome to the guessing game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Pick a difficulty, 'Easy' or 'Hard'.: ")

number = random.randint(1,100)

number_of_guesses=0 
if difficulty == 'Easy':
  number_of_guesses =10
elif difficulty =='Hard':
  number_of_guesses=5
print(f"You have {number_of_guesses} attemps")
while number_of_guesses >0:
  guess = int(input("What is you guess: "))
  if guess > number:
    print("Too High")
    number_of_guesses -=1
    print(f"{number_of_guesses} attemps left")
  elif guess < number:
    print("Too Low")
    number_of_guesses -=1
    print(f"{number_of_guesses} attemps left")
  elif guess == number:
    print(f"Correct , I was thinking of {number} ")


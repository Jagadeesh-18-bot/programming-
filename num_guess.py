import random
# defined a function called guess the number 
def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    

    a = 1
    b = 100
    secret_number = random.randint(a, b)
    
    attempts = 0
    guessed = False

    while not guessed:
        try:
           
            guess = int(input(f"Guess a number between {a} and {b}: "))
            attempts += 1
            
            if guess < a or guess > b:
                print(f"Please guess a number within the range {a} to {b}.")
                continue
            
           
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


guess_the_number()

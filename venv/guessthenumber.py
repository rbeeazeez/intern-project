import random
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')
for guess_taken in range (1, 7):
    print('guess the number')
    guess = int(input())
    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break
if guess == secret_number:
        print('Good job!,you guessed in ' + str(guess_taken) + ' guesses!')
else:
        print('Nope, the number I was thinking of is '+ str(secret_number))
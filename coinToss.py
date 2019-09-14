import random

money = 100

print("Hello, and welcome to the coin toss game! I hope you're having a lovely day")
print("What is your name? :")
name=input()
print("Hello, "+name)
print("How much would you like to bet (max. bet £100)? ")
bet=input()
print("Heads or Tails? ")
guess = input().lower().strip()
flip=random.randint(1,2)


def coin_toss(guess,bet):
    # Heads is 1, Tails is 2
    if guess == "heads" and flip==1:
        print("Heads! You win £"+bet)
    if guess=="tails" and flip==1:
        print("Heads... You lose £"+bet)
    if guess=="tails" and flip==2:
        print("Tails! You Win "+bet)
    if guess=="heads" and flip==2:
        print("Tails... You lose £"+bet)
                  
print(coin_toss(guess,bet))

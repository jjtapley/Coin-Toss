import random

money = 100
flip=random.randint(1,2)



#Introduce game, ask user for name, bet amount and guess:
print("Hello, and welcome to the coin toss game! I hope you're having a lovely day")
print("What is your name? :")
name=input()
print("Hello, "+name)
print("How much money do you have?")
balance = input("£")
try_again = "yes"

#While loop - run the bet and guess while user wants to continue playing
while try_again=="yes":
    print("How much would you like to bet (max. bet 100)? (enter number between 1 and 100)")
    bet=input("£")
    if int(bet)>0 or int(bet)<=100:
        print("You have bet " +str(bet))
    while int(bet)<=0 or int(bet)>100:
            print("Bet must be between 1 and 100")
            bet=input()
            print("You have bet " +str(bet))
    print("Heads or Tails? ")
    guess = input().lower().strip()


#Function - defines the outcome of the flip compared to the guess

    def coin_toss(guess,bet):
    # Heads is 1, Tails is 2
        if guess == "heads" and flip==1:
            print("Heads! You win £"+bet)
        if guess=="tails" and flip==1:
            print("Heads... You lose £"+bet)
        if guess=="tails" and flip==2:
            print("Tails! You Win £"+bet)
        if guess=="heads" and flip==2:
            print("Tails... You lose £"+bet)


#Runs the function using the guess and bet amount as parameters
        print(coin_toss(guess,bet))

#Gives user their balance leftover:

    if (guess == "heads" and flip==1) or (guess=="tails" and flip==2):
        balance=(int(balance)+int(bet))
        print("You now have £" + str(balance) + "!")
    if (guess=="tails" and flip==1) or (guess=="heads" and flip==2):
        balance=(int(balance)-int(bet))
        print ("Unlucky, you lose. Your new balance is £" + str(balance))


#Asks user if they would like to try again

    print ("Would you like to try again?")
    try_again=input().lower().strip()

#When user is finished playing, the game will end
else:
    print ("Thanks for playing! Have a great day")

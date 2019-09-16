import random

money = 100
flip=random.randint(1,2)



#Introduce game, ask user for name, bet amount and guess:
print("Hello, and welcome to the coin toss game! I hope you're having a lovely day!")
print("What is your name? :")
name=input()
#Make sure name is string, not int:
while (name.isdigit()):
    print("That's a number! What's your name?")
    name=input().strip()
print("Hello, "+name)
print("How much money do you want to start with? (Choose a value between £1 and £10,000")
balance = input("£")

#Make sure balance is an int between 1 and 10000:
while balance.isalpha() or int(balance)<0 or int(balance)>10000:
    print ("Unexpected error - please enter a value between £1 and £10,000")
    balance = input("£")
if balance.isdigit() and int(balance) >0 and int(balance)<=10000:
    print("You are starting with £" + str(balance) +". Good luck!")

try_again = "yes"

#While loop - run the bet, guess and flip function while user wants to continue playing
while try_again=="yes":
    print("How much would you like to bet? (this cannot be more than your current balance)")
    bet=input("£")
    while bet.isalpha() or int(bet)>int(balance):
        print ("Please enter a number between £1 and £" + str(balance))
        bet = input("£")
    if int(bet)< int(balance) or int(bet)>0:
        print("You have bet " +str(bet))
    #Check bet and compare to balance - bet cannot be higher than balance
    while int(bet)>int(balance):
           print ("You do not have enough money for that bet - please bet an amount between £1 and £" + str(balance))
           bet=input()
    while int(bet)<=0 or int(bet)>int(balance):
            print("Bet must be a number between 1 and " + str(balance))
            bet=input()
            print("You have bet " +str(bet))
    print("Heads or Tails? ")
    guess = input().lower().strip()
    if guess == guess.isdigit():
        print ("Please type heads or tails")


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
    if balance <=0:
        try_again == "no"
        print ("""
Oh, no. You do not have any money left!
Thanks for playing.
GAME OVER""")
        break


#Asks user if they would like to try again

    print ("Would you like to try again?")
    try_again=input().lower().strip()



#When user is finished playing, the game will end
else:
    print ("Thanks for playing the Coin Toss Game! Your final balance is £" + str(blanace) +". Have a great day")

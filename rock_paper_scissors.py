import random
options=('Rock','Paper','Scissors')

running=True

while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter a choice(rock,paper or scissors): ")

        print("Player:",player)
        print("Computer:",computer)
        
        if player==computer:
            print("Its a tie!")
        elif player=='Rock' and computer=='Scissors':
           print("You Win!")
        elif player=='Paper' and computer=='Rock':
            print("You Win!")
        elif player=='Scissors' and computer=='Paper':
            print("You Win!")
        else:
            print("You LOst")

        if not input("Play again? (yes or no): ").lower()=='yes':
            running =False        
        

print("Thanks for Playing!")




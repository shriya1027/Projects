import random

#using ASCII ART and Unicode characters
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2518 \u2514")

dict={
1:  (  "┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),

2:  (  "┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),

3:  (  "┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),

4:  (  "┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),    

5:   ( "┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"), 

6:  ( "┌─────────┐",
      "│ ●     ● │",
      "│ ●     ● │",
      "│ ●     ● │",
      "└─────────┘") ,    
}
dice=[]
total=0

num_of_dice=int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in range(num_of_dice):
    for line in dict.get(dice[die]):
       print(line)

  
for die in dice:
    total+=die
print("total:",total)




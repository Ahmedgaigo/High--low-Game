from art import *
from replit import clear
from game_data import data
import random as r
    
game = False
while not game:
    score = 0
    

    rand = r.randint(0, 49)
    
    end = False
    while not end:
        print(logo)
        Rand = r.randint(0, 49)
        Name = data[Rand]['name']
        Description = data[Rand]['description']
        Country = data[Rand]['country']
        Follower_count = data[Rand]['follower_count']

        name = data[rand]['name']
        description = data[rand]['description']
        country = data[rand]['country']
        follower_count = data[rand]['follower_count']
        
        print(f"Compare A: {name}, a {description}, from {country}, followers: {follower_count} Million ")
        print(f"           {vs}")
        print(f"Against B: {Name}, a {Description}, from {Country}")
        follower = input("Who has more followers? 'A' or 'B': ").lower()
        
        a = data[rand]['follower_count']
        b = data[Rand]['follower_count']
        if (a >= b and follower == 'a') or (b >= a and follower == 'b'):
            score += 1
            print(f"\n{name} has {a} Million followers\n {Name} has {b} Million followers") 
            clear()
            print(f"You're right.current score: {score}")
            rand = Rand
            
        else:
            clear()
            print(f"\n{name} has {a} Million followers\n {Name} has {b} Million followers\n sorry, that's wrong. Final score: {score}")
            end = True

    restart = input("Type 'r' to restart or 'c' to end the game: ")
    if restart == 'r':
        clear()
    else:
        clear()
        print(over)
        game = True

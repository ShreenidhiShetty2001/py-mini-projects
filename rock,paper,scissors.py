#[(D,Rock,Rock),(S,Rock,Paper),(U,Rock,Scissors),(U,Paper,Rock),
#(D,Paper,Paper),(S,Paper,Scisoors),(S,Scissors,Rock),(U,Scissors,Paper),(D,Scissors,Scissors)]
import random

user_score = 0
system_score = 0
options = ['Rock','Paper','Scissors']
print("Are you ready to play?")
ans = input()
if(ans != 'yes'):
    quit()

while(True):
    user_choice = input("Choose Rock, Paper, Scissors or q(quit)\n")
    if(user_choice == 'q'):
        quit()
    else:
        ran_num = random.randint(0,2)
        system_choice = options[ran_num]
        print("system choice: "+system_choice)
        print("user choice: "+user_choice)

        if((user_choice == 'Rock' and system_choice == 'Rock') or (user_choice == 'Paper' and system_choice == 'Paper') or(user_choice == 'Scissors' and system_choice == 'Scissors')):
            print("It's a draw")
    
        elif((user_choice == 'Rock' and system_choice == 'Paper') or (user_choice == 'Paper' and system_choice == 'Scissors') or (user_choice == 'Scissors' and system_choice == 'Rock')):
            print("System wins")
            system_score += 10
    
        else:
            print("user wins")
            user_score += 10
        
        v = input("Do you want to play again?\n")
        if(v != 'yes'):
            break

print("TOTAL SCORE")
print("SYSTEM SCORE : " +str(system_score))
print("USER SCORE : " +str(user_score))


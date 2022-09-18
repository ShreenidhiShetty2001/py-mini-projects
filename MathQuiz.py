#quiz mini projects here user is asked certain questions, depending on the number of correct answers they give score wil be calculated.
#what should the quiz be about? Math problems
#number of questions? 5
#each question arries 10 points so the score will be evaluated out of 50


score = 0
print("Do you want to play the game?")
playing = input()
if( playing != 'yes'):
    quit()

while(True):
    print("Solve the following questions")
    val = int(input(" 1. (15*6)*(123*2)?\n"))
    if(val == 22140):
        score += 10
        print("Good job!! 22140 is the right answer") 
    else:
        print(str(val)+" is incorrect, better luck next time!")

    print("\n")

    val = int(input("2. ((6**2) * (12/6))/6\n"))
    if(val == 12):
        score += 10
        print("Good job!! 12 is the right answer")
    else:
        print(str(val)+" is incorrect, better luck next time!")

    print("\n")

    val = int(input("3. (7**3)/7\n"))
    if(val == 49):
        score += 10
        print("Good job!! 49 is the right answer")
    else:
        print(str(val)+" is incorrect, better luck next time!")

    print("\n")

    print("you have finished playing the game")

    print("\n")

    ans = input("Do you want to play again?\n")

    if(ans != 'yes'):
        break

print("Total Score = " + str(score))

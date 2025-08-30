import random
width=50
print("="*width)
print("welcome to rock 🪨 pape 📜 scissors ✂️ game 🎮".center(width))
print("="*width)
listofchoice=["rock",'paper','scissor']
userchoice=None
computerchoice=None
user_score,computer_score=0,0
while True:
    userchoice=input(f"Enter a valid elemet from list of elements below \n 1.Rock \n 2.Paper \n 3.scissor  \n").lower()
    computerchoice=random.choice(listofchoice)
    if userchoice=="exit":
      break
    if userchoice not in listofchoice:
        print("enter a valid choice")
        continue
    if(computerchoice==userchoice):
        print("Match tied")
        play_again=int(input("Do you want to play again if yes type 1 otherwise any key"))
        if(play_again==1):
         continue
        else:
         break
    elif(userchoice=="rock" and computerchoice=="scissor") or (userchoice=="paper" and computerchoice=="rock") or(userchoice=="scissor" and computerchoice=="paper"):
     print("you win this round")
     user_score+=1
     play_again=int(input("Do you want to play again if yes type 1 otherwise any key"))
     if(play_again==1):
         continue
     else:
       break
    else:
        print("computer win this round")
        play_again=int(input("Do you want to play again if yes type 1 otherwise any key"))
        computer_score+=1
        if(play_again==1):
         continue
        else:
         break
if(user_score>computer_score):
    print("you win after all rounds")
elif(user_score==computer_score):
    print("Its a tie ")
else:
    print("computer wins")

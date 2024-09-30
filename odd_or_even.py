# a program to play odd or even game
import random #to select random numbers and things
from datetime import datetime # to print current date and time

def printf(list):  #to print a list of elements line by line
    for i in list:
        if i.isupper():
            print(i.center(50)) # to print the heading which is in capital letters at the center
        else:
            print(i)

def rules(): #to print the rules and regulations
    rule=["*"*75,"RULES","*"*75,"\n","GAME OVERVIEW","\n","1. Inspired from cricket","2. Game divided into two halves: batting and bowling","3. Virtual coin toss determines the first half's role","\n"*2,
          "BATTING HALF","\n","1. User selects an integer between 0 and 10","2. jack generates a random integer between 0 and 10 (no bias)","3. If user's and jack's numbers match, user is out and bowling half begins","4. If numbers don't match, user scores a run (point) and continues batting","5. User bats for 10 overs (60 balls) or getting out","6. Total runs scored are accumulated","\n"*2,
          "BOWLING HALF","\n","1. User selects an integer between 0 and 10","2. jack generates a random integer between 0 and 10 (no bias)","3. jack scores a run if user fails to match jack's number.","4. jack continues batting until:","  - 10 overs (60 balls) are completed without achieving target","  - 10 overs (60 balls) are completed without achieving target","5. If jack fails to achieve target or user matches jack's number, user wins","\n"*2,
          "GAME OUTCOME","\n","1. User wins if:","  - jack fails to score 1 more run than user's total runs.","  - User matches jack's number while bowling.","2. jack wins if:","  - jack scores 1 more run than user's total runs.","  - User fails to match jack's number while bowling.","\n"*2,
          "COIN TOSS","\n","1. Virtual coin toss determines whether user bats or bowls first.","2. User inputs 'h' for heads or 't' for tails to simulate coin toss.","-"*75]
    printf(rule)

def welcm_note(): #to print welcome note, here jack named bot is the competent for the user
    note=["-"*75,"WELCOME","ODD OR EVEN","-"*75,"\n","hey, i am jack, your companion. Are you ready to compete with me !.."]
    printf(note)

def coin_toss(): # to decide who to do what first in fair way
    coinpr=["COIN TOSS","enter h for heads, t for tails".center(50),"\n"]
    printf(coinpr)
    while True:
        usr_coin=input("Heads or tails : ")
        if usr_coin.lower() == "h" or usr_coin.lower() == "t":
            break
        else:
            continue # to re input the value if it is wrong
    c=["h","t"]
    res=random.choice(c) # heads or tails
    print("COIN TOSS : ",end="")
    if res=="h":
        print("HEAD")
    else:
        print("TAIL")
    if usr_coin.lower()==res: # if result is favorable to user, user can choose what to do first
        while True:
            print("\nEnter a for batting and b for bowling")
            choice=input("BATTING OR BOWLING : ").lower()
            if choice == "a" or choice =="b":
                who='u'
                break
            else:
                continue
    else:
        choice=random.choice(["a","b"]) # here bot choose what to do first ramdomly
        who="b"
        if choice=="a":
            print("JACK CHOOSE BATTING".center(50))
        else:
            print("JACK CHOOSE BOWLING".center(50))
    return choice,who

def user_input(): # a function that allows user to input their run (value)
    print()
    while True:
        try: #to check and correct users input
            while True:
                user_num = int(input("Enter your run(0-10) : "))
                if user_num > 10 or user_num < 0: # user can only input a number from 0 to 10
                    print("Select a run between 0 to 10 !")
                    continue
                else:
                    return user_num # to re input if entered value is out of boundary
            break
        except ValueError as e:
            print(f"Error : {e}")


def batting(shalf,tscore): # a function for users to bat and jack will bowl
    over=10 # pre defined overs and balls to make the game short
    balls=60 #shalf = is this second half, tscore = if shalf, that score to be beated
    runs=0 # variable to store the runs scored by the user
    while balls>0:
        user_num=user_input() # user to input their run
        jack_num=random.randint(0,10) #bot will choose a number randomly (0-10)
        print(f"bolled number : {jack_num}")
        if user_num != jack_num : # if both numbers aren't a match, then user score that run
            balls-=1
            runs += user_num
            if balls%6==0:
                over-=1
            if shalf==True: # a special condition to check whether this is batted in second half
                if runs>tscore: # if so, there will a target scored by bot in first half that to be beated in this round
                    print("YOU WIN".center(50))
                    win="USER"
                    break
            win=None
        else: # if both numbers are a match, then the user is out
            print("OUT".center(50))
            win=None
            break
    if shalf==True and runs<tscore: # if balls are over in the second half and user couldn't score the target,user fails
        print("YOU LOOSE, DIDN'T OBTAIN REQUIRED RUNS")
        print("JACK WINS !!..")
        win="JACK"
    return over,balls,runs,win # for the scorecard

def bowling(shalf,tscore): # a function for users to bowl and jack will bat
    over =10
    balls=60
    runs=0
    while balls>0:
        user_num=user_input()
        jack_num=random.randint(0,10)
        print(f"jack's run : {jack_num}")
        if user_num != jack_num :
            runs+=jack_num
            balls-=1
            if balls%6==0:
                over-=1
            if shalf==True: # second half condition
                if runs>tscore:
                    print("YOU LOOSE".center(50))
                    win="JACK"
                    break
            win=None
        else:
            print("JACK OUT".center(50))
            win=None
            break
    if shalf==True and runs<tscore:
        print("JACK LOOSE, DIDN'T OBTAIN REQUIRED RUN")
        print("USER WINS !!..")
        win="USER"
    return over,balls,runs,win

def history(): #to print history gamesplay
    print("HISTORY".center(50))
    txt=open('scorehistory.txt','r')
    his=txt.readlines()
    for i in reversed(his):
        print(i)
    txt.close()

def history_des(win,who1,runs1,balls1,who2,runs2,balls2): # a function to re assign the detains for history
    if win==who1:
        win,winrun,winball,lsr,lsrrun,lsrball=who1,runs1,60-balls1,who2,runs2,60-balls2
    else:
        win,winrun,winball,lsr,lsrrun,lsrball=who2,runs2,60-balls2,who1,runs1,60-balls1
    return win,winrun,winball,lsr,lsrrun,lsrball



def scorecard(who,choice,over1,balls1,runs1,over2,balls2,runs2,win): # a function to display the game details
    if choice=="a" and who=="u" or choice=="b" and who=="b": # condition to check who batted and bowled first
        who1,who2="USER","JACK" #who1 batted and who2 bowled in the first half, and the reverse happens in the second half
    else:
        who1,who2="JACK","USER"
    print()
    win,winrun,winball,lsr,lsrrun,lsrball=history_des(win,who1,runs1,balls1,who2,runs2,balls2)
    wonrun=winrun-lsrrun # the run by which the winner won
    txt=open('scorehistory.txt','+a')
    txt.write(f"{datetime.now()}   {win}({winrun}/{winball}) bt {lsr}({lsrrun}/{lsrball} by {wonrun})\n")
    txt.close()
    print("-"*75,"\n","SCORECARD".center(50),f"\n\n FIRST HALF \n BATSMAN = {who1}, BOWLER = {who2} scored {runs1} RUNS in {60-balls1}balls,{10-over1} OVERS "
                                 f"\n SECOND HALF \n BATSMAN = {who2}, BOWLER = {who1} scored {runs2} RUNS in {60-balls2}balls,{10-over2} OVERS","\n","-"*75)
    print()
    print()
    history()

def main(): #the main function that governs the game
    welcm_note() # to print the welcome note
    print() # print() is used to make CLI more beautiful
    while True:
        want_rule=input("Do you want to see the RULES (y/n) : ").lower()
        if want_rule=="y":
            rules()
            break
        elif want_rule=="n":
            break
        else:
            continue
    print("\n"*2)
    while True: # main game starts
        choice,who=coin_toss() # coin is tossed
        print()
        print("GAME STARTS".center(50))
        print()
        if choice=="a" and who=="u" or choice=="b" and who=="b": # condition for making who to do what first according to coin toss
            print("BATSMAN : USER , BOWLER : JACK".center(50))
            over1,balls1,runs1,win=batting(False, None)
            print("\n","SECOND HALF".center(50),"\n",f"RUNS TO BE SCORED : {runs1}","\n")
            print("BATSMAN : JACK , BOWLER : USER".center(50))
            over2,balls2,runs2,win=bowling(True,runs1)
        else:
            print("BATSMAN : JACK , BOWLER : USER".center(50))
            over1,balls1,runs1,win=bowling(False,None)
            print("\n", "SECOND HALF".center(50), "\n",f"RUNS TO BE SCORED : {runs1}","\n")
            print("BATSMAN : USER , BOWLER : JACK".center(50))
            over2,balls2,runs2,win=batting(True,runs1)

        scorecard(who,choice,over1, balls1, runs1, over2, balls2, runs2,win)
        print()
        play_again=input("Do you want to play again (y/n) : ").lower()
        if play_again == "y":
            print("\n","-"*75,"\n")
            continue
        else:
            break


main()


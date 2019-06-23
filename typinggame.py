## 1) Function for each round of typing
def gameround(speed,text,score):
 ## 2) Ask if they are ready
 throwawayvariable = input("You will be given a message, type it back. \nNot only does it have to be perfect it has to be done in less than {} seconds!\nClick Enter to Begin  ".format(speed))
 
 
 ## 3) Start Timer
 start=default_timer()
 
 
 ## 4) Give them the text to repeat
 typetext=input("TYPE THE TEXT::: {} \n".format(text))
 
 
 ## 5) Stop Timer, calculate the total

 stop=default_timer()
 totalTime = stop - start
 print("YOUR TIME {} \n".format(totalTime))
 
 ## 6) Who won, update score
 if(typetext==text and totalTime<speed):
     print("YOU GO BOY!!!!!!! \n")
     score[0]=score[0]+1
 else:
     print("FUCK!!!!!!!! \n")
     score[1]=score[1]+1
 
 ## 7) Return Score
 return score
 
 
################## Main Body ######################

## Take care of any importing I need to

from timeit import default_timer
import random

##  Create Scorboard

score = [0,0]

##  Create Lists of Words to Type

masterlist = ['8675309', 'shubham anand', 'this is my first python project', 'okay type this fast']

## Game Loop
while True:
 ## Check Score: Either Break or Feed that Function!
    if(score[0]==2 or score[1]==2):
         if(score[0]==2):
            print("I FUCKED COMPUTER")
         if(score[1]==2):
            print("YOU ARE A DISGRACE")
         break
    else:
            textspeed=random.randint(7,20)
            a=random.randint(0,3)
            texttype=masterlist[a]
            score=gameround(textspeed,texttype,score)
            print("YOUR SCORE {} \n".format(score[0]))
            print("COMPUTER SCORE {} \n".format(score[1]))




            
    
        
   

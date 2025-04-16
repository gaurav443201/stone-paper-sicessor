import random

'''
1 for stone 
-1 for paper
0 for scissor'''

computer = random.choice([-1, 0 ,1 ])
youst = input("Enter your choise: ")
youDict = {"s":1, "p":-1, "sr":0}
reverseDict = {1:"Stone", 0:"Scissor", -1:"Paper"}
you = youDict[youst]

#by now we have 2 numbers(variables), you and computer.
print(f"you chose {reverseDict[you]} \ncomputer chose {reverseDict[computer]}") 
                    
if(computer == you):
    print("It's a draw")
'''                           (computer +you)   (computer- you)
else:                                   sum     subtract
    if(computer== -1 and you==0):       -1         -1
        print("YOU WIN!")
    elif(computer== -1 and you == 1):    0         -2
        print("YOU LOSE !")    
    elif(computer== 1 and you== -1):     0          2
        print("YOU WIN!")
    elif(computer== 1 and you == 0):     1          1
        print("YOU LOSE !")    
    elif(computer== 0 and you==1):       1         -1
        print("YOU WIN!")
    elif(computer== 0 and you == -1):   -1          1
        print("YOU LOSE !")    

    else:
        print("something went wrong")     

       
'''
# the bellow logic is written as the basics of (computer - you)
if((computer - you) == -1 or (computer - you ==2)):
    print("You win")
else:
    print("You lose")

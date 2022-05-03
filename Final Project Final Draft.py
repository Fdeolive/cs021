#Author: Fernanda De Oliveira Girelli
#CS021 Section B Final Project
#This program runs a game of guess who with Grey's Antatomy characters between the user and the computer



import random

#Randomizers the computer and the user's character from a list of Grey's Antatomy character
def character_random():
    character_list=("Meredith Grey","Derek Shephard","Christiana Yang","Izzie Stevens","Mark Sloan","Miranda Bailey","George O'Malley", "Alex Karev")
    
    character_computer=random.choice(character_list)
    character_user=random.choice(character_list)
    
    return(character_computer,character_user)


#Questions asked by the computer
def question_computer(number,character,potential):
    #Asks the user a question
    if number==1:
        user_answer=input("Is your character female?")
    if number==2:
         user_answer=input("Did you charater die?")
    if number==3:
        user_answer=input("Is your character part of the 5 interns?")
    if number==4:
        user_answer=input("Is your character still on the show")
    while user_answer!="y" and user_answer!="n":
        user_answer=input("Please enter valid reponse (y/n)")



#Interates through the dictionary and removes character that does not match the user's answer 
    
    for key in character.keys():
       if character[key].get(number)!=user_answer:
         try:    
             potential.remove(key)
         except:
             pass
   
    return(potential)


    
    

#Questions asked by the user-returns yes or no depending on the character the computer recives and the question
def question_user(numb,com_char):
    character={"Meredith Grey":{1:"Yes",2:"No",3:"Yes",4:"Yes"},"Derek Shephard":{1:"No",2:"Yes",3:"No",4:"No"},"Christiana Yang":{1:"Yes",2:"No",3:"Yes",4:"No"},"Izzie Stevens":{1:"Yes",2:"No",3:"Yes",4:"No"},"Mark Sloan":{1:"No",2:"Yes",3:"No",4:"No"},"Miranda Bailey":{1:"Yes",2:"No",3:"No",4:"No"},"George O'Malley":{1:"No",2:"Yes",3:"Yes",4:"No"}, "Alex Karev":{1:"No",2:"No",3:"Yes",4:"No"}}
    return(character[com_char][numb])


def main():
    #Rules for the Game
    print("Welcome to Guess Who-Greys Antatomy Edition")
    print("\nRULES:\n1. Both you and the computer randomly get assigned a character from the list \nMeredith Grey,Derek Shephard,Christiana Yang,Izzie Stevens,Mark Sloan,Miranda Bailey,George O\'Malley, Alex Karev \n2. Every round both you and the computer gets to ask 1 yes or no question.v\n3.Only answer questions with y or n \n4. You only get the chance to guess the character once per game if you loose the game is over.")
    print("\nQuestions Asked.\n1.Is your character female?\n2.Did you charater die?\n3.Is your character part of the 5 interns?\n4.Is your character still on the show")

    play=input("\nDo you want to play? (Y/N)")
    while play=="Y" or play=="y":
            
        #Character gets Assigned
        attempt=character_random()
       
        print(f'Your character is {attempt[1]}')

        print("\nComputer will start:")

        com_guess="n"
        user_guess="n"
        list1=[1,2,3,4]
        character_list1=["Meredith Grey","Derek Shephard","Christiana Yang","Izzie Stevens","Mark Sloan","Miranda Bailey","George O'Malley", "Alex Karev"]
        anatomy={"Meredith Grey":{1:"y",2:"n",3:"y",4:"y"},"Derek Shephard":{1:"n",2:"y",3:"n",4:"y"},"Christiana Yang":{1:"y",2:"n",3:"y",4:"n"},"Izzie Stevens":{1:"y",2:"n",3:"y",4:"n"},"Mark Sloan":{1:"n",2:"y",3:"n",4:"n"},"Miranda Bailey":{1:"y",2:"n",3:"n",4:"y"},"George O'Malley":{1:"n",2:"y",3:"y",4:"n"}, "Alex Karev":{1:"n",2:"n",3:"y",4:"n"}}
       
        
        while user_guess=="n" and com_guess=="n":
        #Makes the computer take a guess when it runs out of questions
            try:
                computer_num=random.choice(list1)
                hey=question_computer(computer_num,anatomy,character_list1)
                #print(hey)

            
                if len(hey)<=1:
                    com_guess=random.choice(hey)
                    print("Computer going to take a guess")
                    print(f'Computer Guessed: {com_guess}')
                    if com_guess==attempt[1]:
                        print("Computer guessed right!, you lose! ")
                        play=input("\nDo you want to play again? (Y/N)")
                    else:
                        print("Computer guessed wrong, you win!")
                        play=input("\nDo you want to play again? (Y/N)")
                else:
                    list1.remove(computer_num)
                    user_input=int(input("\nChoose a number that correlates to the question you want to ask from the list? (1-4)"))

                    people=question_user(user_input,attempt[0])
                    print(people)
                    
                    user_guess=input("\nDo you want to guess? (Y/N)")
                    if user_guess=="y" or user_guess=="Y":
                        user_characters=input("Guess character: ")
                        if user_characters==attempt[0]:
                            print("You win!")
                            play=input("Do you want to play again? (Y/N)")
                        else:
                            print("You Lose!")
                            print(f'The computer\'s charcater was {attempt[0]}')
                            play=input("Do you want to play again? (Y/N)")
                
            except:
                    
                com_guess=random.choice(hey)
                print("Computer going to take a guess")
                print(f'Computer Guessed: {com_guess}')
                if com_guess==attempt[1]:
                    print("Computer guessed right!, you lose! ")
                    play=input("/nDo you want to play again? (Y/N)")
                else:
                    print("Computer guessed wrong, you win!")
                    play=input("\nDo you want to play again? (Y/N)")

    
main()
 
           
                
    

#add more questions: maybe potential wont need it because computer will guess if run out of question
#CHnage the dictionary from yes and no to y or n
#add comments and author/summary line 
    


    

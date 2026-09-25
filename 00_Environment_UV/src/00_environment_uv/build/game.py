#details about the program in base file
import random
import datetime

from enum import Enum

class Difficulty(Enum):
    EASY = 'easy'
    MEDIUM = 'mid'
    HARD = 'hard'
    EXTREME = 'ex'

    def select_dificulty(self, diff: str, difficulty: Difficulty=0):
        if (diff == "easy") :
            return self.EASY
        elif (diff == "mid") :
            return self.MEDIUM
        elif (diff == "hard") :
            return self.HARD
        elif (diff == "ex") :
            return self.EXTREME
        else:
            return None

#global variables
score: list[int] = []
difficulty: Difficulty = Difficulty.EASY
round_no: int = 1 
compelete_score: dict[int, int] = {}


#prints the score for the user
def print_score () -> None :
    global round_no
    totalaccuray = 0

    print("Your score of accuray of each round is :")
    for round, score in compelete_score.items() :
        print(f"Round {round} : {score}") #prints round with its accuray
        totalaccuray += score

    overallaccuray = (totalaccuray / (round_no-1))
    compelete_score[0] = overallaccuray

    print(f"Overall accuray : {overallaccuray}")
    print()
    return
#end

#fuction to calculate the score
def calcu_score (triestaken, tries) -> None :
    global round_no, compelete_score

    accuray = (100 - ( ( (triestaken-1)/ tries) * 100))
    compelete_score[round_no] = round(accuray, 2)
    return
#end


def guessing (tries: int, n: int, guessing_range: int) -> None :
    triestaken = 1
    print(n)
    for _ in range(tries) : 
        gno_str = input("Enter a number: ")
        while not gno_str.strip():
            # Check if the input is not empty
            gno_str = input('Invalid input, please enter a valid number :')
        
        gno = int(gno_str)
        
        if(n == gno) :
            print(f"You won, it took you : {triestaken} tries")
            break
        
        elif((n-gno) > 0) : #if the gno is smallerq
            triestaken += 1
            if((n - gno) > guessing_range) :
                print("too low")
                continue 
            print("little low")
        
        else : #if gno is greater
            triestaken += 1
            if((n-gno) < (-guessing_range) ):
                print("too high")
                continue 
            print("little high")
        
    else :
        print(f"You lost, the number was {n} ")
        #manage till here
        
    print()
    calcu_score(triestaken, tries)
    return

#base Diffuculty_args  func
def Diffuculty_args (max_tries: int, range_max: int, guessing_range: int) -> None:
    global difficulty
    tries = Trys_Input(max_tries)
    n = random.randint(1, range_max)  # n is our generated number
    guessing(tries, n, guessing_range)
    return 


def Trys_Input (upper_bound)  -> int:
    print("Enter the number tries you will need :", end=" ")
    while True :
        tries_str = input()
        if not tries_str.strip() :
            print("Enter a valid number")
            continue
        
        tries = int(tries_str) 
        if not(5 <= tries <= upper_bound ) :
            print("Enter a valid number")
        else:
            break
        
    return tries
#end of Trys_Input function


def change_difficulty()  -> None:
    diff_check = input("Do you want to change the difficulty (type 1 for yes) :")
    if(diff_check == "1") :
        Difficulty_Selector()
    else :
        Difficulty_Selector(take_input=False)
#end

def Try_again() -> None:
    play_again = input("Do want to try again (type 1 for yes) : ")
    print()

    if(play_again == "1") :
        change_difficulty()
        return

    print_score()
    print("Thanks for playing")
    return
#end


def Difficulty_Selector (take_input: bool=True) -> None :
    global round_no, difficulty

    while True : 
        if take_input:
            difficulty = Difficulty.EASY.select_dificulty(input("Enter difficulty (easy, mid, hard, ex) : "))

            if difficulty:
                break
        else:
            break
    
    if (difficulty == Difficulty.EASY) :
        Diffuculty_args (20, 100, 20)
    elif (difficulty == Difficulty.MEDIUM) :
        Diffuculty_args (15, 150, 25)
    elif (difficulty == Difficulty.HARD) :
        Diffuculty_args (10, 200, 35)
    elif (difficulty == Difficulty.EXTREME) :
        Diffuculty_args (5, 300, 45) 

    round_no += 1
    Try_again()
    return
#end of Difficulty_Selector function


def Starting_Instructions() -> None:
    print("INSTRUCTIONS:")
    print("In this program a you need to guess a randomly generated number and minimun tries are 5")
    print()

    print("There are 4 difficulties: easy, medium (mid), hard, exterme (ex)")
    print()

    print("EASY mode rules :")
    print("In it you have to guess a munber b/w 1 to 100")
    print("If the guessed number it more or less than the selected number by more than 20 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 20 or less then the screen will show high or low respectively")
    print("And you get maximum of 20 tries")
    print()

    print("MEDIUM mode rules :")
    print("In it you have to guess a munber b/w 1 to 150")
    print("If the guessed number it more or less than the selected number by more than 25 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 25 or less then the screen will show high or low respectively")
    print("And you get maximum of 15 tries")
    print()

    print("HARD mode rules :")
    print("In it you have to guess a munber b/w 1 to 200")
    print("If the guessed number it more or less than the selected number by more than 35 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 35 or less then the screen will show high or low respectively")
    print("And you get maximum of 10 tries")
    print()

    print("EXTREME mode rules :")
    print("In it you have to guess a munber b/w 1 to 300")
    print("If the guessed number it more or less than the selected number by more than 45 then the screen will show too high or too low respectively")
    print("If the guessed number it more or less than the selected number by 45 or less then the screen will show high or low respectively")
    print("And you get 5 tries")
    print()

    return
#end of Starting_Instructions function

def main() -> None:
    Starting_Instructions()
    Difficulty_Selector()

    return

if __name__ == "__main__":
    main()
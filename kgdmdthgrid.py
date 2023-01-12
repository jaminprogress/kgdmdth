#import dictionary of all the available cards
from cards import Cards

#class for all needed parsing of cards
class CardBoard:
    def __init__(self, name, position, L, R, T, B, requirements):
        self.name = name
        self.position = position
        self.L = L
        self.R = R
        self.T = T
        self.B = B
        self.requirements = requirements

#function to convert card from dict to CardBoard class and place on the board
def place(position, card, Cards, board):
    board[position]=CardBoard(card, position, Cards[card]['L'], Cards[card]['R'], Cards[card]['T'], Cards[card]['B'], None)
    return board;

def remove(board, position):
    board[position]=blank

def printboard(board):
    print("\n")
    print(board["1"].name," | ", board["2"].name," | ",  board["3"].name)
    print(" ")
    print(board["4"].name," | ",  board["5"].name," | ",  board["6"].name)
    print(" ")
    print(board["7"].name," | ",  board["8"].name," | ",  board["9"].name)
    print("\n")

#function to add a card onto the board - continues until all cards have been placed
def addcard(board):
    cont = "Y"
    while cont == "Y":
        cardname = input("What is the name of the card?  ")
        position = input("What position would you like to place the card in (1-9)?  ")
        place(position, cardname, Cards, board)
        cont = input("Would you like to place another card? Y/N  ")
    board, affinitycount = resolve(board)
    return board, affinitycount

def resolve(board):
    affinitycount = {"Red":0, "Blue":0, "Green":0}
    #check for matching pips on cards
    checkside(board["1"].R,board["2"].L, affinitycount) #1-2
    checkside(board["2"].R,board["3"].L, affinitycount) #2-3
    checkside(board["1"].B,board["4"].T, affinitycount) #1-4
    checkside(board["4"].R,board["5"].L, affinitycount) #4-5
    checkside(board["2"].B,board["5"].T, affinitycount) #2-5
    checkside(board["5"].R,board["6"].L, affinitycount) #5-6
    checkside(board["3"].B,board["6"].T, affinitycount) #3-6
    checkside(board["4"].B,board["7"].T, affinitycount) #4-7
    checkside(board["7"].R,board["8"].L, affinitycount) #7-8
    checkside(board["5"].B,board["8"].T, affinitycount) #5-8
    checkside(board["8"].R,board["9"].L, affinitycount) #8-9
    checkside(board["6"].B,board["9"].T, affinitycount) #6-9

    print("These are the affinities in your inventory: ", affinitycount)
    return(board, affinitycount)


def checkside(pip1,pip2, affinitycount):
    if pip1 and (pip1 == pip2):
        affinitycount[pip1] +=1
    return affinitycount


blank = CardBoard("None", None, None, None, None, None, None)

board = {"1":blank,"2":blank,"3":blank,"4":blank,"5":blank,"6":blank,"7":blank,"8":blank,"9":blank}

board, affinitycount = addcard(board)

printboard(board)
print("Your affinity count for your inventory is: Red: ", affinitycount["Red"]," Blue: ", affinitycount["Blue"], " Green: ", affinitycount["Green"])





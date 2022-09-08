#Python Tic-Tac-Toe game
"""Plays a game of Tic-Tac-Toe with a user"""
import os,random,time

def pickChar(cellvalue):
    """takes the value of a given cell on the board and returns an appropriate character to assign to that space"""
    #define the characters that will appear in the cells, indexes 0 to 6 from top to bottom
    xchar = ["        "," XX  XX ","  XXXX  ","   XX   ","  XXXX  "," XX  XX ","        "]
    ochar = ["        ","  OOOO  "," OO  OO "," OO  OO "," OO  OO ","  OOOO  ","        "]
    bcell = ["        ","        ","        ","        ","        ","        ","        "]
    
    if cellvalue == "x":
        return xchar
    elif cellvalue == "o":
        return ochar
    else:
        return bcell

def drawBoard(currentboard):
    """draws the current state of the tic tac toe board"""
    #assign display characters to the nine spaces on the board, according to the curent state of the board
    ba1 = pickChar(currentboard[0]) #pick a list from def pickChar, depending on the value of the space of A1
    ba2 = pickChar(currentboard[1])
    ba3 = pickChar(currentboard[2]) #end of Row A
    bb1 = pickChar(currentboard[3])
    bb2 = pickChar(currentboard[4])
    bb3 = pickChar(currentboard[5]) #end of Row B
    bc1 = pickChar(currentboard[6])
    bc2 = pickChar(currentboard[7])
    bc3 = pickChar(currentboard[8]) #end of Row C
    
    #Row headings
    Achar = ["        ","   AA   ","  A  A  "," AAAAAA "," AA  AA "," AA  AA ","        "]
    Bchar = ["        "," BBBBB  "," BB  BB "," BBBBB  "," BB  BB "," BBBBB  ","        "]
    Cchar = ["        ","  CCCC  "," CC  CC "," CC     "," CC  CC ","  CCCC  ","        "]
    
    #draw the board's current state
    print("\n")
    for lines in range(0,7): 
        print("  " + Achar[lines] + " " + ba1[lines] + " # "  + ba2[lines] + " # " + ba3[lines])
    print("\t   ######### ########## #########")
    for lines in range(0,7):
        print("  " + Bchar[lines] + " " + bb1[lines] + " # "  + bb2[lines] + " # " + bb3[lines])
    print("\t   ######### ########## #########")
    for lines in range(0,7):
        print("  " +Cchar[lines] + " " + bc1[lines] + " # "  + bc2[lines] + " # " + bc3[lines])
    
    print("\t      11         2222       3333")
    print("\t     111        22  22     33  33")
    print("\t      11           22         33")
    print("\t      11          22       33  33")
    print("\t     1111       222222      3333")

def drawHeader(player="Player",gamesplayed=[0,0,0]):
	"""draws a header to greet the player, defaults to Player in absence of any input from the player, also displays
	games played, won and lost (defaults to 0 for all values)"""
	cltm()
	print("\t********************************")
	print("\tWelcome " + player + " to Tic-Tac-Toe")
	print("\t********************************")
	print("\tGames = " + str(gamesplayed[0]) + " Won = " + str(gamesplayed[1]) + " Lost = " + str(gamesplayed[2]))

def chekCount(boardstate,currentplayer): #pass the current gameboardto the function, whose turn it is
	"""evaluates each row, column and diagonal on the board to evaluate whether a win condition is reached"""
	#cltm()
	
	#initialize the win-state list, setting all counts to 0
	totalcounts = []
	for i in range(0,8):
		totalcounts.append(0) 
	
	for t in boardstate[:3]: #count up x's or o's in first row
		if t == currentplayer:
			totalcounts[0] += 1 #total number of current player characters in Row A
	for m in boardstate[3:6]: 
		if m == currentplayer:
			totalcounts[1] += 1 #total number of current player characters in Row B
	for b in boardstate[6:]: 
		if b == currentplayer:
			totalcounts[2] += 1 #total number of current player characters in Row C
	for l in (boardstate[0],boardstate[3],boardstate[6]):
		if l == currentplayer:
			totalcounts[3] += 1 #total number of current player characters in Column 1
	for c in (boardstate[1],boardstate[4],boardstate[7]): 
		if c == currentplayer:
			totalcounts[4] += 1 #total number of current player characters in Column 2
	for r in (boardstate[2],boardstate[5],boardstate[8]):
		if r == currentplayer:
			totalcounts[5] += 1 #total number of current player characters in Column 3
	for d1 in (boardstate[0],boardstate[4],boardstate[8]): 
		if d1 == currentplayer:
			totalcounts[6] += 1 #total number of current player characters in Diagonal 1
	for d2 in (boardstate[2],boardstate[4],boardstate[6]):
		if d2 == currentplayer:
			totalcounts[7] += 1 #total number of current player characters in Diagonal 2

	if 3 in totalcounts:
		return(currentplayer.upper() + " win.") #may want to return a tuple with the winstate and human/computer win
	else:
		return("No winner.")

def cltm():
	"""checks environment script is running in and issues appropriate command to OS to clear the terminal"""
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def setPlay():
	"""asks for player preference for playing as X or O, and determines who will play first in the first game of
	tic-tac-toe by returning 0 for player going first, or 1 for the computer taking the first turn"""
	#ask for player token preference and check to see if player has entered a valid choice
	errorcode = True
	while errorcode:
		playertoken = input("\tPlease enter whether you want to play as X or O. >>>> ")
		playertoken = playertoken.lower() #forces the input here to be a lower case string
		if playertoken == "x" or playertoken == "o":
			errorcode = False
			continue
		else:
			print("\tERROR! Invalid token selected!")
	if playertoken == "x":
		comptoken = "o"
	else:
		comptoken = "x"
	#determine whether player will start the first game or take the second turn
	firstturn = random.randint(0,1)
	return[playertoken,comptoken,firstturn]

def humanMove(currentboard,playersmark):
	"""prompts human player to select a space to make their mark, takes the state of the current board and the mark that player selected, no return value"""
	errorcode = True
	while errorcode:
		playerturn = input("\n\tPlease enter your move >>> ")
		if playerturn in currentboard:
			errorcode = False
		else:
			print("\tError. That is not a legal space!")
	for index, space in enumerate(currentboard):
		if currentboard[index] == playerturn:
			currentboard[index] = playersmark
    
def computerMove(currentboard,compmark):
	"""computer selects random empty space to make its mark, takes state of current board and the computer's mark, no return value, currently does not support
	a board evaluation by the computer to make an intelligent move in response to the game's progress."""
	openspaces = legalMoves(currentboard)
	compchoice = random.choice(openspaces)
	for index, space in enumerate(currentboard):
		if currentboard[index] == compchoice:
			currentboard[index] = compmark

def play_agame(playername,gamesetup,gamecounter):
    gameplay = True #initialize game loop
    gamecounter[0] += 1
    gameboard = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] #initialize game board for new game
    wincheck = "No winner."
    #start of game loop (will be inside a main loop, eventually), but want it to play one full game, first
    while gameplay:
        drawHeader(playername,gamecounter)
        drawBoard(gameboard)
       
        #determine whom the active player is and call the appropriate function for the next move
        if gamesetup[2] == 0:
            humanMove(gameboard,gamesetup[0])
            wincheck = chekCount(gameboard,gamesetup[0])
            gamesetup[2] = 1 #pass control back to the computer player
        else:
            print("\n\tComputer is thinking.")
            computerMove(gameboard,gamesetup[1])
            time.sleep(2) #delay switch back to human player to simulate an opponent considering the consequences of the move
            wincheck = chekCount(gameboard,gamesetup[1])
            gamesetup[2] = 0 #passcontrol back to the human player
            
        #Check if the game is won by the human player or the computer
        if wincheck == "No winner.":
            spaceleft = legalMoves(gameboard)
            if len(spaceleft) != 0:
                continue #as long as there are spaces to make moves in, the game continues
            else:
                drawHeader(playername,gamecounter)
                drawBoard(gameboard)
                print(wincheck)
                gameplay = False #end the round of tic-tac-toe
        elif wincheck == "X win.":
            drawHeader(playername,gamecounter)
            drawBoard(gameboard)
            if gamesetup[0] == "x":
                print("\n\t " + playername + " has won the game!")
                gamecounter[1] += 1 #human player wins playing X, increment games won counter
            else:
                print("\n\tThe computer has won the game!")
                gamecounter[2] += 1 #computer player wins playing X, increment games lost counter
            gameplay = False #end the round of tic-tak-toe
        else:
            drawHeader(playername,gamecounter)
            drawBoard(gameboard)
            if gamesetup[0] == "o":
                #print(wincheck) #debug line
                print("\n\t " + playername + " has won the game!")
                gamecounter[1] += 1 #human player wins playing O, increment games won counter
            else:
                print("\n\tThe computer has won the game!")
                gamecounter[2] += 1 #computer palyer wins playing O, increment games lost counter
            gameplay = False #end the round of tic-tak-toe
def legalMoves(boardstate):
	"""looks at the state of the current board and returns a list of blank spaces that either the player or the
	computer may choose as a legal move"""
	legalspaces = [] #initialize a list to contain legal spaces for the next move
	for space in (boardstate):
		if space !="x" and space !="o":
			legalspaces.append(space)
	return legalspaces    

def main():
    #Application Set Up
    drawHeader()
    playername = input("\tPlease enter you name. >>> ")
    gamesetup = setPlay()
    gamecounter = [0,0,0] #initialize games played, won, lost
    keepplaying = True #initialize the main loop
    #start of main loop
    while keepplaying:
        play_agame(playername,gamesetup,gamecounter)
        #ask player if they wish to play another game, with error checking
        anothererror = True
        while anothererror:
            anothergame = input("\n\tWould you like to play another game? (y/n) >>> ")
            if anothergame.lower() == "y":
                anothererror = False
            elif anothergame.lower() == "n":
                anothererror = False
            else:
                print("\tError! " + anothergame + " is an invalid response, please select y or n.")
                
        if anothergame.lower() == "y":
            continue
        else:
            print("\tThank you for playing Tic-Tac-Toe with me!")
            keepplaying = False

#program executes below this line
main()

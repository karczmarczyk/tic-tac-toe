def visualizeField (value, idx):
    if value == "-":
        return "("+str(idx)+")"
    else: 
        return " "+value+" "

def visualize (b):
    # print ("\n")
    # print (visualizeField(b[0],1)+"\t|\t"+visualizeField(b[1],2)+"\t|\t"+visualizeField(b[2],3))
    # print (visualizeField(b[3],4)+"\t|\t"+visualizeField(b[4],5)+"\t|\t"+visualizeField(b[5],6))
    # print (visualizeField(b[6],7)+"\t|\t"+visualizeField(b[7],8)+"\t|\t"+visualizeField(b[8],9))
    # print ("\n")

    s = ""

    #line 1
    for lineNr in range (0,4):
        line = (printCell (b, 0, lineNr) 
        + printLineDivider (lineNr) 
        + printCell (b, 1, lineNr) 
        + printLineDivider (lineNr) 
        + printCell (b, 2, lineNr) 
        + "\n")
        s = s+line

    s =s+printLineX() + "\n"

    #line 2
    for lineNr in range (0,4):
        line = (printCell (b, 3, lineNr) 
        + printLineDivider (lineNr) 
        + printCell (b, 4, lineNr) 
        + printLineDivider (lineNr) 
        + printCell (b, 5, lineNr) 
        + "\n")
        s = s+line    

    s =s+printLineX() + "\n"

    #line 3
    for lineNr in range (0,4):
        line = (printCell (b, 6, lineNr) 
        + printLineDivider (lineNr) 
        + printCell (b, 7, lineNr) 
        + printLineDivider (lineNr) 
        + printCell (b, 8, lineNr) 
        + "\n")
        s = s+line    

    print (s)

    return;

def printCell (b, id, lineNr):
    if b[id] == "X":
        return printX(lineNr)
    elif b[id] == "O":
        return printO(lineNr)
    else:
        return printEmpty(lineNr, id+1) 

def printX (lineNr):
    s = [ "..##.##..",
          "...###...",
          "...###...",
          "..##.##.."]
    return s[lineNr]

def printO (lineNr):
    s = [ "...#.#...",
          "..#...#..",
          "..#...#..",
          "...#.#..."]
    return s[lineNr]

def printEmpty (lineNr, idx):
    s = [ "["+str(idx)+"]......",
          ".........",
          ".........",
          "........."]
    return s[lineNr]


def printLineDivider (lineNr):
    s = ["#","#","#","#"]
    return s[lineNr]

def printLineX ():
    return "#"*29

def validate (board, move):
    return (0<move and move < 10) and board[move-1]=="-"

def fieldIsAccessible (board, idx):
    return board[idx-1] == "-"

def isNearlyDead (board, idx1, idx2, idx3, player):
    line = board[idx1-1]+board[idx2-1]+board[idx3-1]
    return (line == player+player+"-"
        or line == player+"-"+player
        or line == "-"+player+player)

def defenseMove (board, idx1, idx2, idx3):
    if board[idx1-1] == "-":
        return idx1
    if board[idx2-1] == "-":
        return idx2
    if board[idx3-1] == "-":
        return idx3

def computerAI (board, computer, player):
    # try to choose middle of the board
    if fieldIsAccessible (board, 5):
        return 5

    # check nearly win
    if isNearlyDead(board, 1, 2, 3, computer):
        return defenseMove (board, 1, 2, 3)

    if isNearlyDead(board, 4, 5, 6, computer):
        return defenseMove (board, 4, 5, 6)

    if isNearlyDead(board, 7, 8, 9, computer):
        return defenseMove (board, 7, 8, 9)

    if isNearlyDead(board, 1, 4, 7, computer):
        return defenseMove (board, 1, 4, 7)

    if isNearlyDead(board, 2, 5, 8, computer):
        return defenseMove (board, 2, 5, 8)

    if isNearlyDead(board, 3, 6, 9, computer):
        return defenseMove (board, 3, 6, 9)

    if isNearlyDead(board, 1, 5, 9, computer):
        return defenseMove (board, 1, 5, 9)

    if isNearlyDead(board, 3, 5, 7, computer):
        return defenseMove (board, 3, 5, 7)    

    # check nearly dead
    if isNearlyDead(board, 1, 2, 3, player):
        return defenseMove (board, 1, 2, 3)

    if isNearlyDead(board, 4, 5, 6, player):
        return defenseMove (board, 4, 5, 6)

    if isNearlyDead(board, 7, 8, 9, player):
        return defenseMove (board, 7, 8, 9)

    if isNearlyDead(board, 1, 4, 7, player):
        return defenseMove (board, 1, 4, 7)

    if isNearlyDead(board, 2, 5, 8, player):
        return defenseMove (board, 2, 5, 8)

    if isNearlyDead(board, 3, 6, 9, player):
        return defenseMove (board, 3, 6, 9)

    if isNearlyDead(board, 1, 5, 9, player):
        return defenseMove (board, 1, 5, 9)

    if isNearlyDead(board, 3, 5, 7, player):
        return defenseMove (board, 3, 5, 7)

    # 
    if fieldIsAccessible (board, 1):
        return 1
    if fieldIsAccessible (board, 3):
        return 3
    if fieldIsAccessible (board, 7):
        return 7
    if fieldIsAccessible (board, 9):
        return 9    

    # first free
    idx = 1
    for field in board:
        if field == "-":
            return idx
        idx = idx + 1
    return

def boardIsFull (board):
    for field in board:
        if (field == "-"):
            return False
    return True

def checkIsOver (b):
    return (checkIfWin(b, "X")
    or checkIfWin(b, "O") 
    or boardIsFull(b))

def whoWin (board):
    if checkIfWin (board, "X"):
        return "X"
    if checkIfWin (board, "O"):
        return "O"
    return "-"

def checkIfWin (b, player):
    # 0 1 2
    # 3 4 5 
    # 6 7 8
    return (b[0]==b[1]==b[2]==player
    or b[3]==b[4]==b[5]==player
    or b[6]==b[7]==b[8]==player
    or b[0]==b[3]==b[6]==player
    or b[1]==b[4]==b[7]==player
    or b[2]==b[5]==b[8]==player
    or b[0]==b[4]==b[8]==player
    or b[6]==b[4]==b[2]==player)

def makeMove (board, move, player):
    board[move-1] = player
    return board

def mainLoop ():
    print ("-------------")
    print ("|Tic-Tac-Toe|")
    print ("-------------\n")
    print ("Choose Xs or Os")
    print ("1. Xs")
    print ("2. Os")
    
    mainChoose = input("type option (number): ")
    player = ""
    computer = ""
    computerStartFirst = False

    if "1" == mainChoose:
        player = "X"
        computer = "O"
    elif "2" == mainChoose: 
        player = "O"
        computer = "X"
        computerStartFirst = True
    else: 
        print ("Bad choose.")
        return

    board = ["-","-","-", "-","-","-", "-","-","-"]
    
    visualize (board)
    round = 1
    while (True):
        print ("Round ["+str(round)+"]")
        if computerStartFirst:
            move = computerAI (board, computer, player)
            print("Computer play: "+str(move))
            board = makeMove (board, move, computer)
            visualize (board)
            if checkIsOver(board):
                break
        move = int(input("choose field (number): "))
        if validate(board, move):
            round = round+1
            board = makeMove (board, move, player)
            visualize (board)
            if checkIsOver(board):
                break
            if computerStartFirst == False:
                move = computerAI (board, computer, player)
                print("Computer play: "+str(move))
                board = makeMove (board, move, computer)
                visualize (board)
                if checkIsOver(board):
                    break
        else: 
            print("Bad move\n")

    winner = whoWin (board)    
    if (player==winner):
        print ("You are a WINNER!")
    if (computer==winner):
        print ("Computer is a WINNER :(")
    if ("-"==winner):
        print ("Draft! Try again")

    return;

# main lop of the game
mainLoop();
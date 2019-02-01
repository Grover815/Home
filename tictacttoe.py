from guizero import App, Waffle, PushButton, Text, Window
player1playing = True
#Function to toggle colors depending on player
def change_pixel(x,y):
    if board.get_pixel(x,y) == 'white':
        global player1playing
        #last click used for determining winner
        global lastclick
        if player1playing == True:
            board.set_pixel(x,y, "red")
            player1playing = False
            lastclick = board.get_pixel(x,y)
            checkwin()
        else:
            board.set_pixel(x, y, "blue")
            player1playing = True
            lastclick = board.get_pixel(x,y)
            checkwin()
#Function to check if a winning move has been made
def checkwin():
    #Updates list with current layout of colors on the board
    #Arranges it by rows, columns, an diagnols
    row1 = [board.get_pixel(0,0), board.get_pixel(1,0), board.get_pixel(2,0)]
    row2 = [board.get_pixel(0,1), board.get_pixel(1,1), board.get_pixel(2,1)]
    row3 = [board.get_pixel(0,2), board.get_pixel(1,2), board.get_pixel(2,2)]
    col1 = [board.get_pixel(0,0),board.get_pixel(0,1) ,board.get_pixel(0,2)]
    col2 = [board.get_pixel(1,0),board.get_pixel(1,1) ,board.get_pixel(1,2)]
    col3 = [board.get_pixel(2,0),board.get_pixel(2,1) ,board.get_pixel(2,2)]
    diaglr = [board.get_pixel(0,0), board.get_pixel(1,1), board.get_pixel(2,2)]
    diagrl = [board.get_pixel(2,0), board.get_pixel(1,1), board.get_pixel(0,2) ]
    #Puts the name of the lists in a list, this is for calling
    rows = [row1, row2, row3]
    cols = [col1, col2, col3]
    diags = [diaglr, diagrl]
    #Checks each row for white space,
    #if none detected checks if the row is all the same color
    for x in range(0,3):
        rowcheck = rows[x]
        if "white" in rowcheck:
           pass
        else:
            if len(set(rowcheck)) == 1 == True:               
                winner()
                board.disable()
    #Checks each column for white space,
    #if none detected checks if the row is all the same color
    for x in range(0,3):
        colcheck = cols[x]
        if "white" in colcheck:
            pass
        else:
            if len(set(colcheck)) == 1 == True:               
                winner()
                board.disable()
    #Checks each diagnol for white space,
    #if none detected checks if the row is all the same color
    for x in range(0,2):
        diagcheck = diags[x]
        if "white" in diagcheck:
            pass
        else:
            if len(set(diagcheck)) == 1 == True:
                winner()
                board.disable()
#Function to check who made the winning move
def winner():
    global lastclick
    if lastclick == "red":
        toptext.value = "Red Wins"
        toptext.text_color = "red"
    else:
        toptext.value = "Blue Wins"
        toptext.text_color = "blue"
#Function to reset the board
def reset():
    board.set_all("white")
    board.enable()
    global player1playing
    player1playing = True
    toptext.value = ""
#Creates the window/app
app = App("TicTacToe", height="200", width="200")
#Creates unseen text, updated when a player has won
toptext = Text(app, text="")
#Creates the board
board = Waffle(app, height=3, width=3, dim=50, pad=2, dotty=False, command=change_pixel)
#Creates the reset button
reset = PushButton(app, text="Reset", command=reset)
app.display()

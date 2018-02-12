count = 0
x=int(input("Enter the size of Tic Tac Toe Matrix you want to play:"))
board = [['O'] * x for i in range(x)]
def print_board():
    for i in board:
        print(i)
print_board()
def player1():
    global count, x
    x1 = int(input("Player1 - Enter the X co-ordinate value you want to mark:"))
    y1 = int(input("Player1 - Enter the Y co-ordinate value you want to mark:"))
    if (x1>=0 and x1<x and y1>=0 and y1<x):
        if board[int(x1)][int(y1)] == 'O':
            board[int(x1)][int(y1)] = 'X'
            print_board()
            count += 1
                
        else:
            print("Select a different position, this position is already marked")
            player1()
    else:
        print("Those co-ordinates are not allowed. Please enter again")
        player1()

        
def player2():
    global count, x
    x2 = int(input("Player2 - Enter the X co-ordinate value you want to mark:"))
    y2 = int(input("Player2 - Enter the Y co-ordinate value you want to mark:"))
    if (x2>=0 and x2<=x and y2>=0 and y2<=x):
        if board[int(x2)][int(y2)] == 'O':
            board[int(x2)][int(y2)] = 'Y'
            print_board()
            count += 1
                    
        else:
            print("Select a different position, this position is already marked")
            player2()
    else:
        print("Those co-ordinates are not allowed. Please enter again")
        player2()
            
def logic():
    i=0
    global x
    while(i<x):
        ct1=0
        ct2=0
        ct3=0
        ct4=0
        for j in range(x):
            if(board[i][j]=='X'):
                ct1 += 1
            if(board[j][i]=='X'):
                ct3 += 1
            if(board[i][j]=='Y'):
                ct2 += 1
            if(board[j][i]=='Y'):
                ct4 += 1
        
        
        if ct1==x or ct3==x:
            print("Player1 is the winner!")
            return True
            break
        if ct2==x or ct4==x:
            print("Player2 is the winner!")
            return True
            break
        i += 1
        
        

    i=0
    while(i<x):
        ct5=0
        ct6=0
        for i in range(x):
            if board[i][i]=='X':
                ct5 += 1
            if board[i][i]=='Y':
                ct6 += 1
        if ct5==x:
            print("Player1 is the winner!")
            return True
            break
        if ct6==x:
            print("Player2 is the winner!")
            return True
            break
        i += 1



    i=0
    while(i<x):
        r=x-1
        ct7=0
        ct8=0
        for q in range(x):
            if board[q][r]== 'X':
                ct7 += 1
            if board[q][r]== 'Y':
                ct8 += 1
            r -= 1
        if ct7==x:
            print("Player1 is the winner!")
            return True
            break
        if ct8==x:
            print("Player2 is the winner!")
            return True
            break
        i += 1
            



while(True):
    if(count==x*x):
        print("It's a Draw!")
        break
    if logic()==True:
        break
    if(count==x*x):
        print("It's a Draw!")
        break
    player1()
    if logic()==True:
        break
    if(count==x*x):
        print("It's a Draw!")
        break
    player2()
    if logic()==True:
        break
    


    
    
    
    
    
    

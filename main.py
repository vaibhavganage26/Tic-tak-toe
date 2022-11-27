# def printBoard(xState,yState):
#     zero= "X" if xState[0] else ("O" if yState[0] else 0)
#     one= "X" if xState[1] else ("O" if yState[1] else 1)
#     two= "X" if xState[2] else ("O" if yState[2] else 2)
#     three= "X" if xState[3] else ("O" if yState[3] else 3)
#     four= "X" if xState[4] else ("O" if yState[4] else 4)
#     five= "X" if xState[5] else ("O" if yState[5] else 5)
#     six= "X" if xState[6] else ("O" if yState[6] else 6)
#     seven= "X" if xState[7] else ("O" if yState[7] else 7)
#     eight= "X" if xState[8] else ("O" if yState[8] else 8)
#     print(f" {zero} | {one} | {two} ")
#     print(f"---|---|---")
#     print(f" {three} | {four} | {five} ")
#     print(f"---|---|---")
#     print(f" {six} | {seven} | {eight} ")
# def sum(a,b,c):
#     return a+b+c

# def winner(xState, yState):
#     wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#     for win in wins:
#         if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
#             print("X is Winner")
#             return 1
#         if(sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
#             print("O is Winner")
#             return 0
#     return -1

# if __name__=="__main__":
#     xState=[0,0,0,0,0,0,0,0,0]
#     yState=[0,0,0,0,0,0,0,0,0]
#     turn = 1 
#     print("Welcome to Tic Tac Toe")
#     while (True):
#         printBoard(xState,yState)
#         if turn==1: 
#             print("X's chance")
#             value=int(input("Enter value: "))
#             xState[value]=1
#         else:
#             print("O's chance")
#             value=int(input("Enter value: "))
#             yState[value]=1
#         n = winner(xState, yState)
#         if n!=-1:
#             print("Mtach Over")
#             break
#         turn=1-turn


# to display the board
def printBoard(xstate,ystate):
    zero= "X" if xstate[0] else("O" if ystate[0] else 0)
    one= "X" if xstate[1] else("O" if ystate[1] else 1)
    two= "X" if xstate[2] else("O" if ystate[2] else 2)
    three= "X" if xstate[3] else("O" if ystate[3] else 3)
    four= "X" if xstate[4] else("O" if ystate[4] else 4)
    five= "X" if xstate[5] else("O" if ystate[5] else 5)
    six= "X" if xstate[6] else("O" if ystate[6] else 6)
    seven= "X" if xstate[7] else("O" if ystate[7] else 7)
    eight= "X" if xstate[8] else("O" if ystate[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

# for sum
def sum(a,b,c):
    return a+b+c
# for to check winner
def winner(xstate,ystate):
    win=[[0,4,8],[0,1,2],[1,4,7],[2,5,8],[3,4,5],[6,7,8],[2,4,6],[0,3,6]]
    for wins in win:
        if sum(xstate[wins[0]],xstate[wins[1]],xstate[wins[2]] == 3):
            print("X winner")
            return 1
        if sum(ystate[wins[0]],ystate[wins[1]],ystate[wins[2]] == 3):
            print("O winner")
            return 0
    return -1
# main function
if __name__=="__main__":
    xstate=[0,0,0,0,0,0,0,0,0]
    ystate=[0,0,0,0,0,0,0,0,0]
    print("welcome to TIC TAC TOE")
    turn=1
    while 1:
        printBoard(xstate,ystate)
        if turn==1:
            print("X's chance")
            value=int(input("Enter value where u have to mark:"))
            xstate[value]=1
        else:
            print("O's chance")
            value=int(input("Enter value where u have to mark:"))
            ystate[value]=1
        n=winner(xstate, ystate)
        if n!=1:
            print("Game Over")
            break
        turn -=1
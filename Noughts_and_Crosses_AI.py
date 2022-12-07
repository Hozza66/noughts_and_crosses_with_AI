# Noughts and Crosses game with AI
# Authur: Haoran Hong

from cProfile import label
import random
from tkinter import *

def next_turn(row, column):

    global player
    global move_count
    global last_square
    global player_moves
  
    if squares[row][column]['text'] == '' and check_win() is False:
        if player == players[0]:
            last_square = [row,column]
            squares[row][column].config(text= 'You', fg = 'red')
            player_moves.append(last_square)
        if check_win() is False:
            player = players[1]
            label.config(text= players[1] +  ' turn')
            move_count +=1
            ai()
        elif check_win() is True:
            label.config(text= 'You Win')
            return True
        elif check_win() == 'Tie':
            label.config(text= 'Tie Game')
    


def check_win():
    for row in range(3):
        if squares[row][0]['text'] == squares[row][1]['text'] == squares[row][2]['text'] !='':
            squares[row][0].config(bg='green')
            squares[row][1].config(bg='green')
            squares[row][2].config(bg='green')
            return True

    for column in range(3):
        if squares[0][column]['text'] == squares[1][column]['text'] == squares[2][column]['text'] !='':
            squares[0][column].config(bg='green')
            squares[1][column].config(bg='green')
            squares[2][column].config(bg='green')
            return True

    if squares[0][0]['text'] == squares[1][1]['text']  == squares[2][2]['text']  !='':
        squares[0][0].config(bg='green')
        squares[1][1].config(bg='green')
        squares[2][2].config(bg='green')
        return True

    elif squares[0][2]['text']  == squares[1][1]['text']  == squares[2][0]['text']  !='':
        squares[0][2].config(bg='green')
        squares[1][1].config(bg='green')
        squares[2][0].config(bg='green')
        return True

    elif check_empty() is False:

        for row in range(3):
            for column in range(3):
                squares[row][column].config(bg='yellow')
        return 'Tie'

    else:
        return False

def check_empty():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if squares[row][column]['text'] !='':
                spaces -=1

    if spaces == 0:
        return False
    else:
        True

def new_game():
    global player
    global move_count
    global random_corner
    global ai_moves
    global player_moves
    global last_square
    global ai_first

    player = random.choice(players)
    label.config(text= player +  ' turn', font=('ariel', 50))

    for row in range(3):
        for column in range(3):
            squares[row][column].config(text='', bg='white')

    move_count = 1
    player_moves = []
    ai_moves = []
    random_corner = random.choice(corner_squares)
    last_square = []
    ai_first = False
    if player == players[1]:
        ai_first = True
    print('newgame\n\n\n')
    ai()

def ai():
    global player
    global move_count
    global random_corner
    global player_moves
    global ai_moves
    
    if ai_first:
        if move_count == 1:
            squares[random_corner[0]][random_corner[1]].config(text= 'AI', fg = 'Blue')
            player = players[0]
            label.config(text= players[0] +  ' turn')
            ai_moves.append(random_corner)
            move_count +=1

        if move_count == 3 :
            if squares[centre_square[0]][centre_square[1]]['text'] == 'You':
                square = opposite_corner(random_corner[0], random_corner[1])
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1  
            elif any(x == last_square for x in side_squares):
                square = nearest_unblocked_corner(random_corner[0],random_corner[1],last_square[0],last_square[1])
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1 
            elif last_square == opposite_corner(random_corner[0], random_corner[1]):
                square = nearest_unblocked_corner(random_corner[0],random_corner[1],last_square[0],last_square[1])
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1  
            elif any(x == last_square for x in corner_squares):
                square = opposite_corner(random_corner[0], random_corner[1])
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1  

        if move_count >4:
            square = ai_move()
            squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
            player = players[0]
            label.config(text= players[0] +  ' turn')
            ai_moves.append(square)
            move_count +=1  

    if not ai_first:
        if move_count == 2:
            if last_square in corner_squares:
                square = [1,1]
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1
            elif last_square == centre_square:
                square = random_corner
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1
            else:
                square = centre_square
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1  

        if move_count > 3:
            if (move_count == 4) and (all(item in corner_squares for item in player_moves)):
                square = [1,0]
                squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                player = players[0]
                label.config(text= players[0] +  ' turn')
                ai_moves.append(square)
                move_count +=1  
            else:
                if ai_move() != False:
                    square = ai_move()
                    squares[square[0]][square[1]].config(text= 'AI', fg = 'Blue')
                    player = players[0]
                    label.config(text= players[0] +  ' turn')
                    ai_moves.append(square)
                    move_count +=1  

    
    
    check_win()
    if check_win() == True:
        label.config(text= players[1] +  ' Wins')
    elif check_win() == 'Tie':
        label.config(text= 'Tie Game')

		

def ai_move():
    global player
    global move_count
    global ai_moves
    global player_moves
    global win_squares

    move_count +=1  

    for i in win_squares:
        count = 0
        squares = []
        for j in i:
            if j in player_moves:
                count = 0
                break
            if j in ai_moves:
                squares.append(j)
                count+=1

        if count == 2:
            copy = i.copy()
            copy.remove(squares[0])
            copy.remove(squares[1])
            return copy[0]
    
    for i in win_squares:
        count = 0
        squares = []
        for j in i:
            if j in ai_moves:
                count = 0
                break
            if j in player_moves:
                squares.append(j)
                count+=1

        if count == 2:
            copy = i.copy()
            copy.remove(squares[0])
            copy.remove(squares[1])
            return copy[0]

    arr = []
    for i in ai_moves:
        for j in win_squares:
            if (i in j) and (any(item in player_moves for item in j) is False):
                arr.append(j)
        
    for i in range(len(arr)):
        copy = arr.copy()
        del copy[i]
        for j in arr[i]:
            for k in copy:
                if (j in k) and (j not in ai_moves):
                    return j

    arr2 = []
    for i in player_moves:
        for j in win_squares:
            if (i in j) and (any(item in ai_moves for item in j) is False):
                arr2.append(j)
        
    for i in range(len(arr)):
        copy = arr2.copy()
        del copy[i]
        for j in arr2[i]:
            for k in copy:
                if (j in k) and (j not in player_moves):
                    return j
    
    for corner in corner_squares:
      if (corner not in player_moves) and (corner not in ai_moves):
        return corner

    for i in win_squares:
        squares = []
        count = 0
        for j in i:
            if j in player_moves:
                break
            if j in ai_moves:
                squares.append(i)
                count+=1
        
        if count>0:
          for j in squares:
            if (j[0] not in ai_moves) and (j[0] not in player_moves):
              return j[0]
            elif (j[2] not in ai_moves) and (j[2] not in player_moves):
              return j[2]
            elif (j[1] not in ai_moves) and (j[1] not in player_moves):
              return j[1]

    for i in win_squares:
      for j in i:
        if (i not in ai_moves) and (i not in player_moves):
          return j

    return False


def opposite_corner(a,b):
    c = a - 2
    d = b - 2
    return [abs(c), abs(d)]

def nearest_unblocked_corner(fc_x,fc_y,lc_x,lc_y):
    if fc_x == lc_x:
        if fc_x == 0:
            return [2, fc_y]
        else:
            return [0, fc_y]
    elif fc_y == lc_y:
        if fc_y == 0:
            return [fc_x, 2]
        else:
            return [fc_x, 0]
    else:
        if fc_x == 0:
            return [2, fc_y]
        else:
            return [0, fc_y]


window = Tk()
window.title('Noughts and Crosses (AI)')


players = ['Your', 'AI']
player = random.choice(players)
#player = players[1]
move_count = 1
player_moves = []
ai_moves = []

squares = [[0,0,0],[0,0,0],[0,0,0]]
corner_squares = [[0,0],[0,2],[2,0],[2,2]]
side_squares = [[0,1],[1,0],[1,2],[2,1]]
centre_square = [1,1]
win_squares = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]], 
                [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]], 
                [[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]]]
diagnal_win_squares = [[[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]]]
last_square = []

ai_first = False
if player == players[1]:
    ai_first = True



label = Label(text= player +  ' turn', font=('ariel', 50))
label.pack(side= 'top')

restart_button = Button(text='restart', font=('ariel', 50), command=lambda: new_game())
restart_button.pack(side="bottom")

frame = Frame(window)
frame.pack()





for row in range(3):
    for column in range(3):
        squares[row][column] = Button(frame, text="", font=('ariel', 50), bg='white', width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        squares[row][column].grid(row=row, column=column)

random_corner = random.choice(corner_squares)
ai()

window.mainloop()
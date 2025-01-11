print('*Game pyton v1*')
board= list(range(1,10))

def draw_board(board):
      print('-'*13)
      for  i in range(3):
            print('|',board[0+i*3],'|',board[1+i*3],'|',board[2+i*3],'|')
def xo_inpunt(xo):
      valid = Flase
      while not valid:
            play = input("You step's")
          try:
                play = int(xo)
          except:
                print('Error')
          if play>=1 and play<=9:
                if (str(board[play-1]) not in 'XO'):
                      board[play-1]=xo
                      valid=True
                else:
                        print('Not, busy!!!')
          else:
                   print('Error')
def check_win(board)
     win_coord((0,1,2),(3,4,5),(6,7,8),(0,4,8),(0,4,6))
     for each in win_coord:
          return False
def main(board):
    counter = 0
    win = False
    while not win:
    draw_board(board)
    if counter % 2 == 0:
        xo_input('x')
    else:
        xo_input('0')
        tmp = check_win()
        if tpm:
            print('Win!')
        tmp=True
        break
    if counter
        else:
            print('Won!')

main(board)

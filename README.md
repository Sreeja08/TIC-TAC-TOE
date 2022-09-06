# TIC-TAC-TOE


display_board(board): 
      
       This function takes an empty board as the argument and displays the empty board to
       the user whenever it is called.
     
player_input():
         
        Firstly, this function asks player1 to choose his/her marker as 'X' OR 'O'.
        if user chooses 'X' it return a tuple of markers as ('X','O') and vice versa.
        If player gives input in small letters then this function keeps asking for the correct input
        i.e., capital x or o.
        And assigns the given marker to the marker variable.

place_marker(board,marker,position):
         
         This takes empty board as argument and the marker choosen by the player and
         the position that he/she wants to place that marker.
         This function will assign the marker on the given position of the board.
  
 
win_check(board,mark):
         
         This function checks rows,columns and diagonals of the board as if any has similar markers.And returns
         the boolean value.
 
choose_first():
         
          This function will choose the player randomly. To know the random player,
          we take the help of the random module and use randint method.Method is applied
          on two numbers 0,1 if it gives 0,player2 is choosen else player1 is choosen.
          
          
space_check(board,position):
           
          This checks given position of the board and returns true if the position is empty
          false otherwise.
           
           
full_board_check(board):

           This function checks the entire board and returns true if all the positions are filled 
           false otherwise.
          

player_choice(board):
             
            This function asks the player for his/her next postion.Until the position not in the range of board and
            the given position is not empty,it will keep asking for the next position.And it wil return the position choosen.
             
                         
replay():
             
            This function asks the user whether they want to play again or not.ANd the given input is converted to lower letters and checks whether it
            starts with 'y'. 
             
             
        




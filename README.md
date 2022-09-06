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
             
            This function asks the user whether they want to play again or not.ANd the given input is converted to 
            lowerletters and checks whether it starts with 'y'. 
             
             
 ---------------------------------------------------------------------------------------------------------------------------
 
=> Initially, the board is empty which is said by the 'theBoard' variable.

=> player_input() function returns a tuple as an output which is unpacked with the help of two variables namely, player1_marker    and player2_marker.

=> As we know choose_first() function will return a random player and it is assigned to a variable called as 'turn'.

=> play_game asks for whether the player is ready to play or not.

=> When the input says 'yes' then, 'game_on' will be True.

=> If it is player1's turn then firstly, it will show the empty board.Next, it will call the player_choice function asking
   for the position where the player wants to place his marker and assigns it to the 'position' variable.
  
=> Next, it will call the place_marker function by giving theBoard, player1_marker, position as arguments. It will fill the
   position of the board with player1 marker.
   
=> Then, it will check whether anyone has won the game by calling win_check() function. If any row, column, or any diagonal 
   has player1's marker commonly then it will dispaly the board and print's out a appreciating statement.
   Then, the game_on will become False.
   
=> Else, it checks the entire board with the help of full_board_check() function . If all positions are filled and no one has      won the game then it will printout the message saying "the game is a draw". 

=> Next, at the end it will assign the turn as player 2. If the above things doesn't happen then turn will be changed to 
   another player.
 
=> player2 also goes through the above steps same as player1.

=> At last, the board may be matched with anyone's marker or the board may get filled without anybody's victory.
   In that cases, it will printout the corresponding statement.

=> Lastly, it will ask the user whether they wants to play again, if 'yes' it will repeat the loop else break the loop.







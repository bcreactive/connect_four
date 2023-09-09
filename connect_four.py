class ConnectFour:
    """Class contains the code for the game "Connect Four"."""

    def __init__(self):
        self.current_player = "x"
        self.win = False
        
        self.create_board()

    def run_game(self):
        # Main game loop.
        while not self.win:   
            if self.check_board(): 
                self.set_item(self.current_player)
                self.check_win(self.current_player)
                self.print_board()
                if not self.win:
                    self.switch_player(self.current_player)
                if self.win:
                    self.ask_replay()
                    break
            elif not self.check_board():
                print("There's no more place on the board left!\n")
                self.ask_replay()
                break

    def create_board(self):
        print("\nFour in a row in any direction wins the game.\nPress [q] to exit.")
        self.reset_board()
        self.print_board()

    def reset_board(self):
        # Reset board for a new game.
        self.column_1 = [".", ".", ".", ".", ".", "."]
        self.column_2 = [".", ".", ".", ".", ".", "."]
        self.column_3 = [".", ".", ".", ".", ".", "."]
        self.column_4 = [".", ".", ".", ".", ".", "."]
        self.column_5 = [".", ".", ".", ".", ".", "."]
        self.column_6 = [".", ".", ".", ".", ".", "."]
        self.column_7 = [".", ".", ".", ".", ".", "."]

    def check_board(self):    
        # Test, if the board has any free space left.
        self.columns = [self.column_1, self.column_2, self.column_3,
                        self.column_4, self.column_5, self.column_6,
                        self.column_7]
        
        for column in self.columns:
            for item in column:
                if item == "x" or item == "o":
                    continue
                if item == ".":
                    return True
                
    def set_item(self, player):     
        choice = self.get_user_choice(player)
        if choice == "q":
            print("Good Bye!")
            exit(0)
        self.set_item_place(choice)

    def get_user_choice(self, player):
        pool = ["1", "2", "3", "4", "5", "6", "7", "q"]
        choice = ""
        
        while not choice in pool:
            choice = input(f"\nPlayer {player}, please chose column:\n> ")
            choice = choice.lower()
        if choice in pool:       
            return choice
              
    def check_space(self, column):
        # Checks, if chosen column has some free space left.
        column = int(column) - 1
        for i in self.columns:
            if self.columns[column][5] == ".":
                return True
            else:
                print("No more space left! Please chose another column.")
                self.set_item(self.current_player)
                return False
    
    def set_item_place(self, column):
        # Sets the item in the chosen list at top position.
        counter = 0
        if column == "1": 
            while counter < 6:  
                if self.check_space(column):
                    if self.column_1[counter] == ".":
                        self.column_1[counter] = self.current_player
                        return
                    if self.column_1[counter] != ".":
                        counter += 1
                else:
                    break
        elif column == "2": 
            while counter < 6:  
                if self.check_space(column):
                    if self.column_2[counter] == ".":
                        self.column_2[counter] = self.current_player
                        return
                    if self.column_2[counter] != ".":
                        counter += 1
                else:
                    break
        elif column == "3": 
            while counter < 6:  
                if self.check_space(column):
                    if self.column_3[counter] == ".":
                        self.column_3[counter] = self.current_player
                        return
                    if self.column_3[counter] != ".":
                        counter += 1
                else:
                    break
        elif column == "4": 
            while counter < 6:  
                if self.check_space(column):
                    if self.column_4[counter] == ".":
                        self.column_4[counter] = self.current_player
                        return
                    if self.column_4[counter] != ".":
                        counter += 1
                else:
                    break
        elif column == "5": 
            while counter < 6:  
                if self.check_space(column):
                    if self.column_5[counter] == ".":
                        self.column_5[counter] = self.current_player
                        return
                    if self.column_5[counter] != ".":
                        counter += 1
                else:
                    break
        elif column == "6": 
            while counter < 6:  
                if self.check_space(column):
                    if self.column_6[counter] == ".":
                        self.column_6[counter] = self.current_player
                        return
                    if self.column_6[counter] != ".":
                        counter += 1
                else:
                    break
        elif column == "7": 
            while counter < 6:  
                if self.check_space(column):
                    if self.column_7[counter] == ".":
                        self.column_7[counter] = self.current_player
                        return
                    if self.column_7[counter] != ".":
                        counter += 1
                else:
                    break
  
    def print_board(self):
        # Displays the Board in console.
        board = f"""
        -----------------------
        | 1  2  3  4  5  6  7 |
        |                     |
        | {self.column_1[5]}  {self.column_2[5]}  {self.column_3[5]}  {self.column_4[5]}  {self.column_5[5]}  {self.column_6[5]}  {self.column_7[5]} |
        | {self.column_1[4]}  {self.column_2[4]}  {self.column_3[4]}  {self.column_4[4]}  {self.column_5[4]}  {self.column_6[4]}  {self.column_7[4]} |
        | {self.column_1[3]}  {self.column_2[3]}  {self.column_3[3]}  {self.column_4[3]}  {self.column_5[3]}  {self.column_6[3]}  {self.column_7[3]} |
        | {self.column_1[2]}  {self.column_2[2]}  {self.column_3[2]}  {self.column_4[2]}  {self.column_5[2]}  {self.column_6[2]}  {self.column_7[2]} |
        | {self.column_1[1]}  {self.column_2[1]}  {self.column_3[1]}  {self.column_4[1]}  {self.column_5[1]}  {self.column_6[1]}  {self.column_7[1]} |
        | {self.column_1[0]}  {self.column_2[0]}  {self.column_3[0]}  {self.column_4[0]}  {self.column_5[0]}  {self.column_6[0]}  {self.column_7[0]} |    
        -----------------------"""
        
        print(board)

    def check_win(self, player):
        self.check_horizontal(player)
        self.check_vertical(player)
        self.check_diagonal_r(player)
        self.check_diagonal_l(player)

    def check_horizontal(self, player):
        # Checks the possible horizontal tiles for a winner.
        i = [0, 1, 2, 3, 4, 5]
        for a in i:
            tile_a = [self.column_1[a], self.column_2[a], self.column_3[a],
                    self.column_4[a]]
            tile_b = [self.column_2[a], self.column_3[a], self.column_4[a],
                    self.column_5[a]]
            tile_c = [self.column_3[a], self.column_4[a], self.column_5[a],
                    self.column_6[a]]
            tile_d = [self.column_4[a], self.column_5[a], self.column_6[a], 
                    self.column_7[a]]
            
            if (tile_a[0] == tile_a[1] == tile_a[2] == tile_a[3] == player):  
                self.win = True
                self.ending()
                return
            elif (tile_b[0] == tile_b[1] == tile_b[2] == tile_b[3] == player):  
                self.win = True
                self.ending()
                return
            elif (tile_c[0] == tile_c[1] == tile_c[2] == tile_c[3] == player):  
                self.win = True
                self.ending()
                return
            elif (tile_d[0] == tile_d[1] == tile_d[2] == tile_d[3] == player):  
                self.win = True
                self.ending()
                return
            
    def check_vertical(self, player):
        # Checks the possible vertical tiles for a winner.
        self.columns = [self.column_1, self.column_2, self.column_3,
                        self.column_4, self.column_5, self.column_6,
                        self.column_7]
        
        a = 0
        for i in self.columns:
            tile_a = [self.columns[a][0], self.columns[a][1], 
                    self.columns[a][2], self.columns[a][3]]
            tile_b = [self.columns[a][1], self.columns[a][2], 
                    self.columns[a][3], self.columns[a][4]]
            tile_c = [self.columns[a][2], self.columns[a][3], 
                    self.columns[a][4], self.columns[a][5]]
                
            if (tile_a[0] == tile_a[1] == tile_a[2] == tile_a[3] == player):  
                self.win = True
                self.ending()
                return
            elif (tile_b[0] == tile_b[1] == tile_b[2] == tile_b[3] == player):  
                self.win = True
                self.ending()
                return
            elif (tile_c[0] == tile_c[1] == tile_c[2] == tile_c[3] == player):  
                self.win = True
                self.ending()
                return
            else:
                a += 1          

    def check_diagonal_r(self, player):
        # Checks the possible diagonal-up-right tiles for a winner.
        self.columns = [self.column_1, self.column_2, self.column_3,
                        self.column_4, self.column_5, self.column_6,
                        self.column_7]
        
        x = 0
        y = 0
        while y < 2:
            tile_a = [self.columns[x][y], self.columns[x+1][y+1], 
                    self.columns[x+2][y+2], self.columns[x+3][y+3]]
            
            tile_b = [self.columns[x+1][y], self.columns[x+2][y+1], 
                    self.columns[x+3][y+2], self.columns[x+4][y+3]]
            
            tile_c = [self.columns[x+2][y], self.columns[x+3][y+1], 
                    self.columns[x+4][y+2], self.columns[x+5][y+3]]
            
            tile_d = [self.columns[x+3][y], self.columns[x+4][y+1], 
                    self.columns[x+5][y+2], self.columns[x+6][y+3]]
                
            if (tile_a[0] == tile_a[1] == tile_a[2] == tile_a[3] == player):  
                self.win = True
                self.ending()
                break
            elif (tile_b[0] == tile_b[1] == tile_b[2] == tile_b[3] == player):  
                self.win = True
                self.ending()
                break
            elif (tile_c[0] == tile_c[1] == tile_c[2] == tile_c[3] == player):  
                self.win = True
                self.ending()
                break
            elif (tile_d[0] == tile_d[1] == tile_d[2] == tile_d[3] == player):  
                self.win = True
                self.ending()
                break
            else:
                y += 1          

    def check_diagonal_l(self, player):
        # Checks the possible diagonal-up-left tiles for a winner.
        self.columns = [self.column_1, self.column_2, self.column_3,
                        self.column_4, self.column_5, self.column_6,
                        self.column_7]
        
        x = 6
        y = 0
        while y < 3:
            tile_a = [self.columns[x-3][y], self.columns[x-4][y+1], 
                    self.columns[x-5][y+2], self.columns[x-6][y+3]]
            
            tile_b = [self.columns[x-2][y], self.columns[x-3][y+1], 
                    self.columns[x-4][y+2], self.columns[x-5][y+3]]
            
            tile_c = [self.columns[x-1][y], self.columns[x-2][y+1], 
                    self.columns[x-3][y+2], self.columns[x-4][y+3]]
            
            tile_d = [self.columns[x][y], self.columns[x-1][y+1], 
                    self.columns[x-2][y+2], self.columns[x-3][y+3]]      
                
            if (tile_a[0] == tile_a[1] == tile_a[2] == tile_a[3] == player):  
                self.win = True
                self.ending()
                break
            elif (tile_b[0] == tile_b[1] == tile_b[2] == tile_b[3] == player):  
                self.win = True
                self.ending()
                break
            elif (tile_c[0] == tile_c[1] == tile_c[2] == tile_c[3] == player):  
                self.win = True
                self.ending()
                break
            elif (tile_d[0] == tile_d[1] == tile_d[2] == tile_d[3] == player):  
                self.win = True
                self.ending()
                break
            else:
                y += 1          
    
    def switch_player(self, player):
        if player == "x":
            self.current_player = "o"
        else:
            self.current_player = "x"

    def ending(self):
        print(f"\nCongratulation! Player {self.current_player} wins!!")

    def ask_replay(self):
        pool = ["y", "n"]
        choice = ""
        while choice not in pool:
            choice = input("\nReplay? (y/n):\n> ")
            choice = choice.lower()
        if choice == "n":
            print("\nThanks for testing!\n")
            exit()
        elif choice == "y":
            game = ConnectFour()
            game.run_game()


if __name__ == "__main__":
    game = ConnectFour()
    game.run_game()

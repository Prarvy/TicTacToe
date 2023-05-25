# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: Tic-Tac-Toe Game
# Version: 1.0: Base version by author
import random
import tkinter as tk
import tkinter.messagebox as messagebox


class Game:
    # Initialize the Game parameters
    def __init__(self, _window):
        self.state = None
        self.color = None
        self.window = _window
        self.board = None
        self.first_move = None
        self.font_style = ('Arial Bold', 35)
        self.game_status = None
        self.initiate_game()

    # Start the Game
    def initiate_game(self):
        self.game_status = True
        self.first_move = True
        self.board = [' ' for _ in range(9)]
        self.display_board()
        if self.first_move:
            self.computer_move()

    # Display Tic-Tac-Toe Game Board
    def display_board(self):
        for i in range(9):
            button = tk.Button(self.window, text=self.board[i], font=self.font_style, width=3, height=1, borderwidth=5,
                               bg='red' if self.board[i] == 'X' else 'green' if self.board[i] == 'O' else 'white',
                               state=tk.NORMAL if self.board[i] == ' ' else tk.DISABLED,
                               command=lambda i=i: self.user_move(i))
            button.grid(row=i // 3, column=i % 3)

    # Perform computer move automatically
    def computer_move(self):
        if self.first_move:
            self.board[4] = 'X'
            self.first_move = False
            self.display_board()
        else:
            computer_choice = random.choice([i for i in range(9) if self.board[i] == ' '])
            self.board[computer_choice] = 'X'
            self.display_board()
            if self.rules_checker('X'):
                messagebox.showinfo("Game Over", "Computer won!")
                self.reset_game()

    # Perform user move
    def user_move(self, index):
        self.board[index] = 'O'
        self.display_board()
        if self.rules_checker('O'):
            messagebox.showinfo("Game Over", "You won!")
            self.reset_game()
        else:
            self.computer_move()

    # Verify the rules
    def rules_checker(self, player):
        rules = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]

        for rule in rules:
            if all(self.board[i] == player for i in rule):
                return True

        unfilled_board_data = [i for i in range(9) if self.board[i] == ' ']
        if len(unfilled_board_data) == 0:
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
        return False

    # Start a new game
    def reset_game(self):
        self.initiate_game()


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Tic-Tac-Toe')
    window.config(borderwidth=8)
    window.config(background='#f2f2f2')
    window.iconbitmap(window, default="tictactoe.ico")
    game = Game(window)
    window.mainloop()

from tkinter import *
#TODO change import method, to from tkinter import module


class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=canvas_size, width=canvas_size, bg=bg_color)
        self.canvas.pack()
        self.figure_size = figure_size
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [empty, empty, empty],
            [empty, empty, empty],
            [empty, empty, empty]]
        
    def click_event(self, event):
        """Get coordinates of the click, and proccess player/ai move"""
        #player move
        x_coord = event.x // figure_size
        y_coord = event.y // figure_size
        self.make_move(x_coord, y_coord)
    
    def check_win(self, board, player):
        for y in range(3):
            if board[y] == [player, player, player]:
                return True
        for x in range(3):
            if board[0][x] == board[1][x] == board[2][x] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        elif board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
    
    def check_draw(self, board):
        for row in board:
            if empty in row:
                return False
        return True
    
    def update_board(self, x, y):
        c_player = self.current_player
        self.board[x][y] = c_player
        if self.check_win(self.board, c_player):
            self.winner(c_player)
        elif self.check_draw(self.board):
            self.winner()
    
    def change_player(self):
        if self.current_player == X:
            self.current_player = O
        else:
            self.current_player = X


    def make_move(self, x, y):
        position = {0: 0, 1: 200, 2: 400}
        current_player = self.current_player
        try:
            if self.board[x][y] == empty:
                self.update_board(x, y)
                self.change_player()
                if current_player == X:
                    self.render_cross(position[x], position[y])
                elif current_player == O:
                    self.render_circle(position[x], position[y])
        except IndexError:
            pass


    def build_grid(self, grid_color):
        x = canvas_size // ratio
        y1 = 0
        y2 = 600
        for _ in range(ratio-1):
            self.canvas.create_line(x, y1, x, y2, fill=grid_color)
            self.canvas.create_line(y1, x, y2, x, fill=grid_color)
            x += canvas_size // ratio

    def render_cross(self, posX, posY):
        f_size = self.figure_size
        self.canvas.create_line(posX, posY, posX + f_size, posY + f_size, fill='red', width=5)
        self.canvas.create_line(posX + f_size, posY, posX, posY + f_size, fill='red', width=5)

    def render_circle(self, posX, posY):
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline='blue', width=5)

    def winner(self, player=None):
        """Display end game text, depends on player attribute
        and shutdown the game"""

        center = canvas_size // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text=text, fill='white', font='Arial 50')
        self.canvas.unbind('<Button-1')



# Constants
canvas_size = 600
figure_size = 200
ratio = canvas_size // figure_size
bg_color = 'black'
empty = None

# Players setup
X = 'player 1'
O = 'player 2'
first_player = X

# Initialize game object and execute require methods
game_v1 = Board(start_player=first_player)
game_v1.build_grid('white')

# Testing
#game_v1.render_cross(0, 0)
#game_v1.render_circle(0, 0)
#game_v1.winner()

# Run the game
game_v1.mainloop()

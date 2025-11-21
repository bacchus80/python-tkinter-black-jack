import tkinter as tk

COLORS = {
    'green': '#afdead',
    'black': '#000000',
    'white': '#ffffff'
}

TEXT = {
    'scoreboard': 'Scoreboard',
    'wins': 'Wins',
    'losses': 'Losses',
    'ties': 'Ties',
}

class ScoreBoard:
    """
    Scoreboard for the player to keep track of wins, losses and ties
    The scoreboard is positioned in the upper right corner of the board
    """
    def __init__(self, root):
        self.nr_of_wins = 0
        self.nr_of_losses = 0
        self.nr_of_ties = 0

        self.canvas = tk.Canvas(root, bg=COLORS['green'], bd=1, relief='solid', width=110 ,height=110)
        self.canvas.place(relx=1.0, x=-40, y=20, anchor='ne')

        self.scoreboard_texts = [TEXT['wins'], TEXT['losses'], TEXT['ties']]
        self.header = tk.Label(self.canvas, text=TEXT['scoreboard'], bg=COLORS['black'], fg=COLORS['white'], justify='center')
        self.canvas.create_window(60, 14, window=self.header)

        # Draw a black rectangle to fill background for header
        self.canvas.create_rectangle(8, 10, 110, 20, outline=COLORS['black'], width=12)

        self.canvas_frame = tk.Frame(root, bg=COLORS['green'])
        self.canvas_frame.pack(pady=20)
        self.canvas.create_window(60, 70, window=self.canvas_frame)

        for counter, text in enumerate(self.scoreboard_texts):
            self.scoreboard_text_label = tk.Label(self.canvas_frame, text=text, bg=COLORS['green'], justify='left')
            self.scoreboard_text_label.grid(row=counter, column=0, padx=0, pady=0, sticky='w' )

        label_value_options = {
            'justify': 'right',
            'font': ('Courier', 16),
            'bg': COLORS['green']
        }

        # loop out the score board values
        self.label_values = []
        label_value_texts = [self.nr_of_wins, self.nr_of_losses, self.nr_of_ties]
        for i, value in enumerate(label_value_texts):
            label = tk.Label(self.canvas_frame, text=self.pad_number(value), **label_value_options)
            label.grid(row=i, column=1, padx=4, pady=0)
            self.label_values.append(label)

    def pad_number(self, value):
        return f"{value:>4}"

    def update_result_text(self):
        """
        Update GUI with new values
        """
        scoreboard_values = [self.nr_of_wins, self.nr_of_losses, self.nr_of_ties]

        for i, value in enumerate(scoreboard_values):
            self.label_values[i].config(text=self.pad_number(value))
    
    def update_score_tie(self):
        self.nr_of_ties += 1
        self.update_result_text()

    def update_score_player_wins(self):
        self.nr_of_wins += 1
        self.update_result_text()

    def update_score_player_loses(self):
        self.nr_of_losses += 1
        self.update_result_text()
    
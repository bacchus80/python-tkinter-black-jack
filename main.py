import tkinter as tk
from blackjack import BlackjackBoard

def main():
    root = tk.Tk()
    root = root
    root.title("Black Jack")
    root.geometry("800x600")

    game = BlackjackBoard(root)
    game.start_game()

    root.mainloop()

if __name__ == '__main__':
    main()
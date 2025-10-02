import tkinter as tk
from blackjack import BlackjackBoard

def main():
    root = tk.Tk()
    root = root
    root.title("Black Jack")
    root.geometry("600x400")

    app = BlackjackBoard(root)
    app.start_game()

    root.mainloop()

if __name__ == '__main__':
    main()
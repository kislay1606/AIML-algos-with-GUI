import tkinter as tk
from tkinter import messagebox
import random

board = [" " for _ in range(9)]

def check_win(brd, player):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(all(brd[i]==player for i in combo) for combo in wins)

def empty_cells(brd):
    return [i for i, val in enumerate(brd) if val == " "]

def minimax(brd, is_max):
    if check_win(brd, "O"): return 1
    if check_win(brd, "X"): return -1
    if not empty_cells(brd): return 0

    if is_max:
        best = -float('inf')
        for i in empty_cells(brd):
            brd[i] = "O"
            best = max(best, minimax(brd, False))
            brd[i] = " "
        return best
    else:
        best = float('inf')
        for i in empty_cells(brd):
            brd[i] = "X"
            best = min(best, minimax(brd, True))
            brd[i] = " "
        return best

def best_move():
    best_val = -float('inf')
    move = -1
    for i in empty_cells(board):
        board[i] = "O"
        move_val = minimax(board, False)
        board[i] = " "
        if move_val > best_val:
            best_val = move_val
            move = i
    return move

def button_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X")
        if check_win(board, "X"):
            messagebox.showinfo("Game Over", "You Win!")
            window.destroy()
            return
        if not empty_cells(board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            window.destroy()
            return
        ai_move = best_move()
        board[ai_move] = "O"
        buttons[ai_move].config(text="O")
        if check_win(board, "O"):
            messagebox.showinfo("Game Over", "AI Wins!")
            window.destroy()

def start_tic_tac_toe():
    global window, buttons, board
    window = tk.Toplevel()
    window.title("Tic Tac Toe")
    board = [" " for _ in range(9)]
    buttons = []

    for i in range(9):
        btn = tk.Button(window, text=" ", font='Helvetica 20', height=2, width=4, command=lambda i=i: button_click(i))
        btn.grid(row=i//3, column=i%3)
        buttons.append(btn)

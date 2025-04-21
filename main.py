import tkinter as tk
from tkinter import PhotoImage
from bfs_dfs import bfs_main, dfs_main
from tic_tac_toe import start_tic_tac_toe
from water_jug import solve_water_jug


root = tk.Tk()
root.title("AI ML Project")
root.geometry("400x400")
root.configure(bg="#f0f4f7")


title = tk.Label(root, text="AI/ML Project", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#2c3e50")
title.pack(pady=20)



button_config = {
    "font": ("Arial", 14),
    "width": 25,
    "height": 2,
    "bg": "#3498db",
    "fg": "white",
    "activebackground": "#2980b9",
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0
}

tk.Button(root, text="🔎 Breadth First Search (BFS)", command=bfs_main, **button_config).pack(pady=10)
tk.Button(root, text="🌲 Depth First Search (DFS)", command=dfs_main, **button_config).pack(pady=10)
tk.Button(root, text="❌⭕ Tic Tac Toe", command=start_tic_tac_toe, **button_config).pack(pady=10)
tk.Button(root, text="💧 Water Jug Problem", command=solve_water_jug, **button_config).pack(pady=10)


footer = tk.Label(root, text="Designed with ❤️ by Kislay", font=("Arial", 10), bg="#f0f4f7", fg="#7f8c8d")
footer.pack(side="bottom", pady=10)

root.mainloop()

import tkinter as tk
from tkinter import simpledialog, messagebox

def parse_graph_input(input_str):
    graph = {}
    lines = input_str.strip().split("\n")
    for line in lines:
        parts = line.strip().split(":")
        if len(parts) != 2:
            continue
        node = parts[0].strip()
        neighbors = parts[1].strip().split(",")
        graph[node] = [n.strip() for n in neighbors if n.strip()]
    return graph

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph.get(node, []) if n not in visited])
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs_main():
    root = tk.Tk()
    root.withdraw()
    graph_str = simpledialog.askstring("BFS Graph Input", "Enter graph (e.g. A:B,C\nB:D\nC:E):")
    start_node = simpledialog.askstring("Start Node", "Enter start node:")
    if graph_str and start_node:
        graph = parse_graph_input(graph_str)
        result = bfs(graph, start_node)
        messagebox.showinfo("BFS Result", f"BFS Order: {' -> '.join(result)}")

def dfs_main():
    root = tk.Tk()
    root.withdraw()
    graph_str = simpledialog.askstring("DFS Graph Input", "Enter graph (e.g. A:B,C\nB:D\nC:E):")
    start_node = simpledialog.askstring("Start Node", "Enter start node:")
    if graph_str and start_node:
        graph = parse_graph_input(graph_str)
        result = dfs(graph, start_node)
        messagebox.showinfo("DFS Result", f"DFS Order: {' -> '.join(result)}")

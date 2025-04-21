from tkinter import simpledialog, messagebox, Tk

def solve_jug(jug1, jug2, goal):
    visited = set()
    steps = []
    def pour(from_jug, to_jug, from_cap, to_cap):
        amt = min(from_jug, to_cap - to_jug)
        return from_jug - amt, to_jug + amt

    queue = [(0, 0)]
    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        steps.append(f"{x}L - {y}L")
        if x == goal or y == goal:
            return steps
        next_states = [
            (jug1, y), (x, jug2), (0, y), (x, 0),
            pour(x, y, jug1, jug2),
            pour(y, x, jug2, jug1)[::-1]
        ]
        queue.extend(s for s in next_states if s not in visited)
    return None

def solve_water_jug():
    root = Tk()
    root.withdraw()
    jug1 = int(simpledialog.askstring("Jug 1 Capacity", "Enter capacity of Jug 1 (in L):"))
    jug2 = int(simpledialog.askstring("Jug 2 Capacity", "Enter capacity of Jug 2 (in L):"))
    goal = int(simpledialog.askstring("Goal", "Enter desired amount (in L):"))

    steps = solve_jug(jug1, jug2, goal)
    if steps:
        messagebox.showinfo("Solution", "\n".join(steps))
    else:
        messagebox.showerror("No Solution", "Could not solve with given jug sizes and goal.")

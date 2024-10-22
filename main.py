import tkinter as tk
from tkinter import messagebox
import time

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.empty_cells = self.find_empty_cells()

    def find_empty_cells(self):
        return [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] == 0]

    def is_valid(self, num, row, col):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def solve(self):
        if not self.empty_cells:
            return True

        row, col = self.empty_cells[0]
        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.grid[row][col] = num
                self.empty_cells.pop(0)
                if self.solve():
                    return True
                self.grid[row][col] = 0
                self.empty_cells.insert(0, (row, col))
        return False

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = [[0] * 9 for _ in range(9)]
        self.cells = [[None] * 9 for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 24), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                self.cells[i][j] = entry

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        self.solve_button.grid(row=10, column=0, columnspan=9)

        self.time_label = tk.Label(self.root, text="", font=('Arial', 14))
        self.time_label.grid(row=11, column=0, columnspan=9)

    def solve(self):
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                self.grid[i][j] = int(val) if val.isdigit() and 1 <= int(val) <= 9 else 0

        solver = SudokuSolver(self.grid)
        
        start_time = time.time()  # Iniciar el temporizador
        if solver.solve():
            end_time = time.time()  # Detener el temporizador
            self.update_grid(solver.grid)
            elapsed_time = end_time - start_time
            self.time_label.config(text=f"Time para resolver: {elapsed_time:.4f} seconds")
        else:
            messagebox.showinfo("Result", "No solution exists")
            self.time_label.config(text="")

    def update_grid(self, solved_grid):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(solved_grid[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()

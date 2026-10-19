"""Tkinter interface for the Maze Solver AI project."""

import tkinter as tk
from tkinter import ttk, messagebox

from .algorithms import breadth_first_search, depth_first_search, Coordinate, SearchResult
from .expert_system import diagnose


class MazeSolverApp:
    ROWS = 20
    COLS = 20
    CELL = 25

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Maze Solver AI | Search Algorithm & Expert System")
        self.root.minsize(780, 640)
        self.start: Coordinate = (0, 0)
        self.goal: Coordinate = (self.ROWS - 1, self.COLS - 1)
        self.walls: set[Coordinate] = self._sample_walls()
        self.explored: set[Coordinate] = set()
        self.path: set[Coordinate] = set()
        self.algorithm = tk.StringVar(value="BFS")
        self.edit_mode = tk.StringVar(value="Wall")
        self.status = tk.StringVar(value="Siap. Pilih algoritma lalu tekan Search.")
        self.metrics = tk.StringVar(value="Langkah: -   |   Simpul diperiksa: -   |   Waktu: -")
        self.diagnosis = tk.StringVar(value="Diagnosis akan muncul setelah pencarian dijalankan.")
        self._build_ui()
        self._draw_maze()

    def _sample_walls(self) -> set[Coordinate]:
        walls: set[Coordinate] = set()
        # Three vertical barriers with openings make a solvable demonstration maze.
        for col, opening in ((4, 3), (8, 7), (12, 12), (16, 16)):
            for row in range(1, self.ROWS - 1):
                if row not in (opening, min(self.ROWS - 2, opening + 1)):
                    walls.add((row, col))
        # A few short horizontal barriers add branches without blocking the route.
        for row, opening in ((5, 6), (10, 10), (15, 14)):
            for col in range(2, self.COLS - 2):
                if col not in (opening, min(self.COLS - 3, opening + 1)):
                    walls.add((row, col))
        walls.discard(self.start)
        walls.discard(self.goal)
        return walls

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=12)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="MAZE SOLVER AI", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(
            outer,
            text="Search Algorithm and Rule-Based Expert System | Python + Tkinter",
            foreground="#526071",
        ).pack(anchor="w", pady=(0, 10))

        toolbar = ttk.Frame(outer)
        toolbar.pack(fill="x", pady=(0, 8))
        ttk.Label(toolbar, text="Algoritma:").pack(side="left")
        ttk.Combobox(toolbar, textvariable=self.algorithm, values=("BFS", "DFS"), state="readonly", width=7).pack(side="left", padx=(6, 12))
        ttk.Button(toolbar, text="Search", command=self.run_search).pack(side="left", padx=3)
        ttk.Button(toolbar, text="Reset Maze", command=self.reset_maze).pack(side="left", padx=3)
        ttk.Button(toolbar, text="Clear Walls", command=self.clear_walls).pack(side="left", padx=3)
        ttk.Label(toolbar, text="Klik kotak untuk menambah/menghapus dinding.", foreground="#526071").pack(side="left", padx=(12, 0))

        body = ttk.Frame(outer)
        body.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(body, width=self.COLS * self.CELL, height=self.ROWS * self.CELL, bg="white", highlightthickness=1, highlightbackground="#CBD5E1")
        self.canvas.pack(side="left", anchor="n")
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        panel = ttk.Frame(body, padding=(14, 0, 0, 0), width=220)
        panel.pack(side="left", fill="both", expand=True)
        ttk.Label(panel, text="PETUNJUK", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        for color, label in (("#16A34A", "Titik awal"), ("#DC2626", "Titik tujuan"), ("#CBD5E1", "Dinding"), ("#FDE68A", "Simpul diperiksa"), ("#60A5FA", "Jalur solusi")):
            row = ttk.Frame(panel)
            row.pack(anchor="w", pady=2)
            swatch = tk.Canvas(row, width=18, height=18, highlightthickness=0)
            swatch.pack(side="left", padx=(0, 7))
            swatch.create_rectangle(1, 1, 17, 17, fill=color, outline=color)
            ttk.Label(row, text=label).pack(side="left")

        ttk.Separator(panel).pack(fill="x", pady=10)
        ttk.Label(panel, text="HASIL PENCARIAN", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        ttk.Label(panel, textvariable=self.status, wraplength=220).pack(anchor="w", pady=(5, 8))
        ttk.Label(panel, textvariable=self.metrics, wraplength=220).pack(anchor="w", pady=(0, 8))
        ttk.Separator(panel).pack(fill="x", pady=5)
        ttk.Label(panel, text="EXPERT SYSTEM", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        ttk.Label(panel, textvariable=self.diagnosis, wraplength=220, justify="left").pack(anchor="w", pady=(5, 0))

        ttk.Label(
            outer,
            text="Catatan: aplikasi ini mensimulasikan pencarian jalur pada grid. Ini bukan alat navigasi fisik.",
            foreground="#526071",
        ).pack(anchor="w", pady=(8, 0))

    def _draw_maze(self) -> None:
        self.canvas.delete("all")
        for row in range(self.ROWS):
            for col in range(self.COLS):
                cell = (row, col)
                x1, y1 = col * self.CELL, row * self.CELL
                x2, y2 = x1 + self.CELL, y1 + self.CELL
                fill = "#FFFFFF"
                if cell in self.walls:
                    fill = "#CBD5E1"
                elif cell in self.explored:
                    fill = "#FEF3C7"
                if cell in self.path:
                    fill = "#60A5FA"
                if cell == self.start:
                    fill = "#16A34A"
                if cell == self.goal:
                    fill = "#DC2626"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="#E2E8F0", width=1)
                if cell == self.start:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="S", fill="white", font=("Segoe UI", 9, "bold"))
                elif cell == self.goal:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="G", fill="white", font=("Segoe UI", 9, "bold"))

    def on_canvas_click(self, event: tk.Event) -> None:
        col, row = event.x // self.CELL, event.y // self.CELL
        cell = (row, col)
        if not (0 <= row < self.ROWS and 0 <= col < self.COLS):
            return
        if cell in (self.start, self.goal):
            return
        if cell in self.walls:
            self.walls.remove(cell)
        else:
            self.walls.add(cell)
        self._clear_results()
        self._draw_maze()
        self.status.set("Peta diperbarui. Jalankan Search untuk memeriksa jalur.")
        self.diagnosis.set("Diagnosis akan muncul setelah pencarian dijalankan.")

    def _clear_results(self) -> None:
        self.explored.clear()
        self.path.clear()
        self.metrics.set("Langkah: -   |   Simpul diperiksa: -   |   Waktu: -")

    def run_search(self) -> None:
        self._clear_results()
        search = breadth_first_search if self.algorithm.get() == "BFS" else depth_first_search
        result: SearchResult = search(self.ROWS, self.COLS, self.walls, self.start, self.goal)
        self.explored = set(result.explored)
        self.path = set(result.path)
        self._draw_maze()
        if result.found:
            self.status.set(f"Jalur ditemukan menggunakan {self.algorithm.get()}.")
            self.metrics.set(f"Langkah: {result.steps}   |   Simpul diperiksa: {result.visited_count}   |   Waktu: {result.elapsed_ms:.3f} ms")
        else:
            self.status.set("Jalur tidak ditemukan.")
            self.metrics.set(f"Simpul diperiksa: {result.visited_count}   |   Waktu: {result.elapsed_ms:.3f} ms")
        self.diagnosis.set(diagnose(result, self.algorithm.get(), self.start, self.goal))

    def reset_maze(self) -> None:
        self.walls = self._sample_walls()
        self._clear_results()
        self.status.set("Labirin contoh dipulihkan.")
        self.diagnosis.set("Diagnosis akan muncul setelah pencarian dijalankan.")
        self._draw_maze()

    def clear_walls(self) -> None:
        self.walls.clear()
        self._clear_results()
        self.status.set("Semua dinding dihapus.")
        self.diagnosis.set("Peta terbuka. Jalankan Search untuk melihat hasil.")
        self._draw_maze()


def launch() -> None:
    root = tk.Tk()
    MazeSolverApp(root)
    root.mainloop()

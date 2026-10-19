"""Run Maze Solver AI. Execute: python main.py"""

from pathlib import Path
import sys

# Allow running directly from the repository without installing the package.
sys.path.insert(0, str(Path(__file__).parent / "src"))

from maze_solver.gui import launch  # noqa: E402


if __name__ == "__main__":
    launch()

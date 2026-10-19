# Maze Solver AI

**AI Course Project: Search Algorithm and Rule-Based Expert System**

Maze Solver AI is a beginner-friendly desktop application that searches for a route through a grid maze. It demonstrates two classic AI search algorithms, Breadth-First Search (BFS) and Depth-First Search (DFS), and a small rule-based expert system that explains the search result.

> This is an educational simulation. It does not use machine learning and is not a physical navigation system.

## Features

- Interactive 20 × 20 maze grid.
- Click any non-start/non-goal cell to add or remove a wall.
- BFS search. Because each move has equal cost, BFS finds a path with the minimum number of moves when a path exists.
- DFS search. DFS can find a path, but does not guarantee the shortest path.
- Visual display of explored cells and the final path.
- Result metrics: path steps, number of explored cells, and search execution time.
- Rule-based expert-system messages using explicit IF-THEN reasoning.
- Unit tests for search and diagnosis behavior.

## Requirements

- Python 3.10 or newer is recommended.
- Tkinter must be available in your Python installation.
- No third-party Python packages are required.

On some Linux distributions, Tkinter may need to be installed separately (for example, the `python3-tk` package).

## Run the application

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

4. Select BFS or DFS and click **Search**.
5. Click cells to add/remove walls, then search again.
6. Use **Reset Maze** to restore the sample maze or **Clear Walls** to create an open grid.

On some systems, use `python3 main.py` instead of `python main.py`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## How it works

1. The maze is represented as a grid graph. Each open cell is a node, and edges connect horizontally or vertically adjacent open cells.
2. BFS or DFS explores reachable nodes from the start cell.
3. A parent map reconstructs the route if the goal is reached.
4. The expert system applies predefined rules to explain the result. For example, a successful BFS search in an unweighted grid means the route has the minimum number of moves. A failed search prompts the user to inspect walls that may disconnect the goal.

## Project structure

```text
maze-solver-ai/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── maze_solver/
│       ├── __init__.py
│       ├── algorithms.py
│       ├── expert_system.py
│       └── gui.py
├── tests/
│   └── test_algorithms.py
└── docs/
    ├── system_design.md
    └── team_workflow.md
```

## Team members and responsibilities

| Member | Assigned branch | Main responsibilities |
|---|---|---|
| **Fatih (team leader)** | `main` | Repository setup, integration, final testing, README, coordination, and reviewing Pull Requests. |
| **Ilham** | `dev-1` | Grid graph model, BFS/DFS search implementation, and algorithm unit tests. |
| **Ervan** | `dev-2` | Tkinter GUI, path visualization, and rule-based expert-system messages. |

Each member should work on their assigned branch and commit their own contributions. Fatih manages the stable `main` branch and reviews changes from Ilham and Ervan before merging. If the lecturer requires a separate branch named `manager`, confirm the required workflow before changing this setup.

## GitHub branch workflow

The assignment notes identify the leader's branch as `manager/main`, with separate development branches for the other members. This project maps that requirement to `main` managed by **Fatih**, `dev-1` for **Ilham**, and `dev-2` for **Ervan**. If the lecturer explicitly requires a separate branch named `manager`, confirm the exact merge process before creating it.

Example commands:

```bash
git switch -c dev-1
# Make changes, then:
git add .
git commit -m "Implement BFS and DFS search"
git push -u origin dev-1
```

Open a Pull Request from the development branch to the designated integration branch. Review and test the changes before merging. Do not commit directly to the shared integration branch for individual feature work.

## Publish to GitHub

Create an **empty** GitHub repository named `AI-TE-103` (do not initialize it with a README if you plan to push this folder as-is). Extract this project folder, open a terminal inside it, and run the following commands. Replace `YOUR-USERNAME` with your GitHub username.

```bash
git init -b main
git add .
git commit -m "Initial Maze Solver AI project"
git remote add origin https://github.com/YOUR-USERNAME/AI-TE-103.git
git push -u origin main

# Create Ilham's branch from the stable main branch
git switch -c dev-1
git push -u origin dev-1

# Create Ervan's branch from the stable main branch
git switch main
git switch -c dev-2
git push -u origin dev-2
```

Each contributor should then clone the repository, switch to their assigned branch, commit their own changes, push the branch, and open a Pull Request. GitHub authentication may prompt you to sign in.

## Limitations

- The system operates only on the grid entered in the application.
- It does not use machine learning or learn from training data.
- It does not model weighted terrain; each valid move has equal cost.
- Search time is measured for a small educational grid and is not a benchmark for large navigation systems.
- A route in the grid is a logical path, not a guarantee of real-world safety.

## Future improvements

- Add A* search and compare it with BFS and DFS.
- Add maze generation and save/load support.
- Export a search report to a text or CSV file.
- Add more expert-system rules for explaining dead ends and alternative routes.

## Academic note

Use this repository as a project starter. Team members should understand the algorithms, test the program, and be able to explain their own contributions during the presentation. Follow your lecturer's policy for attribution and AI-assisted coding.

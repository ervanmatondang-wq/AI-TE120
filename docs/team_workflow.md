# Team Workflow for GitHub

## Team members and assigned branches

- **Fatih (team leader): `main`**
  - Creates and manages the repository.
  - Coordinates the team and reviews Pull Requests.
  - Integrates approved work, runs final tests, and maintains the README.
- **Ilham: `dev-1`**
  - Implements or improves the grid graph model and BFS/DFS algorithms.
  - Adds and runs algorithm unit tests.
- **Ervan: `dev-2`**
  - Develops the Tkinter interface and path visualization.
  - Implements or improves rule-based expert-system messages.
  - Tests the user workflow.

## Branch workflow

1. Fatih creates the GitHub repository and adds Ilham and Ervan as collaborators.
2. All members clone the same repository.
3. Ilham switches to `dev-1`; Ervan switches to `dev-2`. Fatih manages the stable `main` branch.
4. Each member makes focused changes and commits their own work on the assigned branch.
5. Ilham and Ervan push their branches and open Pull Requests targeting `main`.
6. Fatih reviews the changes, checks that the application runs, and runs the test suite before merging.
7. The team verifies the README instructions from a fresh clone.

## Example commands for contributors

Ilham:
```bash
git switch dev-1
git add .
git commit -m "Implement or test search algorithms"
git push -u origin dev-1
```

Ervan:
```bash
git switch dev-2
git add .
git commit -m "Improve GUI and expert-system feedback"
git push -u origin dev-2
```

## Important

The handwritten assignment notes appear to describe the team leader's branch as `manager/main`. This project uses `main` as the leader-managed stable branch, with `dev-1` and `dev-2` for Ilham and Ervan. If the lecturer requires a separate `manager` branch, ask whether it should be merged into `main` or used as the integration branch. Do not claim commits or contributions that a member did not make.

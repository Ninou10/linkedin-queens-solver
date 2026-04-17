# LinkedIn Queens Puzzle Solver 👑

An AI-powered solver for the popular **Queens** logic puzzle (often seen on LinkedIn) and similar games like Star Battle. This project includes both a core Python implementation and a standalone, interactive Web UI.

## The Rules of the Game
You are given an 8x8 grid divided into 8 distinct colored zones. You must place exactly 8 Queens on the board such that:
1. Exactly **one Queen** is in each **row**.
2. Exactly **one Queen** is in each **column**.
3. Exactly **one Queen** is in each **colored zone**.
4. Queens **cannot touch each other**, not even diagonally.

## How It Works (The AI Algorithm)
This solver uses an AI technique known as **Stochastic Hill Climbing with Random Restarts**. 
Instead of brute-forcing all possible combinations (which is slow), the AI:
1. Drops 8 queens onto the board randomly (one in each column).
2. Scores the board based on how many rules are currently broken (conflicts).
3. Looks at every possible single move for every queen and makes the move that reduces the most conflicts.
4. If it gets stuck in a "local minimum" where no single move improves the board, it completely clears the board and restarts. 
5. Because the search space is highly optimized, it usually finds the 0-conflict solution in a fraction of a second.

## Features & Usage

### 1. Interactive Web Version (`index.html`)
A fully standalone front-end version of the tool. 
* **To use:** Simply double-click `index.html` to open it in any web browser. 
* **How to play:** Select a color from the top palette, click and drag on the 8x8 grid to draw your 8 zones to match your puzzle, and click **Generate Solution**.

### 2. Python Core Solver (`solver.py`)
The original algorithm implemented in Python.
* **To use:** Run the script via your terminal:
  ```bash
  python solver.py
  ```
* **To customize:** Open `solver.py` and modify the `example_area_map` 2D array variable at the bottom of the file to match the zones of the puzzle you want to solve. Each zone is represented by an integer from 0 to 7.

## Tech Stack
* **Python 3** (Core algorithmic logic)
* **HTML/CSS/Vanilla JavaScript** (Interactive web interface)

# Sudoku Solver with Arc Consistency

This repository hosts an efficient Sudoku solver utilizing the Arc Consistency algorithm. The solver efficiently solves Sudoku puzzles by enforcing constraints among cells based on Sudoku rules (rows, columns, and sub-grids).

## Table of Contents

1. [Introduction](#1-introduction)
2. [Methodology](#2-methodology)
   - [Functions and Algorithms](#functions-and-algorithms)
   - [Arc Consistency and Sudoku Solver](#arc-consistency-and-sudoku-solver)
3. [Sample Runs and Arc Consistency Trees](#3-sample-runs-and-arc-consistency-trees)
4. [Comparison of Different Initial Boards](#4-comparison-of-different-initial-boards)
   - [Difficulty Levels](#difficulty-levels)
   - [Arc Consistency Functions](#arc-consistency-functions)
5. [Conclusion](#5-conclusion)

---

## 1. Introduction

Sudoku is a logic-based number-placement puzzle aiming to fill a 9x9 grid with digits 1 to 9, ensuring each row, column, and sub-grid contains all digits without repetition. This README explores an Arc Consistency-based solver for efficiently solving Sudoku puzzles.

## 2. Methodology

### Functions and Algorithms

- **remove_inconsistent_values**: Eliminates inconsistent values between cells.
- **enforce_arc_consistency**: Enforces consistency by iterating through the Arc Consistency algorithm.
- **apply_arc_consistency**: Applies Arc Consistency until the board is solved or no further improvements can be made.
- **is_board_solved**: Verifies if the Sudoku board is solved.
- **solve**: Implements backtracking for solving Sudoku puzzles while applying Arc Consistency.

### Arc Consistency and Sudoku Solver

The implementation utilizes Arc Consistency to reduce the search space and solve Sudoku puzzles efficiently.

## 3. Sample Runs and Arc Consistency Trees

- Showcase sample runs of the solver solving Sudoku puzzles.
- Include visual representations of Arc Consistency Trees.
- Display solving times for various difficulty levels.

## 4. Comparison of Different Initial Boards

### Difficulty Levels

- **Easy**: Description of an easy Sudoku puzzle and its solving time.
- **Intermediate**: Description of an intermediate Sudoku puzzle and its solving time.
- **Hard**: Description of a hard Sudoku puzzle and its solving time.
- Discuss the impact of puzzle complexity on solving times and Arc consistency trees.

### Arc Consistency Functions

- Explain the functionality and importance of `generate_all_arcs()`, `remove_inconsistent_values()`, `enforce_arc_consistency()`, and `apply_arc_consistency()` in the Sudoku solving context.

## 5. Conclusion

- Summarize the efficiency of Arc Consistency in solving Sudoku puzzles.
- Reflect on observations from different initial boards, solving times, and complexity of Arc consistency trees.

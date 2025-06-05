# Chess Piece Placement Solver

This project implements a solver for various chess piece placement problems using backtracking algorithms. It can solve problems involving Queens, Bishops, and Knights on an M×N chessboard.

## Project Structure

```
8-queen-prob/
├── chess.py (Core Game Logic)
│   ├── Board Class
│   │   ├── Board Representation
│   │   │   ├── Visual Board (piece positions)
│   │   │   └── Attack Board (attack tracking)
│   │   ├── Piece Movement
│   │   │   ├── Queen Directions
│   │   │   ├── Bishop Directions
│   │   │   └── Knight Directions
│   │   └── Board Operations
│   │       ├── Place Piece
│   │       ├── Remove Piece
│   │       ├── Mark Attacks
│   │       └── Unmark Attacks
│   └── Validation Functions
│
├── solve.py (Solving Algorithm)
│   ├── Solution Class
│   │   ├── Board State
│   │   ├── Score
│   │   └── Diversity Score
│   ├── Result Class
│   │   ├── Piece Positions
│   │   └── Total Score
│   └── Solve Function
│       ├── Backtracking Logic
│       ├── Early Termination
│       └── Piece Placement Strategy
│
├── Task Modules
│   ├── task1.py (Max Queens)
│   ├── task2.py (Max Bishops)
│   ├── task3.py (Max Knights)
│   ├── task4.py (Knights + Bishops)
│   └── task5.py (Knights + Bishops + Fixed Queens)
│
└── team5.py (Main Interface)
    ├── Command Line Interface
    ├── Task Selection
    └── Result Display
```

## Features

- Solves multiple chess piece placement problems:
  1. Maximum Queens placement
  2. Maximum Bishops placement
  3. Maximum Knights placement
  4. Combined Knights and Bishops placement
  5. Knights and Bishops placement with fixed Queen positions
- Efficient backtracking algorithm with early termination
- Dual-board system for tracking piece positions and attacks
- Comprehensive validation of piece placements
- Performance optimization and time tracking
- Flexible command-line interface

## Implementation Details

### Core Components

1. **Board Class (`chess.py`)**
   - Manages game state
   - Tracks piece positions
   - Validates moves
   - Implements piece movement patterns

2. **Solving Algorithm (`solve.py`)**
   - Backtracking implementation
   - Early termination optimization
   - Solution scoring and diversity tracking
   - Result formatting

3. **Task Modules**
   - Specialized solvers for different problems
   - Reuses core components
   - Implements specific constraints

### Key Techniques

1. **Backtracking Algorithm**
   - Systematic piece placement
   - Efficient state management
   - Early termination for optimization

2. **State Management**
   - Dual-board system
   - Attack tracking
   - Position validation

3. **Performance Optimization**
   - Early termination checks
   - Efficient data structures
   - Attack tracking to avoid redundant calculations

## Usage

```bash
python team5.py <task_id> <m> <n> [<queen_positions>]
```

### Parameters

- `task_id`: Problem type (1-5)
- `m`: Board height
- `n`: Board width
- `queen_positions`: (Optional) List of fixed queen positions for task 5

### Examples

1. Maximum Queens on 8×8 board:
```bash
python3 team5.py 1 8 8
```

2. Maximum Bishops on 5×5 board:
```bash
python3 team5.py 2 5 5
```

3. Maximum Knights on 6×6 board:
```bash
python3 team5.py 3 6 6
```

4. Combined Knights and Bishops on 7×7 board:
```bash
python3 team5.py 4 7 7
```

5. Knights and Bishops with fixed Queens on 8×8 board:
```bash
python3 team5.py 5 9 10 [ "0 0" "2 3" "8 6" ]
```

## Output Format

The program outputs:
- Total number of pieces placed
- Positions of each piece type
- Execution time
- Board visualization
- Validation result

## Requirements

- Python 3.x
- No external dependencies required

## Performance Considerations

- Early termination optimization
- Efficient data structures
- Attack tracking to avoid redundant calculations
- Time tracking for performance analysis
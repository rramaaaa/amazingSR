*This activity has been created as parrt of 42  curriculum by rajarada, sal-qur*

# Description:
A-Maze-ing is a maze generation and solving project developed as part of the 42 curriculum.

The main goal of this activity is to generate a valid maze from a configuration file, display it according to the required format, and provide a solution from the entrance to the exit.

The project focuses on several important programming concepts:

    Parsing and validating configuration files.
    Generating mazes algorithmically.
    Representing and manipulating a two-dimensional grid.
    Finding a path(PERFECT case) or multiple valid paths(IMPERFECT case) through a maze.
    Handling errors and invalid configurations.
    Writing reusable and maintainable code.
    Working efficiently as a team using version control and project-management tools.

The program takes a configuration file as input. This file contains the dimensions and parameters required to generate the maze. The generated maze must respect the requested constraints, including having an entrance, an exit, and a valid path between them.

# Instructions:
## Requirements
This project is implemented in Python.
To run the project, you need:
Python3 installed on your system.
 
## Installation
``` bash 
git clone git@github.com:42learnersCommon-core---A_maze_ing-03c388b2-db67-4770-9165-47512c4f1064.git
cd Common-core---A_maze_ing-03c388b2-db67-4770-9165-47512c4f1064
```

The project has external dependencies we put the a_maze_ing file (that contains the main) in a **mazegen**, to install it:
you need to make a virtual environment and then :
- python3 -m venv .env
- source .env/bin/activate
- pip install build
- make install (using the makefile) or python3 -m build
**- pip install dist/mazegen-1.0.0.tar.gz** **or** **- pip install dist/mazegen-1.0.0.py2.py3-none-any.whl**
then:


# Compiliation
- Compile the project using:

``` bash
make
or
make run
or 
mazegen config.txt (if you had been installed the **mazgen** before)
```
- Compile the project and removes object files using:

```bash
fclean
```
- Removes object files using:
``` bash
clean
```
- To check the flake8 and srtict mypy:
``` bash
make lint-strict
```

- To check the flake8 and normal mypy with some specific constraints
``` bash
make lint
```

# Congig file

The config file must have 6 Keys(required)
HEIGHT = the number of rows of the maze,
WIDTH = the number of columns of the maze,

ENTRY = a user chosen point as a tuple to start entering the maze such as (0,0),

EXIT = a user chosen point as a tuple to exit the maze such as (19,14),

OUTPUT_FILE = a text file that shows the path directions such as SEWN(south, east, weast, north) and a maze walls in hexa-decimal

PERFECT = True(having exactly one path) or PERFECT = False(having more than one path) and SEED = number to make the maze constant(optional).

# Configuration validation
Before generating the maze, the program checks that:

   - All required parameters are present.
   - Numeric values are valid.
   - The maze dimensions are within the allowed limits.
   - The entrance coordinates are valid.
   - The exit coordinates are valid.
   - The configuration does not contain invalid or contradictory values.

Invalid input is handled with an error message rather than allowing the program to continue with incorrect data.

# Algorthims used
**Depth-First Search with backtracking**
 The algorithm starts from a cell and explores an unvisited neighboring cell. When moving to a neighboring cell, the wall between the two cells is removed. The algorithm continues until there are no unvisited neighbors, at which point it backtracks to a previous cell and continues exploring from there.


## Maze Solving

After generating the maze, the program finds a path from the entrance to the exit.

The solver checks neighboring cells and determines whether movement between them is possible. It keeps track of visited cells to avoid infinite loops and reconstructs the path once the exit is reached.

**Bridth-First Search**
To find a path from the entrance to the exit.

BFS explores the maze level by level using a queue. Each visited cell stores its previous cell, allowing us to reconstruct the path once the exit is reached.

Because all movements have the same cost, BFS guarantees the shortest path between the entrance and exit.

The resulting path is then displayed using the format required by the project.
# Resources

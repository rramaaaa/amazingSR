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
- To check the flake8 and 


# Resources

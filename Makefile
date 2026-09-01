PYTHON = python3
MAIN = a_maze_ing.py
CONFIG = config.txt

.PHONY: run debug clean lint lint-strict install

run:
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache

lint:
	flake8 .
	mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

fclean:
	$(PYTHON) $(MAIN) $(CONFIG)
	rm -rf __pycache__
	rm -rf .mypy_cache

install:
	$(PYTHON) -m build

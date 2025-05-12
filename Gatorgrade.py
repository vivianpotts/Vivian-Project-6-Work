(base) vivianpotts@Vivians-MacBook-Pro computer-science-202-algorithm-engineering-project-6-vivianpotts % gatorgrade --config config/gatorgrade.yml
Running set up commands...
🐊 Start to install dependencies ...
🐊 Note: Will not install dependencies if available
Installing dependencies from lock file
The lock file might not be compatible with the current version of Poetry.
Upgrade Poetry to ensure the lock file is read properly or, alternatively, regenerate the lock file with the `poetry lock` command.

No dependencies to install or update

Installing the current project: lcsfinder (0.2.0)
🐊 ... Done installing dependencies
Finished!

✓  Ensure that the __init__.py file exists in the lcsfinder/lcsfinder/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for __init__.py in the lcsfinder/ directory
✓  Ensure that the __init__.py file exists in the lcsfinder/tests/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for __init__.py in the tests/ directory
✓  Ensure that the main.py file exists in the lcsfinder/lcsfinder/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for main.py
✓  Create a sufficient number of docstring (i.e., multiple-line) comments in main.py
✓  Create a sufficient number of single-line comments in main.py
✓  Ensure that the approach.py file exists in the lcsfinder/lcsfinder/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for approach.py
✕  Create a sufficient number of docstring (i.e., multiple-line) comments in approach.py
✓  Ensure that the constants.py file exists in the lcsfinder/lcsfinder/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for constants.py
✓  Create a sufficient number of single-line comments in constants.py
✓  Create a sufficient number of docstring (i.e., multiple-line) comments in constants.py
✓  Ensure that the generate.py file exists in the lcsfinder/lcsfinder/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for generate.py
✕  Create a sufficient number of docstring (i.e., multiple-line) comments in generate.py
✓  Create a sufficient number of single-line comments in generate.py
✓  Ensure that the benchmark.py file exists in the lcsfinder/lcsfinder/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for benchmark.py
✕  Create a sufficient number of docstring (i.e., multiple-line) comments in benchmark.py
✓  Create a sufficient number of single-line comments in benchmark.py
✓  Ensure that the lcs.py file exists in the lcsfinder/lcsfinder/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for lcs.py
✓  Create a sufficient number of docstring (i.e., multiple-line) comments in lcs.py
✓  Create a sufficient number of single-line comments in lcs.py
✓  Ensure that the reflection.md file exists in the writing/ directory
✓  Complete all TODOs, remove the TODO markers, and rewrite comments for the reflection
✓  Delete the 'Add Your Name Here' prompt in the reflection file
✓  Retype the every word in the Honor Code pledge in reflection.md
✓  Confirm that the reflection has a subsection for the references
✓  Confirm that the markdown file has the correct number of headers
✓  Confirm that the markdown file has the correct number of lists of data or commands
✓  Confirm that the markdown file has the correct number of fenced code blocks
✓  Pass the source code linting checks run by mypy
✓  Pass the source code formatting checks run by ruff
✓  Pass the source code linting checks run by ruff
✓  Pass the linting checks run by pymarkdown
✓  Pass the undocumented function checks run by symbex
✕  Pass the untyped function checks run by symbex
✓  Run the recursive algorithm and confirm the correct number of non-blank lines in the benchmark output
✓  Run the dynamic algorithm and confirm the correct number of non-blank lines in the benchmark output
✓  Run the calculate algorithm and confirm the correct number of non-blank lines in the benchmark output
✕  Have at least a specific minimum of commits in repository
Running checks ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━  89%

-~-  FAILURES  -~-

✕  Create a sufficient number of docstring (i.e., multiple-line) comments in approach.py
   → Found 4 comment(s) in the approach.py or the output
✕  Create a sufficient number of docstring (i.e., multiple-line) comments in generate.py
   → Found 2 comment(s) in the generate.py or the output
✕  Create a sufficient number of docstring (i.e., multiple-line) comments in benchmark.py
   → Found 2 comment(s) in the benchmark.py or the output
✕  Pass the untyped function checks run by symbex
   → # File: lcsfinder/benchmark.py Line: 11
     def run_benchmark(algorithm, data_type, start_size, runs, strategy):
     
     # File: lcsfinder/generate.py Line: 18
     def generate_data(size, data_type):
     
     # File: lcsfinder/lcs.py Line: 11
     def lcs_recursive(X, Y):
     
     # File: lcsfinder/lcs.py Line: 21
     def lcs_dynamic(X, Y):
     
     # File: lcsfinder/lcs.py Line: 36
     def lcs_calculate(X, Y):
     
     # File: lcsfinder/main.py Line: 21
     def cli():
     
     # File: lcsfinder/main.py Line: 26
     def parse_arguments():
     
     # File: lcsfinder/main.py Line: 64
     def main():
   → Run this command: cd lcsfinder && poetry run task symbex-typed
✕  Have at least a specific minimum of commits in repository
   → Found 4 commit(s) in the Git repository

╭────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Passed 40/45 (89%) of checks for computer-science-202-algorithm-engineering-project-6-vivianpotts! │
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
(base) vivianpotts@Vivians-MacBook-Pro computer-science-202-algorithm-engineering-project-6-vivianpotts % 

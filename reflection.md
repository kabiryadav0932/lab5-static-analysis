# Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were the missing docstrings and naming conventions, as they only required adding comments or renaming. The hardest was handling mutable default arguments and file operations because it required understanding Python’s memory behavior and context managers.

### 2. Did the static analysis tools report any false positives?
Yes. Pylint flagged the use of `global stock_data`, which was necessary for reassigning data after file loading. This was intentional and not a real problem.

### 3. How would you integrate static analysis tools into your workflow?
I would integrate Pylint, Bandit, and Flake8 into a continuous integration (CI) workflow using GitHub Actions. Each commit could automatically run these tools to ensure clean, secure, and maintainable code before merging.

### 4. What improvements did you observe in code quality after applying the fixes?
The code became cleaner, more readable, and safer. Potential security issues were eliminated, readability improved due to consistent naming and docstrings, and the Pylint score increased from 5.28/10 to 10/10, showing a clear improvement in quality.

# Issues Identified and Fixes

| Issue Type | Line(s) | Description | Fix Approach |
|-------------|----------|--------------|---------------|
| Mutable default argument | 7 | `logs=[]` was shared across calls | Changed default to `None` and initialized inside function |
| Bare except | 21 | Caught all exceptions blindly | Replaced with `except KeyError:` |
| Insecure function usage | 59 | Used `eval()` which is unsafe | Removed `eval()` and replaced with safe `print()` |
| Unused import | 2 | `import logging` not used | Removed unused import |
| Unspecified encoding | 28, 34 | Opened files without specifying encoding | Added `encoding='utf-8'` |
| Missing with context | 28, 34 | `open()` used without context manager | Changed to `with open(file, ...) as f:` |
| Missing docstrings | All functions | Functions lacked documentation | Added short docstrings |
| Invalid naming convention | Multiple | Function names not in `snake_case` | Renamed functions accordingly |

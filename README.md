# PLP Python Week 6

This repository contains the Week 6 Python assignment on error handling with `try` / `except`.

## Files

- `safe_tools.py` – Defines three safe functions (`safe_divide`, `safe_number`, `get_field`) that catch specific errors and return friendly messages instead of crashing.
- `unbreakable.py` – A small interactive program that uses `safe_number` so it can keep running even when the user enters invalid input.

## Why can the `if` check not catch `abc` on its own?

An `if` check can only test conditions you explicitly write, such as `if text == ""` or `if not text.isdigit()`. It cannot *by itself* know that `"abc"` will fail when passed to `int()` unless you write extra logic to validate the string first. Using `try` / `except ValueError` is simpler and more reliable: you attempt the conversion with `int(text)` and let Python raise a `ValueError` if the text is not a valid integer, then handle that case in the `except` block. This way, you catch all kinds of bad numeric input (like `"12.3"`, `" 5 "`, `"abc"`, etc.) in one place without writing many separate `if` conditions.

# Expense Tracker

A command-line expense tracker that saves purchases in a structured CSV file and helps you track your spending overall and by category.

## Features

- Add an expense with an optional name, a category, and an amount.
- Choose from Food, Transport, Services, and Entertainment.
- View total spending and totals by category.
- Save purchases to CSV and load them on the next run.
- Start with an empty list when no saved file exists.
- Validate menu choices and require positive, finite amounts.
- Cancel an expense entry without changing the list.

## Requirements

Python 3. The program uses the built-in `csv` and `math` modules; no additional packages are required.

## Run the tracker

Keep `main.py` and `expense_tools.py` in the same folder. Open a terminal in that folder and run:

```bash
python main.py
```

On Windows, you can also use `py main.py`; on systems where Python is named `python3`, use `python3 main.py`.

The startup call is:

```python
menu(load_expenses('test.csv'), 'test.csv')
```

No edits are needed for normal use. If `test.csv` exists, the program loads it. Otherwise, it starts empty. Saving a nonempty list creates the CSV file. The relative filename refers to the terminal's current working folder, so run the program from the project folder. To use a different filename, change it in both places in the startup call.

## Menu

| Choice | Action |
| --- | --- |
| 1 | Add an expense |
| 2 | Show total spending |
| 3 | Show spending by category |
| 4 | Save expenses and return to the menu |
| 5 | Save and exit |

A name is optional. Choose a category by its displayed number and enter a positive, finite amount, using a decimal point where needed.

Type `quit` at the name, category, or amount prompt to cancel the current entry and return to the menu. Capitalization and surrounding spaces are ignored for this cancellation check. In the main menu, use option 5 to save and exit.

**Expenses are saved only when you choose option 4 or 5.** You can add several purchases before saving them together. Closing the program before saving loses additions since the last save. Saving an empty list displays a message and does not create or overwrite a file.

## Try the sample data

The commented `expenses` list in `main.py` provides sample purchases. To try it:

1. Uncomment the sample list.
2. Replace the normal startup call with:

```python
menu(expenses, 'sample_expenses.csv')
```

This starts from the sample list each time. To continue from saved purchases afterward, use `load_expenses` again with that filename.

## Project files

- `main.py`: starts the program and contains the optional sample data.
- `expense_tools.py`: contains input, validation, calculations, CSV handling, and menu functions.

CSV files contain the columns `name`, `category`, and `amount`. The loader is intended for files produced by this tracker, rather than arbitrary external CSV files.

## Learning focus

Built as a Python refresh project to practise lists of dictionaries, loops, functions, modules, input validation, exception handling, and file persistence.


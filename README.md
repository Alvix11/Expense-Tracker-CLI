# Expense Tracker

A simple command-line Expense Tracker application written in Python. This tool allows you to add, update, delete, list, and summarize your expenses, storing all data in a JSON file.

It is inspired from the Expense Tracker project https://roadmap.sh/projects/expense-tracker featured in the Backend Roadmap from roadmap.sh.

## Features

- **Add Expense:** Add a new expense with description and amount.
- **Update Expense:** Edit an existing expense by its ID.
- **Delete Expense:** Remove an expense by its ID.
- **List Expenses:** Display all recorded expenses in a formatted table.
- **Monthly Summary:** Show the total expenses for a specific month.
- **General Summary:** Show the total of all expenses.

## Usage

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### 2. Install Python (if not already installed)

Make sure you have Python 3.7 or higher.

### 3. Run the application

```sh
python expense-tracker.py <command> [options]
```

### 4. Available Commands

- **Add an expense:**
  ```sh
  python expense-tracker.py add --description "Buy bread" --amount 50
  ```

- **Update an expense:**
  ```sh
  python expense-tracker.py update --id 1 "Buy coffee" 30
  ```

- **Delete an expense:**
  ```sh
  python expense-tracker.py delete --id 1
  ```

- **List all expenses:**
  ```sh
  python expense-tracker.py list
  ```

- **Show monthly summary:**
  ```sh
  python expense-tracker.py summary --month 5
  ```

- **Show general summary:**
  ```sh
  python expense-tracker.py summary
  ```

## File Structure

```
expense-tracker/
├── expense_manager.py
├── helpers.py
├── utils.py
├── settings.py
├── expense-tracker.py
├── expense.json
└── .gitignore
```

- `expense_manager.py`: Main logic for managing expenses.
- `helpers.py`: Helper functions for validation and file operations.
- `utils.py`: Utility functions (e.g., date handling).
- `settings.py`: Argument parsing and configuration.
- `expense-tracker.py`: Entry point for the application.
- `expense.json`: Data storage file.

## Notes

- The `expense.json` file is automatically created when you add your first expense.  
- This file is not tracked by git (`.gitignore`) to avoid committing personal data.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
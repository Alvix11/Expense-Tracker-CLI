import argparse

FILE_PATH = "expense.json" # File name json

def get_parser():
    '''Function to get the user's entries on the console'''

    # A parser is created to receive positional arguments.
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparser = parser.add_subparsers(dest="command", help="Available subcommands")

    # Subcommand add
    add = subparser.add_parser("add", help="Add a new expense")
    add.add_argument("--description", type=str, required=True, help="Expense description")
    add.add_argument("--amount", type=float, required=True, help="Amount expense")

    # Subcommand update
    update = subparser.add_parser("update", help="Update at expense")
    update.add_argument("--id", type=int, required=True, help="Id expense")
    update.add_argument("description", type=str, help="Expense description")
    update.add_argument("amount", type=float, help="Amount expense")

    # Subcommand list
    list = subparser.add_parser("list", help="List expenses")

    # Subcommand delete
    delete = subparser.add_parser("delete", help="Delete an expense")
    delete.add_argument("--id", type=int, required=True, help="Id expense")

    # Subcommand summary
    summary = subparser.add_parser("summary", help="Summary expense for month")
    summary.add_argument("--month", type=int, help="Month expense (optional)")

    return parser.parse_args()
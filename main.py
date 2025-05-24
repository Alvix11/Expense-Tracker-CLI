from settings import get_parser
from expense_manager import ExpenseManager

expense = ExpenseManager()

args = get_parser()

if args.command == "add":
    expense.add_expense(args)
elif args.command == "list":
    expense.list_expenses()
elif args.command == "delete":
    expense.delete_expense(args)
elif args.command == "summary":
    if args.month:
        print(f"sumar mes {args.month}")
    else:
        expense.summary_expense()
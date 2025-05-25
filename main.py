from settings import get_parser
from expense_manager import ExpenseManager

def main():
    '''Run the application'''
    expense = ExpenseManager()
    args = get_parser()
    
    # Here you will control the flow of the CLI application.
    if args.command == "add":
        expense.add_expense(args)
    elif args.command == "list":
        expense.list_expenses()
    elif args.command == "delete":
        expense.delete_expense(args)
    elif args.command == "update":
        expense.update_expense(args)
    elif args.command == "summary":
        if args.month:
            expense.summary_expense_for_month(args)
        else:
            expense.summary_expense()

if __name__ == "__main__":
    main()
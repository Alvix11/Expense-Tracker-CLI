from helpers import load_expense, save_expense, is_text, is_positive
from utils import actual_date_and_time
from settings import FILE_PATH

class ExpenseManager:
    file_path = FILE_PATH

    def add_expense(self, args):
        '''Function to add new expenses'''
        datas = {}
        id = 1
        data = load_expense(self.file_path)
        present_date = actual_date_and_time()

        if is_text(args) and is_positive(args, mode="amount"):

            if data:
                id = max(map(int, data.keys())) + 1
                data[str(id)] = {
                    "date": str(present_date),
                    "description": str(args.description),
                    "amount": str(args.amount)
                }
                save_expense(self.file_path, data)
                print(f"Expense added with id: ({id})")

            else:
                datas[str(id)] = {
                    "date": str(present_date),
                    "description": str(args.description),
                    "amount": str(args.amount)
                }
                save_expense(self.file_path, datas)
                print(f"Expense created with id: ({id})")

    def update_expense(self, args):
        '''Function to update expense'''
        data = load_expense(self.file_path)
        present_date = actual_date_and_time()

        if is_text(args) and is_positive(args, mode="amount") and is_positive(args, mode="id"):
            if data:
                if str(args.id) in data:
                    data[str(args.id)] = {
                        "date": str(present_date),
                        "description": str(args.description),
                        "amount": str(args.amount)
                    }
                    save_expense(self.file_path, data)
                    print(f"Expense updated with id: ({args.id})")
                else:
                    print(f"There are no expenses with this id: ({args.id})")
            else:
                print("There are no expenses to update")


    def delete_expense(self, args):
        '''Function to delete expense'''
        data = load_expense(self.file_path)

        if data:
            if is_positive(args, mode="id"):
                if str(args.id) in data:
                    del data[str(args.id)] # Delete expense
                    save_expense(self.file_path, data)
                    print(f"Expense successfully eliminated id: {args.id}")
                else:
                    print(f"There are no expenses with the id: ({args.id})")        
        else:
            print("There are no expenses to delete")
    
    def list_expenses(self):
        '''Function to list all expenses'''
        data = load_expense(self.file_path)

        if data: 
            # We display the expenses with customized formatting with colors (ANSI Escape Codes)
            print(f"{'#':<1} {'ID':<3} {'Date':<12} {'Description':<16} {'Amount':<6}")
            print("-" * 48)
            for key, value in data.items():
                print(f"{'#':<1} {key:<3} {value.get('date',''):<12} {value.get('description',''):<16} {value.get('amount',''):<6}")
        else:
            print("There are no expenses to show")

    def summary_expense(self):
        '''Function to summary expense'''
        data = load_expense(self.file_path)

        if data:
            amounts = [] # List to store the amounts
            summary = 0 # Variable starting at zero that will contain the sum of expenses

            for key, value in data.items():
                amounts.append(float(value['amount'])) # The amounts are added to the list and converted to float

            summary = sum(amounts) # Sum of amounts
            print(f"Total expenses: {summary}")
        else:
            print("There are no expenses to summary")
    
    def summary_expense_for_month(self, args):
        '''Function to summary expense for month'''
        data = load_expense(self.file_path)
        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                  5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 
                  10: 'October', 11: 'November', 12: 'December'
                  } # Dictionary of months

        if data:
            amounts = []
            summary = 0

            if int(args.month) in months: # It is verified that the month passed by the user exists in the dictionary

                for key, value in data.items():
                    month = value['date'] # The date traveled in the loop is saved and

                    if month[6:7] == str(args.month):  # compares it to the date passed by the user
                        amounts.append(float(value['amount']))

                summary = sum(amounts) # Sum of amounts

                for key, value in months.items():
                
                    if key == int(args.month): # Verify that the password for the month is the same as the user's last month.
                        month_value = value               
                        print(f"Total expenses for {month_value}: {summary}")
                        return
            else:
                print("Enter a valid month")
        else:
            print("There are no expenses to summary")
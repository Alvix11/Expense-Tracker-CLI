from helpers import load_expense, save_expense, is_text, is_number
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

        if is_text(args) and is_number(args):
            
            if data:
                id = max(map(int, data.keys())) + 1
                data[str(id)] = {
                    "date": str(present_date),
                    "description": str(args.description),
                    "amount": str(args.amount)
                }
                save_expense(self.file_path, data)
                print(f"Expense added with id: {id}")

            else:
                datas[str(id)] = {
                    "date": str(present_date),
                    "description": str(args.description),
                    "amount": str(args.amount)
                }
                save_expense(self.file_path, datas)
                print(f"Expense created with id: {id}")
    
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
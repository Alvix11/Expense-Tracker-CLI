from utils import verify_create_json, read_json, write_json

def load_expense(file_path):
    '''Function to load expenses'''
    if verify_create_json(file_path):
        data = read_json(file_path)
        if data:
            return data
        else:
            return {}
        
def save_expense(file_path, data):
    '''Function to save expenses'''
    try:
        write_json(file_path, data)
        return True
    except Exception as e:
        print(f"An error ocurred {e}")
        return False

def is_text(args):
    '''Function to verify that the expense passed by the user is not blank or numbers.'''
    desc = str(args.description).strip()
    if not desc:
        print('Enter a valid expense, no blanks')
        return False
    try:
        float(desc)
        print('Enter a valid expense, not numbers')
        return False
    except ValueError:
        return True

def is_number(args):
    '''Function to verify that the expense passed by the user is not negative number.'''
    num = args.amount
    if num < 0:
        print("You cannot add negative amounts")
        return False
    else:
        return True
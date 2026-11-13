import csv,math




def total_spending(expense_list):
    total = 0
    for exp in expense_list:
        total += exp['amount']

    return total


def spending_by_category(expense_list):
    cat_spending ={}
    if not expense_list:
        print('The are no expenses recorded')
        return cat_spending
    
    for exp in expense_list:
        if exp['category'] in cat_spending.keys():
            cat_spending[exp['category']] += exp['amount']
        else:
            cat_spending[exp['category']] = exp['amount']
    return cat_spending

def add_expense(expense_list):
    result_of_get = get_expense_input()
    if result_of_get is None:
        print('Expense cancelled. No changes made.')
        return
    name, category, amount = result_of_get
    expense_list.append({'name' : name, 'category' : category, 'amount' : amount})
    print('Expense added successfully')

def get_expense_input():
    name = input('Enter the name of product or service: ')
    if name.strip().lower() == 'quit':
        
        return
    

    cat = choose_category_input()
    if cat is None:
        return
   
    while True:
        amount = input('Enter the amount spent on it: ')
        if amount.strip().lower() == 'quit':
            return
        try:
            amount = float(amount) 
            if amount > 0 and math.isfinite(amount):
                break
            else:
                print('Please enter a positive number and a finite number:')
        except ValueError:
            print('Please enter a correct number thx you')


    return name, cat, amount


def choose_category_input():
     cat_list = ["Food", "Transport", "Services", "Entertainment"]
     for i in range(1, len(cat_list)+ 1):
         print(f'{i}. {cat_list[i-1]}')
     while True:
         choice = input('Enter the number of repspective category ')
         if choice.strip().lower() == 'quit':
             return
     
         try:
            choice = int(choice)
            if choice in range(1,len(cat_list)+1):
                cat = cat_list[choice-1]
                break
            else:
                print('Please make a valid choice')
            
         except ValueError:
             print('Please make a valid choice')
     return cat




def save_expenses(expense_list, path):
    if not expense_list:
        print('No expenses to save')
        return
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=expense_list[0].keys())
        writer.writeheader()
        writer.writerows(expense_list)
    print('The addition saved succcessfully')

def load_expenses(path):
    expenses = []
    try:
        with open(path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
        return expenses
    except FileNotFoundError:
        print("No file found, you start wiht an empty list")
        return expenses


def menu(expense_list, path):
    while True:
        print('''
        ==============================
        1. Add an expense.
        2. Show total spending.
        3. Show spending by category.
        4. Save expense.
        5. Save and exit.
        ==============================
        ''')
        while True:
            choice = input('Please select an operation: ').strip()
            if choice not in ['1', '2', '3', '4', '5']:
                print('Please enter a valid choice')
            else:
                break
        if choice== '1':
            add_expense(expense_list)
        if choice == '2':
            print(f'Total spent amount: {total_spending(expense_list):.2f}')
        if choice== '3':
            for cat, amount in spending_by_category(expense_list).items():
                print(f'{cat} {amount:.2f}')

        if choice == '4':
            save_expenses(expense_list, path)
        if choice == '5':
            save_expenses(expense_list, path)
            break
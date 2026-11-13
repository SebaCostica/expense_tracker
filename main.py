from expense_tools import  load_expenses, menu

# expenses = [
#     {"name": "Bread", "category": "Food", "amount": 7.50},
#     {"name": "Milk", "category": "Food", "amount": 8.00},
#     {"name": "Petrol", "category": "Transport", "amount": 150.00},
#     {"name": "Internet", "category": "Services", "amount": 50.00},
#     {"name": "Apples", "category": "Food", "amount": 12.50},
#     {"name": "Bus ticket", "category": "Transport", "amount": 5.00},
#     {"name": "Electricity", "category": "Services", "amount": 120.00},
#     {"name": "Bread", "category": "Food", "amount": 8.00},
#     {"name": "Cinema", "category": "Entertainment", "amount": 35.00},
#     {"name": "Petrol", "category": "Transport", "amount": 100.00},
#     {"name": "Cheese", "category": "Food", "amount": 22.00},
#     {"name": "Netflix", "category": "Entertainment", "amount": 30.00}
# ]


# print(expenses)
menu(load_expenses('test.csv'), 'test.csv')

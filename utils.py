from datetime import datetime

TRANSACTION_TYPES = ["Income", "Expense"]
CATEGORIES = ["Groceries", "Rent", "Utilities", "Entertainment", "Salary", "Other"]

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        return amount > 0
    except ValueError:
        return False

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

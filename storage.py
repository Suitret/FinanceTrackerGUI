import json
import os

class Storage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            return {"transactions": [], "budgets": {}}
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {"transactions": [], "budgets": {}}
        except (json.JSONDecodeError, FileNotFoundError):
            return {"transactions": [], "budgets": {}}

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_transaction(self, transaction):
        self.data["transactions"].append(transaction.to_dict())
        self.save_data()

    def get_transactions(self):
        return self.data["transactions"]

    def set_budget(self, budget):
        self.data["budgets"][budget.category] = budget.amount
        self.save_data()

    def get_budgets(self):
        return self.data["budgets"]

import matplotlib.pyplot as plt
from collections import defaultdict

class ReportGenerator:
    def __init__(self, storage):
        self.storage = storage

    def show_report(self):
        transactions = self.storage.get_transactions()
        budgets = self.storage.get_budgets()

        # Calculate spending by category
        spending_by_category = defaultdict(float)
        for transaction in transactions:
            if transaction["type"] == "Expense":
                spending_by_category[transaction["category"]] += transaction["amount"]

        # Prepare report
        report = "Spending Report by Category:\n"
        report += "-------------------------\n"
        for category, amount in spending_by_category.items():
            budget = budgets.get(category, 0.0)
            report += f"{category}:\n"
            report += f"  Spent: ${amount:.2f}\n"
            report += f"  Budget: ${budget:.2f}\n"
            report += f"  Remaining: ${budget - amount:.2f}\n" if budget > 0 else "  No budget set\n"
            report += "-------------------------\n"

        # Display report in console
        print(report)

        # Create pie chart for spending by category
        if spending_by_category:
            labels = list(spending_by_category.keys())
            sizes = list(spending_by_category.values())
            plt.figure(figsize=(8, 6))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title("Spending by Category")
            plt.axis('equal')
            plt.show()

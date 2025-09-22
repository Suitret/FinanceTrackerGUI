import tkinter as tk
from tkinter import messagebox, ttk
from transaction import Transaction
from budget import Budget
from reports import ReportGenerator
from utils import validate_amount, validate_date, TRANSACTION_TYPES, CATEGORIES

class FinanceTrackerGUI:
    def __init__(self, root, storage):
        self.root = root
        self.storage = storage
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x600")

        # Input fields
        self.create_input_fields()
        # Buttons
        self.create_buttons()
        # Transaction list
        self.create_transaction_list()

        # Load and display transactions
        self.refresh_transaction_list()

    def create_input_fields(self):
        # Frame for inputs
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Amount
        tk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(input_frame, width=50)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        # Type
        tk.Label(input_frame, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        self.type_var = tk.StringVar(value=TRANSACTION_TYPES[0])
        self.type_menu = ttk.Combobox(input_frame, textvariable=self.type_var, values=TRANSACTION_TYPES, state="readonly")
        self.type_menu.grid(row=1, column=1, padx=5, pady=5)

        # Category
        tk.Label(input_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5)
        self.category_var = tk.StringVar(value=CATEGORIES[0])
        self.category_menu = ttk.Combobox(input_frame, textvariable=self.category_var, values=CATEGORIES, state="readonly")
        self.category_menu.grid(row=2, column=1, padx=5, pady=5)

        # Date
        tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(input_frame, width=50)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        # Description
        tk.Label(input_frame, text="Description:").grid(row=4, column=0, padx=5, pady=5)
        self.desc_entry = tk.Text(input_frame, height=4, width=50)
        self.desc_entry.grid(row=4, column=1, padx=5, pady=5)

        # Budget
        tk.Label(input_frame, text="Budget Amount:").grid(row=5, column=0, padx=5, pady=5)
        self.budget_entry = tk.Entry(input_frame, width=50)
        self.budget_entry.grid(row=5, column=1, padx=5, pady=5)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Transaction", command=self.add_transaction).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Set Budget", command=self.set_budget).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Generate Report", command=self.generate_report).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

    def create_transaction_list(self):
        # Frame for transaction list
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview for transactions
        self.transaction_list = ttk.Treeview(
            list_frame,
            columns=("Amount", "Type", "Category", "Date"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        self.transaction_list.heading("Amount", text="Amount")
        self.transaction_list.heading("Type", text="Type")
        self.transaction_list.heading("Category", text="Category")
        self.transaction_list.heading("Date", text="Date")
        self.transaction_list.column("Amount", width=100)
        self.transaction_list.column("Type", width=100)
        self.transaction_list.column("Category", width=150)
        self.transaction_list.column("Date", width=100)
        self.transaction_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.transaction_list.yview)

    def add_transaction(self):
        amount = self.amount_entry.get().strip()
        type_ = self.type_var.get()
        category = self.category_var.get()
        date = self.date_entry.get().strip()
        description = self.desc_entry.get("1.0", tk.END).strip()

        # Validate inputs
        if not validate_amount(amount):
            messagebox.showerror("Error", "Invalid amount. Must be a positive number.")
            return
        if not validate_date(date):
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return
        if not description:
            messagebox.showerror("Error", "Description is required.")
            return

        transaction = Transaction(amount, type_, category, date, description)
        self.storage.add_transaction(transaction)
        self.refresh_transaction_list()
        self.clear_fields()
        messagebox.showinfo("Success", "Transaction added successfully.")

    def set_budget(self):
        category = self.category_var.get()
        amount = self.budget_entry.get().strip()

        # Validate inputs
        if not validate_amount(amount):
            messagebox.showerror("Error", "Invalid budget amount. Must be a positive number.")
            return

        budget = Budget(category, amount)
        self.storage.set_budget(budget)
        self.clear_fields()
        messagebox.showinfo("Success", f"Budget for {category} set to {amount}.")

    def generate_report(self):
        report_generator = ReportGenerator(self.storage)
        report_generator.show_report()

    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.type_var.set(TRANSACTION_TYPES[0])
        self.category_var.set(CATEGORIES[0])
        self.date_entry.delete(0, tk.END)
        self.desc_entry.delete("1.0", tk.END)
        self.budget_entry.delete(0, tk.END)

    def refresh_transaction_list(self):
        # Clear current list
        for item in self.transaction_list.get_children():
            self.transaction_list.delete(item)

        # Populate with transactions
        for transaction in self.storage.get_transactions():
            self.transaction_list.insert("", tk.END, values=(
                f"{transaction['amount']:.2f}",
                transaction["type"],
                transaction["category"],
                transaction["date"]
            ))

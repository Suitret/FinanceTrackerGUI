# Personal Finance Tracker

This is a Python-based Personal Finance Tracker with a graphical user interface (GUI) built using `tkinter`. It allows users to record income and expenses, categorize transactions, set budgets, and generate spending reports with visualizations. Data is stored persistently in a JSON file.

## Features
- Add income and expense transactions with amount, category, date, and description.
- Set and track monthly budgets per category.
- View all transactions in a scrollable list.
- Generate reports showing spending by category and budget status.
- Visualize spending with a pie chart using `matplotlib`.
- Persistent storage using JSON.
- Input validation for amounts, dates, and required fields.

## File Structure
```
finance_tracker/
├── main.py              # Entry point to run the application
├── transaction.py      # Transaction class definition
├── budget.py           # Budget class for managing category budgets
├── storage.py          # Handles JSON file operations
├── ui.py               # GUI implementation with tkinter
├── reports.py          # Generates reports and visualizations
├── utils.py            # Helper functions for validation and formatting
├── config.py           # Configuration settings
└── README.md           # Project documentation
```

## Setup Instructions
1. **Prerequisites**:
   - Python 3.6 or higher.
   - `tkinter` (included with standard Python installations).
   - `matplotlib` for visualizations. Install it using:
     ```bash
     pip install matplotlib
     ```

2. **Installation**:
   - Clone or download the project files to a `finance_tracker` directory.
   - Install the required dependency:
     ```bash
     pip install matplotlib
     ```

3. **Running the Application**:
   - Navigate to the `finance_tracker` directory.
   - Run the following command:
     ```bash
     python main.py
     ```
   - The GUI will open, allowing you to manage transactions and budgets.

4. **Data Storage**:
   - Transactions and budgets are saved in `data.json` in the project directory.
   - The file is created automatically when you add your first transaction or budget.

## Usage
- **Add Transaction**: Fill in the transaction details (amount, type, category, date, description) and click "Add Transaction".
- **Set Budget**: Enter a category and budget amount, then click "Set Budget".
- **View Transactions**: All transactions are displayed in a scrollable list, showing amount, type, category, and date.
- **Generate Report**: Click "Generate Report" to view a summary of spending by category and budget status, along with a pie chart.
- **Clear Fields**: Click "Clear Fields" to reset the input fields.

## Example Data
Data is stored in `data.json` in the following format:
```json
{
  "transactions": [
    {
      "amount": 50.0,
      "type": "Expense",
      "category": "Groceries",
      "date": "2025-09-22",
      "description": "Weekly grocery shopping"
    }
  ],
  "budgets": {
    "Groceries": 200.0,
    "Rent": 1000.0
  }
}
```

## Development Notes
- The application uses `tkinter` for the GUI, making it cross-platform.
- `matplotlib` is used for generating pie charts in reports.
- Data is stored in a JSON file for simplicity and persistence.
- Input validation ensures valid amounts, dates, and required fields.
- The code is modular, separating concerns for transactions, budgets, storage, UI, and reporting.

## Future Improvements
- Add filtering for transactions by date or category.
- Implement monthly budget resets.
- Export reports to PDF or CSV.
- Enhance the GUI with themes or additional styling.

## License
This project is licensed under the MIT License.
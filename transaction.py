class Transaction:
    def __init__(self, amount, type_, category, date, description):
        self.amount = float(amount)
        self.type_ = type_  # Income or Expense
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "amount": self.amount,
            "type": self.type_,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["amount"],
            data["type"],
            data["category"],
            data["date"],
            data["description"]
        )

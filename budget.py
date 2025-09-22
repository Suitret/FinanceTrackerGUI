class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = float(amount)

    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["category"],
            data["amount"]
        )

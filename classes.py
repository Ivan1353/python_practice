class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: int, quantity=0):
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

item1 = Item("Computer", 1000)
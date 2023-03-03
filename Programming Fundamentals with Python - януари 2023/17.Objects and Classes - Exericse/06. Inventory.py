class Inventory:
    __capacity: int

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        Inventory.__capacity = capacity

    def add_item(self, item):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return "not enough room in the inventory"

    @staticmethod
    def get_capacity():
        return Inventory.__capacity

    def __repr__(self):
        items = ", ".join(self.items)
        return f"Items: {items}.\nCapacity left: {self.capacity}"
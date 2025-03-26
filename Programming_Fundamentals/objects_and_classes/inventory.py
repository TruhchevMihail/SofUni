class Inventory:
    __capacity = 0

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            return self.items.append(item)
        return "not enough room in the inventory"
    
    def get_capacity(self):
        return self.__capacity
    
    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"

    def __str__(self):
        return self.__repr__()



inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

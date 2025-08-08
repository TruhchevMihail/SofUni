class FlowerShopManager:
    def __init__(self):
        self.income: float = 0.0
        self.plants: list = []
        self.clients: list = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in ["Flower", "LeafPlant"]:
            raise ValueError("Unknown plant type!")

        if plant_type == "Flower":
            from project.plants.flower import Flower
            plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        else:
            from project.plants.leaf_plant import LeafPlant
            plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)

        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in ["RegularClient", "BusinessClient"]:
            raise ValueError("Unknown client type!")

        for client in self.clients:
            if client.phone_number == client_phone_number:
                raise ValueError("This phone number has been used!")

        if client_type == "RegularClient":
            from project.clients.regular_client import RegularClient
            client = RegularClient(client_name, client_phone_number)
        else:
            from project.clients.business_client import BusinessClient
            client = BusinessClient(client_name, client_phone_number)

        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")

        available_plants = [p for p in self.plants if p.name == plant_name]
        if not available_plants:
            raise ValueError("Plants not found!")

        if len(available_plants) < plant_quantity:
            return "Not enough plant quantity."

        order_amount = available_plants[0].price * plant_quantity * (1 - client.discount / 100)

        for _ in range(plant_quantity):
            plant = next(p for p in self.plants if p.name == plant_name)
            self.plants.remove(plant)

        self.income += order_amount
        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        if plant_name not in [p.name for p in self.plants]:
            return "No such plant name."

        for plant in self.plants:
            if plant.name == plant_name:
                self.plants.remove(plant)
                return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        remove_count = 0
        clients_to_remove = []

        for client in self.clients:
            if client.total_orders == 0:
                clients_to_remove.append(client)
                remove_count += 1

        for client in clients_to_remove:
            self.clients.remove(client)

        return f"{remove_count} client/s removed."

    def shop_report(self):
        report = ["~Flower Shop Report~"]
        report.append(f"Income: {self.income:.2f}")

        total_orders = sum(client.total_orders for client in self.clients)
        report.append(f"Count of orders: {total_orders}")

        report.append("~~Unsold plants: {}~~".format(len(self.plants)))

        plant_counts = {}
        for plant in self.plants:
            plant_counts[plant.name] = plant_counts.get(plant.name, 0) + 1

        sorted_plants = sorted(plant_counts.items(), key=lambda x: (-x[1], x[0]))

        for plant_name, count in sorted_plants:
            report.append(f"{plant_name}: {count}")

        report.append(f"~~Clients number: {len(self.clients)}~~")

        sorted_clients = sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number))

        for client in sorted_clients:
            report.append(client.client_details())

        return "\n".join(report)

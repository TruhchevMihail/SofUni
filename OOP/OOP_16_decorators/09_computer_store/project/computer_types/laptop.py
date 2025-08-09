from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    MAX_RAM = 64

    def __init__(self, manufacturer: str, model:str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f'{processor} is not compatible with laptop {self.manufacturer} {self.model}!')

        if ram > self.MAX_RAM or ram < 2 or (ram & (ram - 1)) != 0:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        ram_price = (ram.bit_length() - 1) * 100
        self.price = self.AVAILABLE_PROCESSORS[processor] + ram_price

        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'
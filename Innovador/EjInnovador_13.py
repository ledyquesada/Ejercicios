# Patron builder


class ElectronicProduct:
    def __init__(self):
        self.storage = ""
        self.memory = ""
        self.processor = ""

    def display_info(self):
        print(f"Storage: {self.storage}")
        print(f"Memory: {self.memory}")
        print(f"Processor: {self.processor}")

class ElectronicProductBuilder(ABC):
    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    @abstractmethod
    def build_processor(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

class ComputerBuilder(ElectronicProductBuilder):
    def __init__(self):
        self.product = ElectronicProduct()

    def build_storage(self):
        self.product.storage = "1TB HDD"

    def build_memory(self):
        self.product.memory = "16GB RAM"

    def build_processor(self):
        self.product.processor = "Intel Core i7"

    def get_product(self):
        return self.product

# Uso del Builder
computer_builder = ComputerBuilder()
computer_builder.build_storage()
computer_builder.build_memory()
computer_builder.build_processor()
computer = computer_builder.get_product()
computer.display_info()

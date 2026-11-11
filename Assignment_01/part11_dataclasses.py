#Warm-up:
"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""
def add(a: int, b: int) -> int:
    return a + b
def calculate_average(marks: list[int]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)
def check_result(average: float) -> str:
    if average >= 50:
        return "Pass"
    return "Fail"
marks: list[int] = [80, 90, 70]
print(calculate_average(marks))
print(check_result(calculate_average(marks)))

# Build:

from dataclasses import dataclass, field
@dataclass(order=True)
class Product:
    price: float
    name: str
    stock: int
    tags: list[str] = field(default_factory=list)
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative")
products = [
    Product(100, "Pen", 0),
    Product(500, "Bag", 5),
    Product(50, "Pencil", 0),
    Product(200, "Book", 10),
    Product(800, "Shoes", 0)
]
print("Out of stock products:")
for product in products:
    if product.stock == 0:
        print(product.name)

# Challenge:
import json
from dataclasses import asdict, dataclass, field
@dataclass(order=True)
class Product:
    price: float
    name: str
    stock: int
    tags: list[str] = field(default_factory=list)
    def __post_init__(self):
        if self.price < 0 or self.stock < 0:
            raise ValueError("Invalid product data")
products = [
    Product(100, "Pen", 10, ["stationery"]),
    Product(500, "Bag", 5, ["school"]),
    Product(50, "Pencil", 0, ["stationery"])
]

with open("products.json", "w") as file:
    json.dump([asdict(p) for p in products], file, indent=4)
with open("products.json", "r") as file:
    data = json.load(file)
loaded_products = [Product(**d) for d in data]
loaded_products.sort(key=lambda p: p.price)
for product in loaded_products:
    print(product)

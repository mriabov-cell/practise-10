from abc import ABC, abstractmethod
from typing import Optional



class Telement(ABC):
    def __init__(self, left: Optional['Telement'] = None, right: Optional['Telement'] = None):
        self.left = left
        self.right = right

    @abstractmethod
    def result(self) -> float:
        pass


class Number(Telement):
    def __init__(self, value: float):
        super().__init__(None, None)
        self.value = float(value)

    def result(self) -> float:
        return self.value


class Plus(Telement):
    def result(self) -> float:
        return self.left.result() + self.right.result()


class Mult(Telement):
    def result(self) -> float:
        return self.left.result() * self.right.result()



def print_graph(node: Telement, level: int = 0, prefix: str = "Root: "):
    if node is None:
        return
    indent = "    " * level
    if isinstance(node, Plus):
        val = "+"
    elif isinstance(node, Mult):
        val = "*"
    elif isinstance(node, Number):
        val = str(node.value)
    else:
        val = "?"

    print(f"{indent}{prefix}[{val}] (rezult = {node.result()})")
    if node.left or node.right:
        print_graph(node.left, level + 1, "L--> ")
        print_graph(node.right, level + 1, "R--> ")



print("=== ВПРАВА 1: Обчислення дерева виразу 3*4+2 ===")


a = Number(3)
b = Number(4)
c = Number(2)

m = Mult(a, b)
p = Plus(m, c)

print("\n--- Деревоподібний граф виразу ---")
print_graph(p)

print("\n--- Значення у вузлах ---")
print(f"Результат листку a (3): {a.result()}")
print(f"Результат піддерева m (3*4): {m.result()}")
print(f"Результат кореня p (3*4+2): {p.result()}")



class BookReplacementService:


    @staticmethod
    def calculate_replacement_fee(base_price: float, rarity_coeff: float, service_fee: float) -> float:
        n_base = Number(base_price)
        n_rarity = Number(rarity_coeff)
        n_service = Number(service_fee)

        mult_node = Mult(n_base, n_rarity)
        total_tree = Plus(mult_node, n_service)
        return total_tree.result()


fee = BookReplacementService.calculate_replacement_fee(3, 4, 2)
print(f"\n[ІС Бібліотека] Сума компенсації за втрачену книгу: {fee} грн")
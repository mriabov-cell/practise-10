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


    def __init__(self, left: Optional[Telement] = None, right: Optional[Telement] = None):
        super().__init__(left, right)

    def result(self) -> float:
        return self.left.result() + self.right.result()


class Mult(Telement):


    def __init__(self, left: Optional[Telement] = None, right: Optional[Telement] = None):
        super().__init__(left, right)

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




def form(expression: str, x_val: float = 0.0, y_val: float = 0.0) -> Telement:
    s = expression.replace(" ", "")

    if '+' in s:
        p = s.find('+')
        s1 = s[:p]
        s2 = s[p + 1:]
        node = Plus()
        node.left = form(s1, x_val, y_val)
        node.right = form(s2, x_val, y_val)
        return node

    elif '*' in s:
        p = s.find('*')
        s1 = s[:p]
        s2 = s[p + 1:]
        node = Mult()
        node.left = form(s1, x_val, y_val)
        node.right = form(s2, x_val, y_val)
        return node

    elif s == 'x':
        return Number(x_val)

    elif s == 'y':
        return Number(y_val)


    else:
        return Number(float(s))




if __name__ == "__main__":
    print("=== ВПРАВА 2: Обчислення функції f(x, y) ===")

    expression_str = "x*x+2*x+y"
    x_input = 3.0
    y_input = 5.0

    # Побудова графа
    tree_fxy = form(expression_str, x_val=x_input, y_val=y_input)

    print(f"\nВираз: f(x, y) = {expression_str}")
    print(f"Вхідні дані: x = {x_input}, y = {y_input}")

    print("\n--- Деревоподібний граф побудованого виразу ---")
    print_graph(tree_fxy)

    print(f"\nРезультат обчислення f({x_input}, {y_input}): {tree_fxy.result()}")



    class LibraryPenaltyCalculator:


        @staticmethod
        def compute_overdue_penalty(formula_from_db: str, overdue_days: float, daily_rate: float) -> float:
            penalty_tree = form(formula_from_db, x_val=overdue_days, y_val=daily_rate)
            return penalty_tree.result()


    db_formula = "x*y+5"
    days = 10.0
    rate = 2.5

    total_penalty = LibraryPenaltyCalculator.compute_overdue_penalty(db_formula, overdue_days=days, daily_rate=rate)

    print("\n--- Інтеграція для ІС Бібліотека ---")
    print(f"Формула розрахунку пені з БД: {db_formula}")
    print(f"Прострочено днів (x): {days}, Тариф/день (y): {rate} грн")
    print(f"Розрахована пеня: {total_penalty} грн")
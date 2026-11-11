def calculate_discount(price: float, discount: float) -> float:
    return price * (100 - discount) / 100


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    return first_name + " " + last_name
# simple_utils.py - A utility library
from typing import Sequence

def reverse_string(text: str) -> str:
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence: str) -> int:
    """Counts the number of words in a sentence."""
    return len(sentence.split())

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def calculate_average(numbers: Sequence[float]) -> float:
    """Calculates the average of a sequence of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty sequence")
    return sum(numbers) / len(numbers)

def parse_user_input(data: str) -> dict[str, str | int]:
    """Parse a comma-separated string into a user record."""
    parts = [part.strip() for part in data.split(",", maxsplit=2)]

    if len(parts) != 3 or any(not part for part in parts):
        raise ValueError('Input must be in the format "name,age,email"')

    name, age_text, email = parts

    try:
        age = int(age_text)
    except ValueError as exc:
        raise ValueError("Age must be a valid integer") from exc

    if "@" not in email:
        raise ValueError("Email must contain '@'")

    return {"name": name, "age": age, "email": email}

class DataProcessor:
    """Processes numeric data by applying transformations."""

    def __init__(self) -> None:
        """Initializes the processor with an empty data list."""
        self.data: list[float] = []

    def process(self) -> list[float]:
        """Returns a new list with each element multiplied by 2."""
        return [x * 2 for x in self.data]
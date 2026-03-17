# random_number_generator.py
import random

def generate_random_number():
    """Generates a random number between 1 and 6 (inclusive)."""
    try:
        return random.randint(1, 6)
    except Exception as e:
        print(f"Error: Failed to generate a random number: {e}")
        return None

if __name__ == "__main__":
    number = generate_random_number()
    if number:
        print(f"Generated number: {number}")
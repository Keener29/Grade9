"""
PUZZLE 2: THE KEYPAD 🔢

You found a keypad! It needs a special combination of numbers.
Fix the bugs to generate the correct combination!

CLUE: Python needs to know about functions from other modules. How do you bring them in?
"""

# BUG: Missing import! We need the 'random' module
# Remove this comment and add the import statement! TODO: Lookup what module we need to import
from random import randint

def generate_combination():
    """Generate a 4-digit combination code."""
    # This should create a list of 4 random digits between 0 and 9
    combination = []
    for i in range(4):
        digit = randint(0, 9)  # BUG: randint is not defined! Need to import it
        combination.append(digit)
    
    return combination

def check_combination(code):
    """Check if the combination is valid (all digits between 0-9)."""
    if len(code) == 4:  # BUG: Variable should be 'code' not 'comb'
        for digit in code:  # BUG: Should be 'code' not 'comb'
            if not (0 <= digit <= 9):
                return False
        return True
    return False

def solve():
    """This function checks if the puzzle is solved correctly."""
    combination = generate_combination()
    
    if check_combination(combination):
        print("✅ Puzzle 2: Keypad unlocked! Combination accepted!")
        print(f"   Combination: {combination}")
        return True
    else:
        print("❌ Puzzle 2: Invalid combination! Keep debugging!")
        return False

if __name__ == "__main__":
    solve()


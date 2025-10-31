"""
PUZZLE 1: THE DOOR LOCK 🚪

The first door is locked! To unlock it, you need to calculate the secret code.
Fix the bugs in this code to unlock the door!

CLUE: Look carefully at the syntax - Python is very particular about punctuation!
"""

def calculate_code()  # BUG: Missing colon after function definition!
    # This function should calculate: (10 + 5) * 2 = 30
    result = (10 + 5) * 2
    return result

def solve():
    """This function checks if the puzzle is solved correctly."""
    expected_code = 30
    
    # BUG: Missing colon after 'if'
    if calculate_code() == expected_code  # Missing colon here too!
        print("✅ Puzzle 1: Door unlocked! The code is correct!")
        return True
    else:
        print("❌ Puzzle 1: Wrong code! The door is still locked.")
        print(f"   Expected: {expected_code}, Got: {calculate_code()}")
        return False

if __name__ == "__main__":
    solve()


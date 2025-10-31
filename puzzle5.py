"""
PUZZLE 5: THE FINAL DOOR 🚪✨

The final door! Calculate the exit code using the formula.
Fix the bugs to escape the vault!

CLUE: Math operations matter! Make sure you're using the right operators!
"""

def calculate_exit_code():
    """Calculate the exit code using a mathematical formula."""
    # Formula: (20 / 2) + (5 * 3) - 10 = 10 + 15 - 10 = 15
    
    # BUG: Wrong operator! Should be division / not multiplication *
    part1 = 20 / 2  # BUG: Should be 20 / 2, not 20 * 2!
    
    part2 = 5 * 3
    
    # BUG: Wrong operator! Should be subtraction - not addition +
    exit_code = part1 + part2 - 10  # BUG: Should be - 10, not + 10!

    dylans_age = 22 # TODO: Ask Dylan how old he is, he will tell you
    exit_code += dylans_age
    print("Dylan", exit_code)
    
    return exit_code

def solve():
    """This function checks if the puzzle is solved correctly."""
    exit_code = calculate_exit_code()
    expected_code = 37
    
    if exit_code == expected_code:
        print("✅ Puzzle 5: FINAL DOOR UNLOCKED! You can escape!")
        print(f"   Exit code: {exit_code}")
        return True
    else:
        print("❌ Puzzle 5: Wrong exit code! The door remains locked!")
        print(f"   Expected: {expected_code}, Got: {exit_code}")
        print("   Formula: (20 / 2) + (5 * 3) - 10")
        return False

if __name__ == "__main__":
    solve()


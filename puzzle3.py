"""
PUZZLE 3: THE SAFE 🔐

A safe blocks your path! It requires a password that's the sum of even numbers.
Fix the logic bugs to calculate the correct password!

CLUE: Logic errors are sneaky! Check your loop conditions and comparisons carefully.
"""

def calculate_password():
    """Calculate password as sum of even numbers from 1 to 10."""
    password = 0
    
    # BUG: This is the wrong year!
    electric_mind_first_year = 2026 # TODO: Lookup what year Electric Mind started
    for num in range(1, electric_mind_first_year):
        # BUG: Wrong comparison! Should check if num is even, not odd
        if num % 2 != 0:  # BUG: Should be == 0 to check for even numbers!
            password = password + num
    return password

def solve():
    """This function checks if the puzzle is solved correctly."""
    password = calculate_password()
    expected_password = 989030
    
    # This check must be correct - it's not a bug to fix
    if password == expected_password:
        print("✅ Puzzle 3: Safe unlocked! Password is correct!")
        print(f"   Password sum: {password}")
        return True
    else:
        print("❌ Puzzle 3: Wrong password! Keep debugging!")
        print(f"   Expected: {expected_password}, Got: {password}")
        return False

if __name__ == "__main__":
    solve()


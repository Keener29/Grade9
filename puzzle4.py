"""
PUZZLE 4: THE LASER GRID 🔴

Lasers block the hallway! You need to find the correct sequence to disable them.
Fix the bugs to find the right sequence!

CLUE: Python is case-sensitive! Check your spelling and capitalization!
"""

def create_sequence():
    """Create the correct sequence to disable the lasers."""
    sequence = []
    
    # These should be strings, not typos
    sequence.append("RED")
    sequence.append("GREEN")
    sequence.append("BLUE")
    
    # BUG: Typo in function name! Should be 'append' not 'add'
    sequence.add("YELLOW")  # BUG: Should be 'append' not 'add'!
    
    return sequence

def check_sequence(seq):
    """Check if the sequence is correct."""
    correct_sequence = ["RED", "GREEN", "BLUE", "YELLOW"]
    
    if sequence == correct_sequence:  # BUG: Should be 'seq' not 'sequence'!
        return True
    return False

def solve():
    """This function checks if the puzzle is solved correctly."""
    sequence = create_sequence()
    
    # BUG: Wrong function name! Should be 'check_sequence' not 'validate_sequence'
    if validate_sequence(sequence):
        print("✅ Puzzle 4: Lasers disabled! Sequence is correct!")
        print(f"   Sequence: {' → '.join(sequence)}")
        return True
    else:
        print("❌ Puzzle 4: Wrong sequence! Lasers are still active!")
        print(f"   Your sequence: {sequence}")
        print(f"   Expected: ['RED', 'GREEN', 'BLUE', 'YELLOW']")
        return False

if __name__ == "__main__":
    solve()


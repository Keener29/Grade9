"""
PUZZLE 6: THE MASTER CONTROL PANEL 🎛️

The master control panel! Decode the secret message to unlock the vault exit.
Fix the bugs to decode the message!

CLUE: Strings in Python can be reversed using slicing! Remember: [::-1] reverses a string.
"""

def decode_message(encoded_message):
    """Decode the message by reversing it and converting to uppercase."""
    # BUG: String slicing syntax is wrong! Should be [::-1] to reverse
    # BUG: Missing the second colon! [:-1] only removes the last character, not reverses
    decoded = encoded_message[:-1]  # BUG: Should be [::-1] to reverse the entire string!
    
    # BUG: Should convert to uppercase, but using wrong method name
    # Python strings use .upper() not .uppercase()
    decoded = decoded.uppercase()  # BUG: Should be .upper() not .uppercase()!
    
    return decoded

def solve():
    """This function checks if the puzzle is solved correctly."""
    encoded = "esrev"
    expected_message = "VERSE"  # "esrev" reversed is "verse", then uppercased is "VERSE"
    
    message = decode_message(encoded)
    
    if message == expected_message:
        print("✅ Puzzle 6: MASTER CONTROL UNLOCKED! The vault is opening!")
        print(f"   Decoded message: {message}")
        return True
    else:
        print("❌ Puzzle 6: Wrong message! The control panel is still locked!")
        print(f"   Expected: {expected_message}, Got: {message}")
        print(f"   Hint: The encoded message is '{encoded}' - try reversing it!")
        return False

if __name__ == "__main__":
    solve()

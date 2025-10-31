#!/usr/bin/env python3
"""
🎮 CODE VAULT ESCAPE ROOM 🎮

You're trapped in a digital vault! To escape, you must fix bugs in each puzzle.
Complete all 6 puzzles to unlock the exit and escape!

Instructions:
1. Run this file: python escape_room.py
2. You'll be given clues about bugs in each puzzle file
3. Fix the bugs in puzzle1.py, puzzle2.py, puzzle3.py, puzzle4.py, puzzle5.py, and puzzle6.py
4. Run each puzzle file after fixing it
5. When all 6 puzzles pass, you'll get the escape code!

Good luck, coders! 🚀
"""

import os
import sys
import importlib.util
import platform

# ANSI color codes for fun terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header():
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*60}")
    print("   🎮 CODE VAULT ESCAPE ROOM 🎮")
    print(f"{'='*60}{Colors.END}\n")
    print(f"{Colors.YELLOW}You're trapped in a digital vault!")
    print("To escape, you must fix bugs in each puzzle.")
    print("Complete all 6 puzzles to unlock the exit!\n{Colors.END}")

def check_puzzle(puzzle_number):
    """Check if a puzzle file has been fixed correctly."""
    puzzle_file = f"puzzle{puzzle_number}.py"
    
    if not os.path.exists(puzzle_file):
        print(f"{Colors.RED}❌ {puzzle_file} not found!{Colors.END}")
        return False
    
    try:
        # Import and run the puzzle
        spec = importlib.util.spec_from_file_location(f"puzzle{puzzle_number}", puzzle_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if puzzle has a main function that returns True when solved
        if hasattr(module, 'solve'):
            result = module.solve()
            return result
        else:
            print(f"{Colors.RED}❌ Puzzle {puzzle_number} doesn't have a solve() function!{Colors.END}")
            return False
            
    except SyntaxError as e:
        print(f"{Colors.RED}❌ Puzzle {puzzle_number} has syntax errors! Fix them first.{Colors.END}")
        print(f"{Colors.YELLOW}Error: {e}{Colors.END}")
        return False
    except Exception as e:
        print(f"{Colors.RED}❌ Puzzle {puzzle_number} has errors! Keep debugging!{Colors.END}")
        print(f"{Colors.YELLOW}Error: {e}{Colors.END}")
        return False

def get_puzzle_hint(puzzle_number):
    """Provide hints for each puzzle."""
    hints = {
        1: "Look for missing punctuation and check indentation!",
        2: "Did you import everything you need? Check variable names too!",
        3: "Logic errors are tricky! Check your comparisons and loop conditions.",
        4: "Is everything spelled correctly? Check function names and variables.",
        5: "Are you using the right operators? Check math operations!",
        6: "String slicing and methods! Check the syntax for reversing strings."
    }
    return hints.get(puzzle_number, "Keep debugging!")

def generate_escape_code():
    """Generate a unique escape code based on system information."""
    # Get system info available on all OS
    username = os.environ.get('USER') or os.environ.get('USERNAME') or 'user'
    hostname = os.environ.get('HOSTNAME') or os.environ.get('COMPUTERNAME') or platform.node() or 'computer'
    
    # Create a simple hash-like code from username and hostname
    # Take first 3 chars of username and hostname, uppercase them
    user_part = username[:3].upper() if len(username) >= 3 else username.upper().ljust(3, 'X')
    host_part = hostname[:3].upper() if len(hostname) >= 3 else hostname.upper().ljust(3, 'X')
    
    # Generate a numeric part based on the sum of character codes
    numeric_part = str((sum(ord(c) for c in username) + sum(ord(c) for c in hostname)) % 10000)
    
    # Format: BUG-USER-HOST-NUM
    escape_code = f"BUG-{user_part}-{host_part}-{numeric_part.zfill(4)}"
    
    return escape_code

def main():
    print_header()
    
    puzzles = [1, 2, 3, 4, 5, 6]
    solved = []
    
    print(f"{Colors.BLUE}{Colors.BOLD}📋 Puzzle Checklist:{Colors.END}\n")
    
    while len(solved) < len(puzzles):
        print(f"\n{Colors.MAGENTA}{'─'*60}{Colors.END}")
        print(f"{Colors.CYAN}Current Progress: {len(solved)}/{len(puzzles)} puzzles solved{Colors.END}")
        
        for puzzle_num in puzzles:
            if puzzle_num in solved:
                status = f"{Colors.GREEN}✅ SOLVED{Colors.END}"
            else:
                status = f"{Colors.RED}❌ NOT SOLVED{Colors.END}"
            print(f"  Puzzle {puzzle_num}: {status}")
        
        print(f"\n{Colors.YELLOW}Which puzzle would you like to check? (1-6, or 'all' to check all):{Colors.END}")
        choice = input("> ").strip().lower()
        
        if choice == 'all':
            # Check all unsolved puzzles
            for puzzle_num in puzzles:
                if puzzle_num not in solved:
                    print(f"\n{Colors.BOLD}Checking Puzzle {puzzle_num}...{Colors.END}")
                    if check_puzzle(puzzle_num):
                        solved.append(puzzle_num)
                        print(f"{Colors.GREEN}{Colors.BOLD}🎉 Puzzle {puzzle_num} SOLVED! Great work!{Colors.END}")
                    else:
                        print(f"{Colors.YELLOW}💡 Hint: {get_puzzle_hint(puzzle_num)}{Colors.END}")
        elif choice.isdigit() and 1 <= int(choice) <= 6:
            puzzle_num = int(choice)
            print(f"\n{Colors.BOLD}Checking Puzzle {puzzle_num}...{Colors.END}")
            if check_puzzle(puzzle_num):
                if puzzle_num not in solved:
                    solved.append(puzzle_num)
                    print(f"{Colors.GREEN}{Colors.BOLD}🎉 Puzzle {puzzle_num} SOLVED! Great work!{Colors.END}")
            else:
                print(f"{Colors.YELLOW}💡 Hint: {get_puzzle_hint(puzzle_num)}{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid choice! Please enter 1-6 or 'all'.{Colors.END}")
    
    # All puzzles solved!
    escape_code = generate_escape_code()
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}{'='*60}")
    print("   🎉 CONGRATULATIONS! 🎉")
    print(f"{'='*60}{Colors.END}")
    print(f"\n{Colors.CYAN}You've fixed all the bugs and escaped the vault!{Colors.END}")
    print(f"{Colors.YELLOW}Your escape code is: {Colors.BOLD}{escape_code}{Colors.END}")
    print(f"\n{Colors.MAGENTA}You're a true coding champion! 🌟{Colors.END}\n")

if __name__ == "__main__":
    main()


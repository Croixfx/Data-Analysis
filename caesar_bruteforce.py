#!/usr/bin/env python3
"""
Caesar cipher brute-force: try all 26 shifts.
Usage: run the script and paste/enter ciphertext when prompted.
"""

import string

ALPHABET_LOWER = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_UPPER = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = 26

def shift_char(ch: str, shift: int) -> str:
    """Shift a single character by 'shift' positions; preserve case; non-letters unchanged."""
    if ch.islower():
        idx = ALPHABET_LOWER.index(ch)
        return ALPHABET_LOWER[(idx + shift) % N]
    if ch.isupper():
        idx = ALPHABET_UPPER.index(ch)
        return ALPHABET_UPPER[(idx + shift) % N]
    return ch

def caesar_shift(text: str, shift: int) -> str:
    """Apply Caesar shift (positive shift moves letters forward)."""
    return ''.join(shift_char(ch, shift) for ch in text)

def bruteforce_caesar(ciphertext: str):
    """Yield (shift, plaintext) for all 26 shifts (0..25)."""
    for shift in range(N):
        yield shift, caesar_shift(ciphertext, shift)

def main():
    print("=== Caesar cipher brute-force (26 shifts) ===")
    ciphertext = input("Enter ciphertext: ").rstrip("\n")
    print("\nTrying all 26 shifts (shift value = how many positions letters moved forward):\n")
    for shift, plaintext in bruteforce_caesar(ciphertext):
        print(f"Shift {shift:2d}: {plaintext}")
    print("\nTip: look for the candidate that reads like normal English. Shift 0 is the original ciphertext.")

if __name__ == "__main__":
    main()

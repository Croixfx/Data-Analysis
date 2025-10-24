#!/usr/bin/env python3
"""
Caesar cipher frequency analysis decryptor.

Usage: run the script and paste/enter ciphertext when prompted.
It will print candidate plaintexts produced by:
 - mapping most frequent ciphertext letter -> common English letters (E,T,A,...)
 - chi-squared scoring over all 26 shifts (best matches first)

Preserves case and non-letters.
"""

from collections import Counter
import string

# Expected English letter frequencies (A-Z) as percentages (source: typical English frequencies)
ENGLISH_FREQ = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
    'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
    'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
    'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.361, 'X': 0.150, 'Y': 1.974, 'Z': 0.074
}

ALPHABET = string.ascii_uppercase
N = 26

def shift_char(ch: str, shift: int) -> str:
    if ch.islower():
        return chr((ord(ch) - ord('a') + shift) % N + ord('a'))
    if ch.isupper():
        return chr((ord(ch) - ord('A') + shift) % N + ord('A'))
    return ch

def caesar_shift(text: str, shift: int) -> str:
    return ''.join(shift_char(ch, shift) for ch in text)

def count_letters(text: str):
    """Count letters A-Z in uppercase; return Counter and total letters."""
    cleaned = [c.upper() for c in text if c.isalpha()]
    c = Counter(cleaned)
    total = sum(c.values())
    return c, total

def chi_squared_score(text: str) -> float:
    """
    Compute chi-squared statistic of text letter distribution vs English frequencies.
    Lower is better (more like English).
    """
    counts, total = count_letters(text)
    if total == 0:
        return float('inf')  # no letters, not useful
    score = 0.0
    for letter in ALPHABET:
        observed = counts.get(letter, 0)
        expected = ENGLISH_FREQ[letter] * total / 100.0
        # avoid division by zero; expected won't be zero for any letter in our table
        diff = observed - expected
        score += (diff * diff) / (expected if expected > 0 else 1e-9)
    return score

def freq_based_candidates(ciphertext: str, top_n: int = 5):
    """
    Produce candidate plaintexts using two strategies:
      - mapping most frequent ciphertext letter to common English letters
      - ranking all 26 shifts by chi-squared score
    Returns dict with results.
    """
    # 1) Most-frequent-letter mapping guesses
    counts, total = count_letters(ciphertext)
    if total == 0:
        mf_candidates = []
    else:
        most_common = [p[0] for p in counts.most_common()]  # order by freq
        mf_candidates = []
        # candidate target letters in order of typical English frequency
        common_targets = ['E','T','A','O','I','N','S','R','H','L']
        mapped = set()
        for cipher_most in most_common:
            # try mapping this ciphertext letter to each likely plaintext letter (E,T,A,...)
            for target in common_targets:
                if (cipher_most, target) in mapped:
                    continue
                # shift needed: (target - cipher_most) mod 26
                shift = (ord(target) - ord(cipher_most)) % N
                plaintext = caesar_shift(ciphertext, shift)
                mf_candidates.append((cipher_most, target, shift, plaintext))
                mapped.add((cipher_most, target))
            # stop after a few ciphertext frequent letters to avoid explosion
            if len(mf_candidates) >= 20:
                break

    # 2) Chi-squared ranking of all 26 shifts
    shift_scores = []
    for s in range(N):
        candidate = caesar_shift(ciphertext, s)
        score = chi_squared_score(candidate)
        shift_scores.append((s, score, candidate))
    shift_scores.sort(key=lambda x: x[1])  # ascending by chi-sq (best first)

    return {
        'most_freq_guesses': mf_candidates,
        'chi_squared_ranking': shift_scores[:top_n]  # top N shifts
    }

def pretty_print_results(results):
    print("\n--- Most-frequent-letter mapping candidates (top guesses) ---")
    if not results['most_freq_guesses']:
        print("No alphabetic characters found in ciphertext.")
    else:
        for i, (ciph_letter, target, shift, plaintext) in enumerate(results['most_freq_guesses'], start=1):
            print(f"{i:2d}. Map {ciph_letter} -> {target}  (shift {shift:2d})")
            print(f"    {plaintext}")

    print("\n--- Chi-squared best shifts (lowest score = better match to English) ---")
    for i, (shift, score, plaintext) in enumerate(results['chi_squared_ranking'], start=1):
        print(f"{i:2d}. Shift {shift:2d}  chi2={score:.2f}")
        print(f"    {plaintext}")

def main():
    print("=== Caesar frequency-analysis decryptor ===")
    ciphertext = input("Enter ciphertext (paste then Enter):\n> ").rstrip("\n")
    results = freq_based_candidates(ciphertext, top_n=6)
    pretty_print_results(results)

    # Provide the single best-guess (lowest chi2) as a convenience
    best_shift, best_score, best_plain = results['chi_squared_ranking'][0]
    print("\nBest automatic guess (chi-squared):")
    print(f"Shift {best_shift} -> chi2={best_score:.2f}")
    print(best_plain)
    print("\nIf this isn't correct, inspect the other candidates above (sometimes short ciphertexts or non-standard text break frequency assumptions).")

if __name__ == "__main__":
    main()

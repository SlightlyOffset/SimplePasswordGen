'''
Entropy-based Password Strength Estimation
==========================================

This module provides a hybrid method to estimate the strength of a password using:
1. Ideal entropy based on character pool size and password length.
2. Shannon entropy based on actual character distribution in the password.

By comparing both estimates, the more conservative (lower) value is chosen as the final measure.
This helps capture both theoretical strength and real-world randomness.

---------
Author: SlightlyOffset
Version: 1.1.0-alpha (Prototype)
Update: 16 June 2025
---------
'''
from math import log2, pow, floor
from collections import Counter

def ideal_entropy(include, password):
    '''
    Calculate the *ideal* password entropy assuming uniform randomness and
    character pool selection.

    Entropy is calculated using the formula: log2(r^l), where:
        - r = size of the selected character pool
        - l = length of the password

    Args:
        include (list of bool): A 4-element list indicating which character groups
                                were allowed during generation, in the order:
                                [uppercase, lowercase, digits, punctuation]
        password (str): The generated password (only its length is used)

    Returns:
        int: Estimated ideal entropy in bits, rounded down to the nearest whole number
    '''
    r = 0
    l = len(password)
    if include[0]: r += 26      # Uppercase 26 characters
    if include[1]: r += 26      # Lowercase 26 characters
    if include[2]: r += 10      # Digits 10 characters
    if include[3]: r += 32      # Punctuation 32 characters
    return floor(log2(pow(r, l)))

def shannon_entropy(password):
    '''
    Calculate the *actual* Shannon entropy of the password based on character frequency.

    This method evaluates the randomness of the password by analysing how evenly
    distributed the characters are. It penalises repeated or patterned characters.

    Formula: H = -∑(p_i * log2(p_i)), where p_i is the frequency of each character.

    Args:
        password (str): The password to analyse

    Returns:
        int: Shannon entropy (bits), scaled by password length and rounded down to the nearest whole number
    '''
    l = len(password)
    freq = Counter(password)
    entropy = -sum((count / l) * log2(count / l) for count in freq.values())
    return floor(entropy * l)

def translate_to_text(e):
    '''
    Translate a numeric entropy value into a human-readable strength label.

    Categories are based on commonly accepted entropy thresholds:
        < 28      : Very Weak
        28–35     : Weak
        36–59     : Reasonable
        60–127    : Strong
        >= 128    : Very Strong

    Args:
        e (int): Entropy in bits (e.g., from ideal_entropy or shannon_entropy)

    Returns:
        str: Readable strength description
    '''
    strength = ""
    if e < 28:
        strength = "Very Weak"
    elif 28 <= e <= 35:
        strength = "Weak"
    elif 36 <= e <= 59:
        strength = "Reasonable"
    elif 60 <= e <= 127:
        strength = "Strong"
    else: # e >= 128
        strength = "Very Strong"
    return strength

def main(include, password):
    '''
    Main function for evaluating password strength using hybrid entropy estimation.

    This combines:
        - Ideal entropy (pool-based theoretical strength)
        - Shannon entropy (distribution-based actual strength)

    The more conservative (lower) of the two is used for final assessment.

    Args:
        include (list of bool): Indicates inclusion of character pools:
                                [uppercase, lowercase, digits, punctuation]
        password (str): The password to evaluate

    Returns:
        str: Password strength classification (e.g., "Strong", "Weak")
    '''

    ideal_e = ideal_entropy(include, password)
    actual_e = shannon_entropy(password)
    password_strength = translate_to_text(min(ideal_e, actual_e))
    return password_strength


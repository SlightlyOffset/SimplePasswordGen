'''
Entropy-based password strength estimation
==========================================

A helper module to estimate the generated password strength
based on entropy logn(r^l)

---------
Author: SlightlyOffset
Version: 1.0 (Prototype)
---------
'''
from math import log2, pow, floor

def entropy(r, l):
    '''
    Function to calculate the strength of password in bit

    Password entropy is a measure of the unpredictability or randomness of a password,
    expressed in bits. The higher the entropy, the more secure the password is
    against brute-force attacks, as it indicates a greater number of possible combinations
    an attacker would need to guess.
    '''
    return floor(log2(pow(r, l)))

def translate_to_text(e):
    '''
    Function to translate entropy(bit) to text format for easy reading
    Args:
        e: Entropy calculated from entropy(r, l)
    Returns:
        str: password strength
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
    elif e >= 128:
        strength = "Very Strong"
    return strength

def main(include, password):
    '''
    Main entry of the module
    Args:
        include (list): A list of inclusion of characters pool for password generation.
        password (str): Generated password --> For len(password)
    Returns:
        str: Password strength
    '''
    r = 0
    l = len(password)
    if include[0]:    # Uppercase 26 characters
        r += 26
    if include[1]:    # Lowercase 26 characters
        r += 26
    if include[2]:    # Digits 10 characters
        r += 10
    if include[3]:    # Punctuation 32 characters
        r += 32

    entropy_e = entropy(r, l)
    password_strength = translate_to_text(entropy_e)
    return password_strength


---

# SimplePasswordGen

A simple terminal-based password generator that allows the user to select which character types to include (uppercase, lowercase, numbers, punctuation) and generates a random password based on those preferences.

---

## 🔼 Update:
- 16 June 2025: Minor update on condition checking on `SimplePasswordGen.py`
- 16 June 2025: Update on entropy calculation. Switching from pool-based entropy(Ideal entropy) to hybrid-entropy(Ideal entropy + Shannon entropy)
- 15 June 2025: Minor update on input validation(mainly reduce redundancy)
- 13 June 2025: Implemented Shannon entropy for password strength estimation log2(r^l) (prototype - still assumes even distribution of characters) 

---

## 📌 Features

- Interactive CLI menu
- User input validation
- Customisable character pool
- Error handling for invalid inputs and empty character pools
- Formatted terminal output for enhanced readability
- Password strength estimation using hybrid-entropy

---

## 🧠 How It Works

The program asks the user:

1. Whether to begin the password generation process.
2. Desired password length.
3. Whether to include:
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Punctuation symbols

If all character types are deselected, the program warns the user before proceeding.

---

## 🛠 Functions Overview

### `genpass(length, include)`
Generates a password using the selected options.

**Parameters:**
- `length (int)`: Password length
- `include (list[bool])`: List of `True` or `False` for each character type

**Returns:**  
- A randomly generated password (printed, not returned)
- Estimated password strength

---

### `get_valid_yes_no(prompt)`
Prompts the user for 'y' or 'n' input with validation.

**Parameter:**  
- `prompt (str)`: Message to display

**Returns:**  
- `bool`: True for yes (y/Enter), False for no (n)

---

### `get_valid_length(prompt)`
Prompts the user to enter a positive integer for password length.

**Parameter:**  
- `prompt (str)`: Message to display

**Returns:**  
- `int`: Validated positive integer

---

### `menu()`
Main menu loop that handles all user interactions and triggers password generation.

---

## 🧪 Example Usage

```
--- Password Generator ---

Begin? (Y/n): y

Password length is recommended to be 8 characters long or more.
Password length: 12

Include uppercase letters?(Y/n): y
Include lowercase letters?(Y/n): y
Include number?(Y/n): y
Include punctuation?(Y/n): n

 -----------------------------
| Random pool will include:   |
| Uppercase Characters: yes   |
| Lowercase Characters: yes   |
| Number Characters: yes      |
| Punctuation Characters: no  |
 -----------------------------

 -----------------------
|  Password length: 12  |
 -----------------------

Continue with selected options? (Y/n): y

--- Password Generated ---

 -------------------------- 
|  Password: AbC1xY7eZwQ9  |
 --------------------------

 ------------------------------ 
|  Estimated strength: Strong  |
 ------------------------------
 
NOTE: The strength estimation did not reflect the real world strength against attacking attempts.
       User still need to practice cautions while using the password.
NOTE: All passwords generated should not be saved locally without encryption such as .txt or .csv.
```

---

## 📦 Dependencies

- `secrets` (Standard library)
- `string` (Standard library)
- `math` (Standard library) --> for strength estimation in `entropy.py`
- `collections` (Standard library) --> for strength estimation in `entropy.py`

---

## 🧩 Future Enhancements

- **Password saving functionality**  
  Option to export generated passwords to `.txt` or `.csv` for backup.  
  ⚠️ _Note: Storing passwords in plain text is **not recommended** unless encrypted._

- **CLI Argument Support**  
  Allow password generation via command-line arguments for automation/scripting.

- **Password Strength Estimation(Ongoing)**  
  Provide feedback on password strength based on selected options and length.

- **Clipboard Copy Option**  
  Auto-copy the generated password to the clipboard using `pyperclip`.

- **GUI Version**  
  Extend the tool with a basic Tkinter or PyQt interface for users who prefer graphical applications.

- **History and Logging (Optional)**  
  Maintain a session log (in-memory or encrypted file) of recent passwords generated for reference.

---

## 🧑‍💻 Author

**SlightlyOffset**
**(Thitiwat Monwiset | ID: 68070035)**
Version: 1.1.1-beta
Update: 15 June 2025
---
This project is now part of the PSCP (Problem-Solving and Computer Programming) course
at King Mongkut's Institute of Technology Ladkrabang (KMITL).
---
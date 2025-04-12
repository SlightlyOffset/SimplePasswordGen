---

# SimplePasswordGen

A simple terminal-based password generator that allows the user to select which character types to include (uppercase, lowercase, numbers, punctuation) and generates a random password based on those preferences.

---

## 📌 Features

- Interactive CLI menu
- User input validation
- Customizable character pool
- Error handling for invalid inputs and empty character pools
- Formatted terminal output for enhanced readability

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
- `include (list[str])`: List of 'y' or 'n' for each character type

**Returns:**  
A randomly generated password (printed, not returned)

---

### `get_valid_yes_no(prompt)`
Prompts the user for 'y' or 'n' input with validation.

**Parameter:**  
- `prompt (str)`: Message to display

**Returns:**  
- `str`: Validated lowercase 'y' or 'n'

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

 ------------------------------
| Random pool will include:   |
| Uppercase Characters: yes   |
| Lowercase Characters: yes   |
| Number Characters: yes      |
| Punctuation Characters: no  |
 ------------------------------

 ------------------------ 
|  Password length: 12  |
 ------------------------

Continue with selected options? (Y/n): y

--- Password Generated ---

 ------------------------ 
|  Password: AbC1xY7eZwQ9  |
 ------------------------

All passwords generated should not be saved locally without encryption such as .txt or .csv.
```

---

## 📦 Dependencies

- `secrets` (Standard library)
- `string` (Standard library)

---

## 🧩 Future Enhancements

- **Password saving functionality**  
  Option to export generated passwords to `.txt` or `.csv` for backup.  
  ⚠️ _Note: Storing passwords in plain text is **not recommended** unless encrypted._

- **CLI Argument Support**  
  Allow password generation via command-line arguments for automation/scripting.

- **Password Strength Estimation**  
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
Version: 1.0

---

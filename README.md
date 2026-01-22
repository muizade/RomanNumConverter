# Roman Numeral Converter

A robust Python script that performs bidirectional conversion between Arabic integers and Roman numerals. It includes a command-line interface (CLI) for easy interaction and strict validation logic.

## 📋 Features

* **Integer to Roman:** Converts integers from **1 to 3999** into standard Roman numerals.
* **Roman to Integer:** Converts Roman numeral strings into integers.
* **Strict Validation:** checks for invalid characters and ensures the Roman numeral follows standard rules (e.g., rejects "IIII" in favor of "IV") by utilizing a "round-trip" conversion check.
* **Interactive Menu:** Simple CLI loop allowing multiple conversions without restarting the script.

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your machine.

### Installation

1.  Save the script logic into a file named `roman_converter.py`.
2.  Ensure this README is in the same directory (optional).

## 💻 Usage

Run the script using your terminal or command prompt:

```bash
python roman_converter.py

Interactive Mode
Once running, follow the on-screen prompts:
1: Integer to Roman
2: Roman to Integer
3: Exit
Choose mode: 1
Enter integer (1-3999): 1994
MCMXCIV

⚙️ Function Documentation
int_to_roman(num)
 * Input: Integer (1–3999).
 * Logic: Uses a greedy algorithm with a mapping of values to subtract the largest possible Roman values first.
 * Error Handling: Raises ValueError if the number is out of the supported range.
roman_to_int(s)
 * Input: Roman numeral string (case-insensitive).
 * Logic: Iterates through the string in reverse. If a value is less than the previous value (e.g., I before V), it subtracts; otherwise, it adds.
 * Error Handling: Raises ValueError for unknown characters.
is_valid_roman(s)
 * Logic: 1. Checks if characters belong to {I, V, X, L, C, D, M}.
   2. Performs a round-trip check: converts the Roman string to an integer, then converts that integer back to Roman. If the result doesn't match the original input, the Roman numeral is considered invalid (non-standard).
📝 Example Cases
| Input Type | Input Value | Result / Output |
|---|---|---|
| Integer | 3 | III |
| Integer | 4 | IV |
| Integer | 1994 | MCMXCIV |
| Roman | X | 10 |
| Roman | IX | 9 |
| Roman | IIII | Invalid Roman numeral |

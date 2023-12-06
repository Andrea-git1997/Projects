# License Plate Validator

This simple Python script checks the validity of a license plate input based on specified conditions. It includes checks for the length of the plate, the first two characters being letters, the absence of certain special characters, and the presence of a valid numeric pattern.

## How to Use

1. Run the script.
2. Enter the license plate when prompted.
3. The script will display whether the license plate is valid or invalid.

## Conditions for Validation

- The length of the license plate must be between 2 and 6 characters.
- The first two characters of the license plate must be letters.
- The license plate must not contain certain special characters, including space, period, comma, colon, and semicolon.
- The first numeric character in the license plate cannot be "0".
- The remaining characters after the first numeric character must be digits.

## Implementation

The `main` function handles user input and calls the `is_valid` function to check the validity of the license plate. The `is_valid` function performs the specified conditions and uses the `number` function to check for the presence of numeric characters.

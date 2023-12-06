Coin Change Program
Overview:
This Python script simulates a simple coin change program where the user is prompted to insert coins to meet a specified amount due. The program continuously requests coins until the total amount due is satisfied or exceeded.

How to Use:
Run the script by executing the Python file:

bash

python coin_change_program.py
Enter coins when prompted. The program accepts coins in denominations of 5, 10, and 25.

The program calculates the remaining amount due and asks for additional coins until the amount is fully paid or exceeded.

The script displays the final amount due or change owed.

Code Explanation:
main() Function:
Initialization:

amount: Initial amount due (set to 50 in this example).
Display the initial amount due.
Coin Input:

Prompt the user to insert coins.
Call check_input to validate coin denominations.
Convert the validated coin input to an integer.
Coin Change Loop:

Initialize i to track the loop iterations.
Enter a loop while the amount due is not zero.
If it's the first iteration (i == 0), perform the initial calculation and update the amount due.
If it's not the first iteration (i >= 1), perform subsequent calculations based on user input.
Check for the end condition when the amount due is zero or negative.
check_input(amount, insert_coin) Function:
Input Validation Loop:
Enter a loop until the user inserts a valid coin denomination (5, 10, or 25).
Display the current amount due if an invalid coin is entered.
Return the valid coin input.
Example:
python

# Run the script
python coin_change_program.py
python
Copy code
# Example Output:

Amount Due: 50
Insert Coin: 10
Amount Due: 40
Insert Coin: 20
Amount Due: 40
Insert Coin: 25
Amount Due: 15
Insert Coin: 10
Amount Due: 5
Insert Coin: 5
Change Owed: 0
This example demonstrates a user inserting coins to meet the amount due, with the program correctly handling the change owed or displaying the final amount due.

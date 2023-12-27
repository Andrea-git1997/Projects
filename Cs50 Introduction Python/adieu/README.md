# Farewell Message Generator

## Overview

This script generates a farewell message based on a list of names provided by the user. It uses the Inflect library to pluralize the names and create a farewell message. The generated message bids farewell to the individuals in the list.

## Usage

### Prerequisites

Make sure you have Python installed on your system.

### Running the Script

1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run the script:

   python farewell_generator.py
Follow the prompts to enter names. Press [Ctrl+d] to exit and generate the farewell message.
Features
The script uses the Inflect library to pluralize names.
Names are collected in a list until the user exits the input loop.
The farewell message is generated based on the number of names entered.
Example


Name: John
['John']
Name: Mary
['John', 'Mary']
Name: Alice
['John', 'Mary', 'Alice']
^D
Adieu, adieu, to John, Mary, and Alice
Dependencies
Inflect: Used for pluralizing names.
Notes
The script can handle up to 8 names in the farewell message.
Customize the farewell message as needed.

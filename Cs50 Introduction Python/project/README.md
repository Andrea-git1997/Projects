# Titanic Data Analysis with Pandas

## Video Demo
[Watch the Video Demo](https://youtu.be/kH5adiBk2bU)

## Description

### Installation of Libraries
- Import `sys` for accepting arguments in terminal: `aviation python project.py`
- Install Pandas: `pip install pandas`
- Import Pandas for data analysis of the Titanic dataset.
- Import Matplotlib for constructing plots: `import matplotlib.pylab as plt`
- Import PyFiglet for formatting the program title.

### Introduction
1. To start the program, navigate to the project folder in the terminal (`cd project`).
2. Run the program: `project/ $ python project.py`
3. Compare the title of the program, 'Analysis of Titanic Disaster,' formatted as ASCII using PyFiglet.
4. Enter the login file (e.g., your name). Non-numerical inputs are accepted.

### Program Flow
- After the welcome message (`Welcome {login}`), the program asks if you're ready to analyze Titanic data frame: `Are you ready to analyze Titanic data frame? (Y/N)`
  1. If 'y' (input has `strip()` and `lower()`), the process continues.
  2. If 'n' (input has `strip()` and `lower()`), the process stops via `sys.exit()`.

### Cleaning Operations
- The program asks if you want to clean the data frame: `Do you want to clean the data frame? (Y/N)`
  1. If 'y,' the program shows the initial and final number of rows and columns and eliminates null rows using `dropna(inplace=True)`.
  2. If 'n,' the cleaning code is skipped.

### Choice Path
- Users choose 'R' for Read modality or 'A' for Analysis modality.

### Analysis Modality
1. **Read Modality (R):**
   - Users choose the number of rows to display (e.g., 10), and the program shows the first ten rows using `head(n)`.

2. **Analysis Modality (A):**
   - Users can choose from 5 different paths:
     - A1) See general statistical parameters.
     - A2) Reduce the data frame.
     - A3) Survived and not survived analysis.
     - A4) Interesting plots.
     - A5) Query about the Embarked.

3. **General Statistics (A1):**
   - The program asks if users want to include 'object' type in general statistics (Y/N) and shows the statistics using `.describe()`.

4. **Reduce Data Frame (A2):**
   - Users can create a new data frame with selected columns and add lines of code to work with the new data frame.

5. **Survived Analysis (A3):**
   - Users choose to analyze survived or not survived (S/SN). The program generates a summary dictionary for both cases.

6. **Plots (A4):**
   - If 'a4' is chosen, the program saves three different plots in the current folder.

7. **Embarked Analysis (A5):**
   - If 'a5' is chosen, the program creates a histogram to visualize the number of passengers embarked in different cities.

### File Test
- Tests 2 functions for simplicity. Other functions give plots or require input inside the functions.


# User Input Python Script

This Python script demonstrates how to take user inputs for various attributes, display them in different formats, and print their data types.

## Overview

The script performs the following tasks:
1. Takes user inputs for name, age, height, and gender.
2. Outputs each input on a separate line.
3. Prints all inputs on a single line.
4. Displays the data types of each input.

## Code

```python
# Take user inputs
name = input("Enter your Name:")
age = int(input("Enter your Age:"))
height = float(input("Enter your Height:"))
gender = bool(int(input("Enter your Gender Male (1) or Female (0):")))

# Output each in line User Inputs
print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("Gender: ", gender)

# Print in one line
print("Name: ", name, end=", ")
print("Age: ", age, end=", ")
print("Height: ", height, end=", ")
print("Gender: ", gender)

# Output User Inputs
print("Name Type: ", type(name))
print("Age Type: ", type(age))
print("Height Type: ", type(height))
print("Gender Type: ", type(gender))
```
## Output
#### After running the script, you will see:

- **Each input value printed on a new line.**
- **All input values printed on a single line separated by commas.**
- **The data type of each input value.**

## Example
```
Enter your Name: John
Enter your Age: 30
Enter your Height: 5.9
Enter your Gender Male (1) or Female (0): 1
Name:  John
Age:  30
Height:  5.9
Gender:  True
Name:  John, Age:  30, Height:  5.9, Gender:  True
Name Type:  <class 'str'>
Age Type:  <class 'int'>
Height Type:  <class 'float'>
Gender Type:  <class 'bool'>
```

### Key Sections:
- **Overview**: Summarizes what the script does.
- **Code**: Includes the full script.   
- **Output**: Describes what to expect when running the script.
- **Example**: Provides a sample run to illustrate how the script works.

Adjust the content as necessary to better fit your project or add any additional information you find useful!

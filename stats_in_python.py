import sys # Importing system to stop the program when an invalid column is selected
import math # Importing math for math operations

def load_data(filepath:str, column:int)->tuple[list, int]: # Function to load numeric data from file
    numbers = [] # List will store valid numeric values
    count = 0 # Counts total rows in file
    with open(filepath,'r') as infile: # Open file for reading
        for line in infile: # Read one line at a time
            count += 1 # Increment row count
            columns = line.split("\t") # Used to split the row into separate columns
            try:
                value = columns[column] # Get the value from the selected column index
            except IndexError: 
                print(f"Exiting: There is no valid 'list index' in {column} in file: {filepath}")
                sys.exit() # It will exit the program if column is invalid
            try: 
                 number = float(value) # It converts column value to a float
                 if math.isnan(number): # Check if the number is NaN
                    pass # Ignore NaN values 
                 else: # Execute when the value is valid number
                    numbers.append(number) # Stores valid numeric values
            except ValueError: # Handle conversion errors
                pass # Ignore non-numeric values
    if len(numbers) == 0: # If column contains no valid numbers
        print(f"Error: There were no valid number(s) in column {column} in file: {filepath}") # Prints the error message for invalid input
        sys.exit() # Exit the program

    return numbers,count # Return the list of valid numbers and total row count

def calculate_average(numbers:list)->float: # Calculate the average
    average = sum(numbers) / len(numbers) # Divide total by the number of values
    return average # Return the average

def get_max_and_min(numbers:list)->tuple[float, float]: # Finds maximum and minimum values
    maximum_number = max(numbers) # Get the largest number
    minimum_number = min(numbers) # Get the smallest number
    return maximum_number,minimum_number # Return the maximum and minimum values


def calculate_variance(numbers:list)->float: # Calculate the variance

    if len(numbers) <= 1: # Check if the list contains one or fewer elements
        return 0.0 # Variance of one value is zero
    
    average = calculate_average(numbers) # Calculate mean
    total = 0 # Store the sum of squared differences
    for n in numbers: # Loop through each number
        squared_difference = (n - average)**2 # Calculate squared difference from mean
        total += squared_difference # Add squared difference to total

    variance = 1/(len(numbers) - 1) * total # Calculate variance using formula
    return variance # Return variance



def calculate_std_dev(numbers:list)->float: # Calculate standard deviation
    standard_deviation = math.sqrt(calculate_variance(numbers)) # Calculate the square root of variance
    return standard_deviation # Return standard deviation

def calculate_median(number:list)->float: # Calculate the median value
    sorted_numbers = sorted(number) # Sort numbers in ascending order
    length = len(sorted_numbers) # Calculate the length of list
    if length % 2 == 0: # Check if count is even
        middle_number_1 = sorted_numbers[length//2-1] # First middle value
        middle_number_2 = sorted_numbers[length//2] # Second middle value
        median = (middle_number_1 + middle_number_2)/2 # Average of middle values
    else: # Handle the odd number of values
        median = float(sorted_numbers[length//2]) # Get middle value

    return median # Return median




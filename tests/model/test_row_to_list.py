import csv
import os
from src.model.row_2_list2 import row_to_list  # Adjust the import path if needed
import pytest

# Define the path to the CSV file relative to the current working directory
data_path = os.path.join('data', 'house_price.csv')

# Load your dataset from the CSV file
dataset = []
with open(data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

# Test function for handling missing values
@pytest.mark.parametrize("input_row", dataset)
def test_row_to_list_with_missing_values(input_row):
    input_string = ' '.join(input_row)
    has_missing_values = any(value == '' for value in input_row)
    if has_missing_values:
        assert row_to_list(input_string) is None
    else:
        assert row_to_list(input_string) is not None

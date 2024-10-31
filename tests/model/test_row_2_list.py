import pytest
from src.model.row_2_list import row_to_list

# Test for a properly formatted string with a tab and newline
def test_for_clean_row():
    assert row_to_list("2,081\t314,942\n") == ["2,081", "314,942"]

# Test for a string missing one of the two required parts (e.g., area missing)
def test_for_missing_area():
    assert row_to_list("\t293,410\n") is None

# Test for a string missing the tab character
def test_for_missing_tab():
    assert row_to_list("1,463238,765\n") is None

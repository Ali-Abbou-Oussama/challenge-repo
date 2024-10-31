from textblob import TextBlob
import pytest
from src.model.sentiment import extract_sentiment
import pandas as pd

# Load text data from CSV
soccer_data_path = 'data/soccer_sentiment_analysis.csv'
soccer_sentiments = pd.read_csv(soccer_data_path)

# Extract the 'Text' column as a list for testing
testdata = soccer_sentiments['Text'].tolist()  # Use 'Text' to match the CSV column name

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)
    # Check for negative sentiments based on specific keywords in the text
    if "disappointing" in sample or "heartbreaking" in sample:
        assert sentiment <= 0  # Expect negative sentiment
    # Check for positive sentiments based on specific keywords in the text
    elif "brilliant" in sample or "phenomenal" in sample:
        assert sentiment > 0  # Expect positive sentiment
    else:
        assert True  # If sentiment is neutral or doesn't fit specific criteria, we can pass

@pytest.mark.parametrize('sample', [
    "Barcelona played brilliantly last Wednesday. Rafinia’s hat-trick was pure magic. Visca Barça!"
])
def test_positive_sentiment(sample):
    pos_sentiment = extract_sentiment(sample)
    assert pos_sentiment > 0  # We expect a positive sentiment

import re
from textblob import TextBlob

# Get the file name directly from the user
file_name = input("Enter the name of the text file (with .txt extension) in the same folder: ")

try:
    # Read the file
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    
    print("\nOriginal Text Preview:")
    print(text[:500] + '...' if len(text) > 500 else text)  # Show the first 500 characters
    
    # Clean the text
    def clean_text(text):
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs and email addresses
        text = re.sub(r"http\S+|www\S+|https\S+", '', text)
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        
        # Remove extra whitespaces
        text = " ".join(text.split())
        
        return text

    cleaned_text = clean_text(text)

    print("\nCleaned Text Preview:")
    print(cleaned_text[:500] + '...' if len(cleaned_text) > 500 else cleaned_text)

    # Perform sentiment analysis
    blob = TextBlob(cleaned_text)
    polarity = blob.sentiment.polarity  # Sentiment polarity (-1 to 1)
    subjectivity = blob.sentiment.subjectivity  # Subjectivity (0 to 1)

    print("\nSentiment Analysis:")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    
    # Rank based on polarity
    if polarity > 0.5:
        rank = "Highly Positive"
    elif 0 < polarity <= 0.5:
        rank = "Positive"
    elif polarity == 0:
        rank = "Neutral"
    elif -0.5 <= polarity < 0:
        rank = "Negative"
    else:
        rank = "Highly Negative"

    print(f"\nSentiment Rank: {rank}")

except FileNotFoundError:
    print("Error: File not found. Please ensure the file exists in the same folder and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

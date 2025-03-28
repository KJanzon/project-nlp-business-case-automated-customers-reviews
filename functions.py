import pandas as pd


# Define function to load and clean each dataset
def load_and_clean(file_path):
    cols = [
        "id",
        "name",
        "brand",
        "reviews.text",
        "reviews.title",
        "reviews.rating",
        "categories",
        "primaryCategories"
    ]
    
    df = pd.read_csv(file_path, usecols=cols)
    
    # Drop nulls
    df = df.dropna(subset=["reviews.text", "reviews.rating"])

    # Map ratings to sentiment
    def map_sentiment(rating):
        if rating <= 3:
            return "negative"
        else:
            return "positive"
        
    df["sentiment"] = df["reviews.rating"].apply(map_sentiment)

    # Drop exact duplicates if any
    df = df.drop_duplicates(subset=["id", "reviews.text"])

    return df
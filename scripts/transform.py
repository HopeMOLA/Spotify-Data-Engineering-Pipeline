import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/spotify_data.csv")

# Remove duplicates
df = df.drop_duplicates(subset=["song","artist"])

# Clean text
df['song'] = df['song'].str.strip()
df['artist'] = df['artist'].str.title()

# Convert popularity to numeric
df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')

# Drop missing values
df = df.dropna()

# Save processed dataset
df.to_csv("data/processed/clean_spotify_data.csv", index=False)

print("Transformation completed successfully")

import pandas as pd
import pyodbc

df = pd.read_csv("data/processed/clean_spotify_data.csv")

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-538HCGH\\SQLEXPRESS;"
    "DATABASE=SpotifyDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for index,row in df.iterrows():
    cursor.execute("""
        INSERT INTO spotify_tracks (song, artist, popularity)
        VALUES (?, ?, ?)
    """, row.song, row.artist, row.popularity)

conn.commit()

print("Data loaded successfully")

import pandas as pd
import requests
from datetime import datetime

def fetch_data():
    """Fetches sample data to simulate a data source."""
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        return pd.DataFrame(response.json())
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def mask_sensitive_data(df):
    """Outstanding Factor: Demonstrates Data Privacy/Security."""
    if df is not None:
        # Masking email for privacy: 'johndoe@email.com' -> 'joh****@email.com'
        df['email'] = df['email'].apply(lambda x: x[:3] + "****" + x[x.find('@'):])
        # Masking geo-coordinates
        df['address'] = "REDACTED"
    return df

if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting Secure Pipeline...")
    raw_data = fetch_data()
    secure_data = mask_sensitive_data(raw_data)
    
    if secure_data is not None:
        # In a real scenario, we'd save to an S3 bucket or Database
        print(secure_data[['name', 'email']].head())
        print("\n[SUCCESS] Data masked and ready for secure storage.")

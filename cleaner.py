import pandas as pd

def clean_csv(file_path):
    df = pd.read_csv(file_path,sep='|')
    # Clean column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    # Replace empty strings or spaces with NaN
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    # Drop rows with any NaN values
    df = df.dropna()
    # Drop duplicates
    df = df.drop_duplicates()
    # Save cleaned data
    cleaned_path = "clean" + file_path
    df.to_csv(cleaned_path, index=False,sep='|')
    print(f"Cleaned data saved to {cleaned_path}")

if __name__ == "__main__":
    clean_csv("sample.csv")
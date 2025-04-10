
import pandas as pd
def clean_csv(file_path):
    df=pd.read_csv(file_path)
    print(df)
    df.columns = [col.strip().lower().replace('','_') for col in df.columns]
    df=df.dropna(how='all')
    df=df.fillna("NA")
    cleaned_path = "clean" +file_path
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned data saved to {cleaned_path}")


if __name__ == "__main__":
    clean_csv("sample.csv")
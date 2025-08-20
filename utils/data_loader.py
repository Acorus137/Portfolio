import pandas as pd

def load_mls_data():
    df = pd.read_csv("Porfolio/assets/MLS_Standings_1996-2025.csv")
    df = df[df["Year"] < 2025]
    df.dropna(inplace=True)
    df.drop(columns=["Home", "Away", "Unnamed: 0"], inplace=True)
    return df

def load_student_data():
    return pd.read_csv("Porfolio/assets/student_habits_performance.csv")
import pandas as pd


def calculate_revenue(df, column, value):
    return df.loc[df[column] == value, "revenue"].sum()


def get_city_revenue(df):
    cities = df["city"].dropna().unique()

    return pd.DataFrame([
        {
            "city": city,
            "total_revenue": calculate_revenue(df, "city", city)
        }
        for city in cities
    ])


def get_top_3_cities(df):
    return get_city_revenue(df).sort_values(
        "total_revenue", ascending=False
    ).head(3)
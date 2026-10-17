import pandas as pd




def calculate_revenue(df, column, value):
    return df.loc[df[column] == value, "revenue"].sum()


def get_revenue_by_group(df, column):
    values = df[column].dropna().unique()

    return pd.DataFrame([
        {
            column: value,
            "total_revenue": calculate_revenue(df, column, value)
        }
        for value in values
    ])


def get_top_3_cities(df):
    return get_revenue_by_group(df, "city").sort_values(
        "total_revenue", ascending=False
    ).head(3)


def get_top_3_categories(df):
    return get_revenue_by_group(df, "category").sort_values(
        "total_revenue", ascending=False
    ).head(3)

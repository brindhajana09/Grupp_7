import csv

import pandas as pd

import io_utils
from ecommerce import CategorySales, CitySales


def calculate_aov(df: pd.DataFrame) -> float:
    return round(df["revenue"].sum() / len(df.index), 2)
    

def calculate_aov_by_month():
    aov_by_month = {
        "January": 0.0,
        "February": 0.0,
        "March": 0.0,
        "April": 0.0,
        "May": 0.0,
        "June": 0.0,
    }
    monthly_orders = number_of_orders_by_month()
    monthly_revenue = calc_total_revenue_by_month()
    for month in monthly_revenue:
        aov_by_month[month] = round(
            monthly_revenue[month] / monthly_orders[month], 2)

    return aov_by_month


def calc_total_revenue(df: pd.DataFrame) -> float:
    return round(df["revenue"].sum(), 2)


def calc_total_revenue_by_month():
    revenue_by_month = {
        "January": 0.0,
        "February": 0.0,
        "March": 0.0,
        "April": 0.0,
        "May": 0.0,
        "June": 0.0,  # finns ingen data i ecommerce_sales för månader efter Juni
    }

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            month = io_utils.convert_number_to_month(
                int(row["date"].split("-")[1].lstrip("0")))
            revenue_by_month[month] += float(row["revenue"])

    return {
        month: round(float(revenue), 2) # avrundar bort floating point errors
        for month, revenue in revenue_by_month.items()
    }


def calculate_revenue(df: pd.DataFrame, column: str, value):
    return df.loc[df[column] == value, "revenue"].sum()


def get_revenue_by_group(df: pd.DataFrame, column: str):
    values = df[column].dropna().unique()

    return pd.DataFrame([
        {
            column: value,
            "total_revenue": calculate_revenue(df, column, value)
        }
        for value in values
    ])


def get_sales_by_category(df: pd.DataFrame):
    category_dict: dict[str, CategorySales] = {}

    for category in df["category"].dropna().unique():
        category_dict[category] = CategorySales(category)

        for i, row in df.loc[df["category"] == category].iterrows():
            category_dict[row["category"]].add_entry(
                row["date"], int(row["units"]), float(row["revenue"]))

    return list(category_dict.values())


def get_sales_by_city(df: pd.DataFrame):
    city_sales: dict[str, CitySales] = {}

    for city in df["city"].dropna().unique():
        city_sales[city] = CitySales(city)

        for i, row in df.loc[df["city"] == city].iterrows():
            city_sales[city].add_entry(
                row["category"],
                row["date"],
                int(row["units"]),
                float(row["revenue"])
            )
        
    return list(city_sales.values())


def get_top_3_cities(df):
    return get_revenue_by_group(df, "city").sort_values(
        "total_revenue", ascending=False
    ).head(3)


def get_top_3_categories(df):
    return get_revenue_by_group(df, "category").sort_values(
        "total_revenue", ascending=False
    ).head(3)


def number_of_orders_by_month():
    orders_by_month = {
        "January": 0,
        "February": 0,
        "March": 0,
        "April": 0,
        "May": 0,
        "June": 0,
    }

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            month = io_utils.convert_number_to_month(int(
                    row["date"].split("-")[1].lstrip("0")))
            orders_by_month[month] += 1

    return orders_by_month

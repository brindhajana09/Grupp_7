import csv

import pandas as pd

import io_utils
from ecommerce import CategorySales


def calc_total_sales_by_month():
    sales_by_month = {
        "Januari": 0,
        "Februari": 0,
        "Mars": 0,
        "April": 0,
        "Maj": 0,
        "Juni": 0,  # finns ingen data i ecommerce_sales för månader efter Juni
    }

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            month = io_utils.convert_number_to_month(int(
                row["date"].split("-")[1].lstrip("0")))
            sales_by_month[month] += int(row["units"])

    return sales_by_month


def calc_total_revenue_by_month():
    revenue_by_month = {
        "Januari": 0.0,
        "Februari": 0.0,
        "Mars": 0.0,
        "April": 0.0,
        "Maj": 0.0,
        "Juni": 0.0,  # finns ingen data i ecommerce_sales för månader efter Juni
    }

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            month = io_utils.convert_number_to_month(int(
                row["date"].split("-")[1].lstrip("0")))
            revenue_by_month[month] += float(row["revenue"])

    for month, revenue in revenue_by_month.items(): 
        revenue_by_month[month] = round(revenue, 2) # vi såg ut att få floating point errors, jag avrundar bort dem

    return revenue_by_month


def calculate_sales_by_category_over_time():
    category_dict: dict[str, CategorySales] = {}

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            category = row["category"]
            if category not in category_dict:
                category_dict[category] = CategorySales(category)
            category_dict[category].add_entry(
                row["date"], int(row["units"]), float(row["revenue"]))

    category_list = list(category_dict.values())

    return category_list


def calculate_revenue(df: pd.DataFrame, column, value):
    return df.loc[df[column] == value, "revenue"].sum()


def get_revenue_by_group(df: pd.DataFrame, column):
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

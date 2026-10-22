import csv

import pandas as pd

import io_utils
from ecommerce import CategorySales, CitySales


def calculate_aov():
    total_revenue = 0.0
    monthly_revenue = calc_total_revenue_by_month()
    for month in monthly_revenue:
        total_revenue += monthly_revenue[month]

    return round(total_revenue / number_of_total_orders(), 2)


def calculate_aov_by_category():
    aov_by_category: dict[str, float] = {}
    category_orders: dict[str, int] = {}

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            category = row["category"]
            if category not in aov_by_category:
                aov_by_category[category] = float(row["revenue"])
                category_orders[category] = 1
            else:
                aov_by_category[category] += float(row["revenue"])
                category_orders[category] += 1

    for category, revenue in aov_by_category.items():
        aov_by_category[category] = round(
            revenue / category_orders[category], 2)

    return aov_by_category
    

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


def calculate_aov_by_category_per_city():
    city_sales: dict[str, CitySales] = {}

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            city = row["city"]
            category = row["category"]
            if city not in city_sales:
                city_sales[city] = CitySales(city)
            if category not in city_sales[city].category_sales:
                city_sales[city].category_sales[category] = CategorySales(category)
            city_sales[city].category_sales[category].add_entry(
                row["date"], int(row["units"]), float(row["revenue"]))

    return list(city_sales.values())


def calc_total_revenue():
    revenue = 0.0
    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            revenue += float(row["revenue"])

    return round(revenue, 2)


def calc_total_sales_by_month():
    sales_by_month = {
        "January": 0,
        "February": 0,
        "March": 0,
        "April": 0,
        "May": 0,
        "June": 0,  # finns ingen data i ecommerce_sales för månader efter Juni
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

    return list(category_dict.values())


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


def number_of_total_orders():
    rows_in_data = 0

    with open("../data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.DictReader(data)
        for row in reader:
            rows_in_data += 1

    return rows_in_data


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

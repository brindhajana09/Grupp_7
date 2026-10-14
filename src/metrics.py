import csv

import io_utils


def calc_sales_by_month():
    sales_by_month = {
        "Januari": 0,
        "Februari": 0,
        "Mars": 0,
        "April": 0,
        "Maj": 0,
        "Juni": 0,  # finns ingen data i ecommerce_sales för månader efter Juni
    }

    with open("data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.reader(data)
        next(reader)
        for row in reader:
            month = io_utils.convert_number_to_month(int(
                row[1].split("-")[1].lstrip("0")))
            sales_by_month[month] += int(row[5])

    return sales_by_month


def calc_revenue_by_month():
    revenue_by_month = {
        "Januari": 0,
        "Februari": 0,
        "Mars": 0,
        "April": 0,
        "Maj": 0,
        "Juni": 0,  # finns ingen data i ecommerce_sales för månader efter Juni
    }

    with open("data/ecommerce_sales.csv", encoding="utf-8") as data:
        reader = csv.reader(data)
        next(reader)
        for row in reader:
            month = io_utils.convert_number_to_month(int(
                row[1].split("-")[1].lstrip("0")))
            revenue_by_month[month] += float(row[6])

    for month, revenue in revenue_by_month.items(): 
        revenue_by_month[month] = round(revenue, 2) # vi såg ut att få floating point errors, jag avrundar bort dem

    return revenue_by_month
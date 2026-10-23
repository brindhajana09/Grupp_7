import matplotlib.pyplot as plt
import pandas as pd

from ecommerce import CategorySales, CitySales


def plot_aov_by_city_and_category(city_sales: list[CitySales]):
    city_names = []
    categories: dict[str, list[float]] = {}
    for city in city_sales:
        city_names.append(city.city_name)
        for category in city.category_sales.values():
            if category.category_name not in categories:
                categories[category.category_name] = []
            categories[category.category_name].append(category.calc_aov())

    plt.grouped_bar(categories, tick_labels=city_names, group_spacing=1) # type: ignore

    plt.ylabel("Average Order Value")
    plt.title("AOV by Category in City")
    plt.legend(ncols=4)
    plt.ylim(0, 3000)
    plt.show()

def plot_revenue_by_category_over_time(categories: list[CategorySales]):
    x = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]
    for category in categories:
        y = [category.january_revenue, category.february_revenue,
             category.march_revenue, category.april_revenue,
             category.may_revenue, category.june_revenue]
        plt.plot(x, y, label = category.category_name)
    plt.title("Revenue by Month")
    plt.xlabel("2024")
    plt.ylabel("Revenue")
    plt.legend()
    plt.show()


def plot_revenue_by_category(
    df: pd.DataFrame,
    category_column,
    revenue_column="revenue",
    title=None
):

    revenue = (
        df.groupby(category_column)[revenue_column]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    revenue.plot(kind="bar", color="steelblue", ax=ax)

    ax.set_title(title or f"Revenue by {category_column.title()}")
    ax.set_xlabel(category_column.title())
    ax.set_ylabel("Total Revenue")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    plt.show()

    return ax


def plot_revenue_over_time(df):
    data = df.copy()
    data["date"] = pd.to_datetime(data["date"])

    daily_revenue = (
        data.groupby("date")["revenue"]
        .sum()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    daily_revenue.plot(ax=ax, color="darkorange")

    ax.set_title("Revenue Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Revenue")

    fig.tight_layout()
    plt.show()

    return ax


def plot_units_sold_by_category_over_time(categories: list[CategorySales]):
    x = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"]
    for category in categories:
        y = [category.january_units_sold, category.february_units_sold,
             category.march_units_sold, category.april_units_sold,
             category.may_units_sold, category.june_units_sold]
        plt.plot(x, y, label = category.category_name)
    plt.ylim(ymin=0)
    plt.title("Units Sold by Month")
    plt.xlabel("2024")
    plt.ylabel("Units Sold")
    plt.legend()
    plt.show()
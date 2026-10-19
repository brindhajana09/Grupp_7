import pandas as pd
import matplotlib.pyplot as plt


def plot_revenue_by_category(
    df,
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
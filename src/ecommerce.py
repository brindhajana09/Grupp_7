from dataclasses import dataclass

from io_utils import convert_number_to_month_english


@dataclass
class CategorySales:
    category_name: str
    total_units_sold: int = 0
    january_units_sold: int = 0
    february_units_sold: int = 0
    march_units_sold: int = 0
    april_units_sold: int = 0
    may_units_sold: int = 0
    june_units_sold: int = 0
    total_revenue: float = 0.0
    january_revenue: float = 0.0
    february_revenue: float = 0.0
    march_revenue: float = 0.0
    april_revenue: float = 0.0
    may_revenue: float = 0.0
    june_revenue: float = 0.0

    def _format_date(self, date: str) -> str:
        return convert_number_to_month_english(
            int(date.split("-")[1].lstrip("0"))).lower()

    def add_entry(self, date: str, units: int, revenue: float):
        month = self._format_date(date)
        sold_attribute = f"{month}_units_sold"
        revenue_attribute = f"{month}_revenue"
        self.total_units_sold += units
        self.total_revenue += revenue
        setattr(self, sold_attribute,
                getattr(self, sold_attribute) + units)
        setattr(self, revenue_attribute,
                round(getattr(self, revenue_attribute) + revenue, 2))
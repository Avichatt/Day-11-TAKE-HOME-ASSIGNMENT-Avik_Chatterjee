import csv
import json
from pathlib import Path
from datetime import datetime

def merge_sales_data():

    folder = Path(".")
    files = list(folder.glob("data*.csv"))

    all_rows = []
    unique_rows = set()

    for file in files:
        with open(file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                key = (row["date"], row["product"], row["qty"], row["price"])

                if key not in unique_rows:
                    unique_rows.add(key)
                    all_rows.append(row)

    # sort by date
    all_rows.sort(key=lambda x: x["date"])

    # calculate revenue
    revenue = {}
    total_revenue = 0

    for row in all_rows:
        product = row["product"]
        qty = int(row["qty"])
        price = float(row["price"])

        rev = qty * price
        total_revenue += rev

        if product not in revenue:
            revenue[product] = 0

        revenue[product] += rev

    # write merged CSV
    with open("merged_sales.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["date", "product", "qty", "price"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(all_rows)

    # JSON metadata
    output = {
        "metadata": {
            "files_processed": len(files),
            "total_rows": len(all_rows),
            "total_revenue": total_revenue,
            "generated_at": datetime.now().isoformat()
        },
        "revenue_by_product": revenue
    }

    with open("revenue_summary.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)


if __name__ == "__main__":
    merge_sales_data()

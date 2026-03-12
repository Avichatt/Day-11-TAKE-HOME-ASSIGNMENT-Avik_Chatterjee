"""
# Part C — Interview Ready

## Q1 — Difference Between json.load() and json.loads()

### json.load()

Definition: json.load() reads JSON data from a file object and converts it into a Python object such as a dictionary or list.
When to use: Use it when JSON data is stored inside a file.
Real-world example: A data analyst loads a configuration file or API response stored as JSON.
"""

import json

def q1_load_example():
    # Example for json.load()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        print(data)
    except FileNotFoundError:
        print("data.json not found for example.")

"""
### json.loads()

Definition: json.loads() reads JSON data from a string and converts it into a Python object.
When to use: Use it when JSON data comes from text, such as: API responses, message queues, web requests.
Real-world example: A web application receives JSON from an API and converts it into Python data.
"""

def q1_loads_example():
    # Example for json.loads()
    text = '{"name": "Laptop", "price": 900}'
    data = json.loads(text)
    print(data["name"])

"""
# Q2 — find_large_files Function
"""

from pathlib import Path

def find_large_files(directory, size_mb):
    folder = Path(directory)
    results = []

    for file in folder.rglob("*"):
        if file.is_file():
            size = file.stat().st_size / (1024 * 1024)
            if size > size_mb:
                results.append((file.name, round(size, 2)))

    results.sort(key=lambda x: x[1], reverse=True)
    return results

# Example usage:
# print(find_large_files(".", 1))

"""
# Q3 — Fixed CSV Merge Code

Fixes applied:
* Added import csv
* Added newline=''
* Skipped duplicate headers using next(reader)
"""

import csv

def merge_csv_files(file_list):
    all_data = []
    header_saved = False

    for filename in file_list:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            if not header_saved:
                all_data.append(header)
                header_saved = True

            for row in reader:
                all_data.append(row)

    with open("merged.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(all_data)

    return len(all_data)

if __name__ == "__main__":
    print("Part C loaded. Functions available: find_large_files, merge_csv_files")
